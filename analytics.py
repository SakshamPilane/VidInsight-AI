import re
from collections import Counter


# --------------------------------------------------
# BASIC STOPWORD SET (CUSTOMIZED FOR TRANSCRIPTS)
# --------------------------------------------------
STOPWORDS = {
    "the", "is", "and", "to", "of", "a", "in", "that", "it", "you",
    "for", "on", "with", "as", "this", "but", "be", "are", "or",
    "have", "not", "at", "by", "from", "they", "i", "we", "he", "she",
    "there", "these", "after", "their", "which", "people", "been",
    "was", "were", "had", "has", "him", "her", "his", "its"
}


# --------------------------------------------------
# BASIC TRANSCRIPT ANALYTICS
# --------------------------------------------------
def basic_analytics(text: str) -> dict:
    """
    Computes basic descriptive statistics from transcript text.
    """
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())

    return {
        "word_count": len(words),
        "estimated_video_duration_minutes": round(len(words) / 155, 2),
        "sentence_count": max(
            1,
            text.count(".") + text.count("?") + text.count("!")
        )
    }


# --------------------------------------------------
# KEYWORD EXTRACTION (RULE-BASED NLP)
# --------------------------------------------------
def extract_keywords(text: str, top_n: int = 15):
    """
    Extracts important keywords using frequency-based NLP heuristics.
    """
    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())

    filtered = [
        w for w in words
        if w not in STOPWORDS
        and len(w) > 4
        and w.isalpha()
    ]

    frequency = Counter(filtered)
    return [word for word, _ in frequency.most_common(top_n)]


# --------------------------------------------------
# KEY POINT EXTRACTION (SENTENCE RANKING)
# --------------------------------------------------
def extract_key_points(text: str, max_points: int = 6):
    """
    Selects the most informative sentences based on keyword density.
    """
    sentences = re.split(r"[.!?]", text)
    sentences = [
        s.strip() for s in sentences
        if len(s.strip()) > 60
    ]

    keywords = extract_keywords(text, top_n=15)
    ranked = []

    for sentence in sentences:
        score = sum(
            1 for k in keywords if k in sentence.lower()
        )
        ranked.append((score, sentence))

    ranked.sort(reverse=True, key=lambda x: x[0])
    return [sentence for _, sentence in ranked[:max_points]]


# --------------------------------------------------
# RULE-BASED SUMMARY GENERATION
# --------------------------------------------------
def rule_based_summary(text: str):
    """
    Generates a structured summary using rule-based NLP.
    Acts as a fallback when AI is unavailable.
    """
    keywords = extract_keywords(text, top_n=15)
    key_points = extract_key_points(text, max_points=5)

    if keywords:
        short_summary = (
            "This video provides a structured explanation of "
            f"{', '.join(keywords[:3])}, highlighting key events, "
            "background context, and important outcomes."
        )
    else:
        short_summary = (
            "This video presents a structured explanation of the topic, "
            "supported by real-world context and examples."
        )

    detailed_summary = " ".join(key_points)

    return {
        "short_summary": short_summary,
        "detailed_summary": detailed_summary,
        "key_points": key_points
    }
