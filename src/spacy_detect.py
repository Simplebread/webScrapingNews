# ========================================================================================
# spacy_detect.py (With Advanced Country Validation)
#
# FILE OVERVIEW:
# This module uses an advanced, multi-layered process for country detection:
# It uses spaCy's NER model to extract potential place names (GPEs).
# For each place, it first tries to match it against an official list of countries.
# If that fails, it checks if the place is a known subdivision (state/province).
# If a subdivision is found, it looks up the parent country.
# It prioritizes returning a country's "common name" (e.g., "South Korea")
#    instead of its formal name ("Korea, Republic of") for cleaner data.
# ========================================================================================

import spacy
import pycountry  # Import the main pycountry library
from transformers import pipeline
from error_log import setup_logger
from langdetect import detect, DetectorFactory
from deep_translator import GoogleTranslator

# Set up a logger for this specific file
logger = setup_logger(__name__)


# --- Load AI Models ---
try:
    nlp = spacy.load("en_core_web_sm")
    logger.info("spaCy NLP model 'en_core_web_sm' loaded successfully.")
except OSError:
    logger.error("spaCy model 'en_core_web_sm' not found. Please run 'python -m spacy download en_core_web_sm'")
    nlp = None

try:
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    logger.info("Hugging Face Zero-Shot Classification model loaded successfully.")
except Exception as e:
    logger.error(f"Could not load the Hugging Face model. Error: {e}")
    classifier = None

# Ensure reproducible results
DetectorFactory.seed = 0

def detect_lang(text):
    """
    Returns the ISO 639-1 language code for `text`, e.g. "en", "zh-cn", "hi".
    Falls back to "unknown" on errors or very short text.
    """
    try:
        # langdetect returns codes like "en", "fr", "zh-cn", "hi", etc.
        return detect(text)
    except Exception:
        return "unknown"
    
def get_country_name(country_object):
    """
    Returns the common name of a country if it exists, otherwise the official name.
    This helps turn 'Iran, Islamic Republic of' into just 'Iran'.
    """
    # The 'hasattr' check is a safe way to see if the common_name attribute is available.
    if hasattr(country_object, 'common_name'):
        return country_object.common_name
    return country_object.name

def ensure_english(text):
    if not text or text.strip() == "":
        return text
    try:
        return GoogleTranslator(source="auto", target="en").translate(text)
    except Exception as e:
        logger.warning(f"Translation failed (auto→en): {e}; using original text.")
        return text

def detect_country_ner(text):
    """
    Detects, validates, and normalizes the most likely country mentioned in a text.
    It prioritizes direct country matches before checking for states or provinces.
    """
    lang = detect_lang(text)
    if lang!= "en":
        text_for_ner = ensure_english(text)
    else:
        text_for_ner = text

    if not nlp:
        logger.warning("English spaCy model not available. Skipping NER country detection.")
        return "Unknown"

    doc = nlp(text_for_ner)
    potential_locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    for loc in potential_locations:
        try:
            # --- Step 1: Try to match as a country first ---
            country_match = pycountry.countries.search_fuzzy(loc)
            if country_match:
                official_name = get_country_name(country_match[0])
                logger.debug(f"NER found '{loc}', validated as COUNTRY: '{official_name}'")
                return official_name

            # --- Step 2: If not a country, check if it's a known state/province ---
            subdivision_match = pycountry.subdivisions.search_fuzzy(loc)
            if subdivision_match:
                country_code = subdivision_match[0].country_code
                parent_country = pycountry.countries.get(alpha_2=country_code)
                if parent_country:
                    official_name = get_country_name(parent_country)
                    logger.debug(f"NER found '{loc}', validated as SUBDIVISION of: '{official_name}'")
                    return official_name

        except Exception:
            # If any search fails (e.g., a location is not in the database), just continue.
            continue
    
    # If the loop finishes with no valid matches, return "Unknown".
    logger.debug(f"spaCy found potential locations {potential_locations}, but none were validated.")
    return "Unknown"


def detect_category_zero_shot(text, categories):
    """
    Detects the most likely category and the word that most influenced the choice.
    """

    lang = detect_lang(text)
    if lang!= "en":
        text_for_zero_shot = ensure_english(text)
    else:
        text_for_zero_shot = text

    if not classifier:
        logger.warning("Hugging Face classifier not available. Skipping category detection.")
        return "General"
    
    if not text or len(text) < 10:
        return "General"

    try:
        # --- Step 1: Classify the entire text ---
        result = classifier(text_for_zero_shot, candidate_labels=categories, multi_label=False)
        detected_category = result['labels'][0]
        score = result['scores'][0]
        
        # Only accept a category if the model is confident enough.
        if score <= 0.25:
            logger.debug(f"Top category '{detected_category}' was below confidence threshold (Score: {score:.2f}). Defaulting to General.")
            return "General"

        # split the text into individual words to test each one.
        words = text_for_zero_shot.split()
        trigger_word = None
        highest_word_score = -1

        # This loop finds which single word gets the highest score for the winning category.
        for word in words:
            # classify just the single word against our winning category.
            word_result = classifier(word, candidate_labels=[detected_category], multi_label=False)
            current_word_score = word_result['scores'][0]
            
            if current_word_score > highest_word_score:
                highest_word_score = current_word_score
                trigger_word = word
        
        if trigger_word:
            logger.debug(f"Category: '{detected_category}' (Score: {score:.2f}). Triggered by keyword: '{trigger_word}'")
        else:
            logger.debug(f"Category: '{detected_category}' (Score: {score:.2f}). No specific trigger word found.")

        return detected_category

    except Exception as e:
        logger.error(f"Error during category classification: {e}")
        return "General"
