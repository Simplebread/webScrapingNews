# ========================================================================================
# nlp_processor.py
#
# FILE OVERVIEW:
# This module contains advanced Natural Language Processing (NLP) functions for
# automatically detecting entities and classifying text. It replaces the old
# keyword-based detection in 'filter.py' with more intelligent, AI-powered models.
# This makes the data enrichment process much more accurate and scalable.
# ========================================================================================

import spacy
from transformers import pipeline
from error_log import setup_logger

# Set up a logger for this specific file
logger = setup_logger(__name__)

# --- spaCy Model for Named Entity Recognition (NER) ---
try:
    nlp = spacy.load("en_core_web_sm")
    logger.info("spaCy NLP model 'en_core_web_sm' loaded successfully.")
except OSError:
    logger.error("spaCy model 'en_core_web_sm' not found. Please run 'python -m spacy download en_core_web_sm'")
    nlp = None


# --- Hugging Face Transformers Pipeline for Zero-Shot Classification ---
# This sets up a "pipeline" for text classification. The "zero-shot" part means
# we can give it any list of categories we want, and it will classify the text
# without needing to be pre-trained on those specific labels.
try:
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    logger.info("Hugging Face Zero-Shot Classification model loaded successfully.")
except Exception as e:
    logger.error(f"Could not load the Hugging Face model. You may need an internet connection. Error: {e}")
    classifier = None


def detect_country_ner(text):
    """
    Detects the most likely country mentioned in a text using spaCy's NER.
    It looks for 'GPE' (Geopolitical Entity) labels.
    """
    # First, check if the NLP model was loaded correctly.
    if not nlp:
        logger.warning("spaCy model not available. Skipping NER country detection.")
        return "Unknown"

    # Process the text with the spaCy model.
    doc = nlp(text)

    # Find all entities labeled as a Geopolitical Entity (country, city, state).
    countries = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    if countries:
        # If countries were found, return the first one as the most likely candidate.
        detected_country = countries[0]
        logger.debug(f"Detected country using NER: {detected_country}")
        return detected_country
    else:
        # If no GPEs were found, default to Unknown.
        logger.debug("No country detected using NER.")
        return "Unknown"


def detect_category_zero_shot(text, categories):
    """
    Detects the most likely category for a text using a Zero-Shot Classification model.
    """
    # Check if the classifier model was loaded correctly.
    if not classifier:
        logger.warning("Hugging Face classifier not available. Skipping category detection.")
        return "General"
    
    # The model works best on slightly longer text, so we check the length.
    if not text or len(text) < 10:
        return "General"

    try:
        # The classifier returns a dictionary with labels and scores.
        # We pass the text and our list of candidate labels.
        result = classifier(text, candidate_labels=categories)
        # The labels are sorted by score, so the first one is the best match.
        detected_category = result['labels'][0]
        score = result['scores'][0]
        
        logger.debug(f"Detected category: {detected_category} (Score: {score:.2f})")
        # You can add a threshold if you want to be more confident.
        if score > 0.5:
            return detected_category
        else:
            return "General"
    except Exception as e:
        logger.error(f"Error during category classification: {e}")
        return "General"
