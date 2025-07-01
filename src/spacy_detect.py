# ========================================================================================
# spacy_detect.py (With Advanced Country Validation)
#
# FILE OVERVIEW:
# This module uses an advanced, multi-layered process for country detection:
# 1. It uses spaCy's NER model to extract potential place names (GPEs).
# 2. For each place, it first tries to match it against an official list of countries.
# 3. If that fails, it checks if the place is a known subdivision (state/province).
# 4. If a subdivision is found, it looks up the parent country, ensuring that
#    mentions of "California" or "London" correctly resolve to their country.
# ========================================================================================

import spacy
import pycountry  # Import the main pycountry library
from transformers import pipeline
from error_log import setup_logger

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


def detect_country_ner(text):
    """
    Detects, validates, and normalizes the most likely country mentioned in a text.
    It prioritizes direct country matches before checking for states or provinces.
    """
    if not nlp:
        logger.warning("spaCy model not available. Skipping NER country detection.")
        return "Unknown"

    doc = nlp(text)
    potential_locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    # --- Advanced Validation and Normalization Loop ---
    for loc in potential_locations:
        try:
            # --- Step 1: Try to match as a country first ---
            country_match = pycountry.countries.search_fuzzy(loc)
            if country_match:
                official_name = country_match[0].name
                logger.debug(f"NER found '{loc}', validated as COUNTRY: '{official_name}'")
                return official_name

            # --- Step 2: If not a country, check if it's a known state/province ---
            subdivision_match = pycountry.subdivisions.search_fuzzy(loc)
            if subdivision_match:
                # Get the country code (e.g., 'US' for California) from the subdivision
                country_code = subdivision_match[0].country_code
                # Look up the parent country using that code
                parent_country = pycountry.countries.get(alpha_2=country_code)
                if parent_country:
                    official_name = parent_country.name
                    logger.debug(f"NER found '{loc}', validated as SUBDIVISION of: '{official_name}'")
                    return official_name

        except Exception:
            # If any search fails, just continue to the next potential location.
            continue
    
    # If the loop finishes with no valid matches, return "Unknown".
    logger.debug(f"spaCy found potential locations {potential_locations}, but none were validated.")
    return "Unknown"


def detect_category_zero_shot(text, categories):
    """
    Detects the most likely category for a text using a Zero-Shot Classification model.
    """
    if not classifier:
        logger.warning("Hugging Face classifier not available. Skipping category detection.")
        return "General"
    
    if not text or len(text) < 10:
        return "General"

    try:
        # Set multi_label to False to force the model to choose only the best category.
        result = classifier(text, candidate_labels=categories, multi_label=False)
        detected_category = result['labels'][0]
        score = result['scores'][0]
        
        logger.debug(f"Detected category: {detected_category} (Score: {score:.2f})")
        # Only accept a category if the model is at least 50% confident.
        if score > 0.5:
            return detected_category
        else:
            return "General"
    except Exception as e:
        logger.error(f"Error during category classification: {e}")
        return "General"
