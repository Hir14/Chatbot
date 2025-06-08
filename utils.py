

import string
from difflib import get_close_matches

def preprocess(text):
    """Converts to lowercase and removes punctuation."""
    text = text.lower()
    return text.translate(str.maketrans('', '', string.punctuation))

def find_match(user_input, knowledge):
    """Find best matching response from the knowledge base."""
    processed = preprocess(user_input)
    questions = [preprocess(q) for q in knowledge]

    # Exact match
    if processed in questions:
        return knowledge[list(knowledge.keys())[questions.index(processed)]]

    # Fuzzy match
    close_matches = get_close_matches(processed, questions, n=1, cutoff=0.6)
    if close_matches:
        match = close_matches[0]
        return knowledge[list(knowledge.keys())[questions.index(match)]]

    return "I'm not sure how to respond to that."
