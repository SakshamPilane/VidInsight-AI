import os
import json
import logging
from dotenv import load_dotenv
from openai import OpenAI
from prompts import SUMMARY_PROMPT, INSIGHTS_PROMPT

# --------------------------------------------------
# INITIALIZATION
# --------------------------------------------------
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

logging.basicConfig(level=logging.INFO)


# --------------------------------------------------
# LOW-LEVEL OPENAI CALL (ISOLATED)
# --------------------------------------------------
def call_openai(prompt: str) -> dict:
    """
    Makes a controlled OpenAI request and guarantees JSON output handling.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        logging.error("Invalid JSON returned from OpenAI")
        raise ValueError("OpenAI returned malformed JSON")


# --------------------------------------------------
# RULE-BASED TOPIC INFERENCE (NLP FALLBACK)
# --------------------------------------------------
def infer_topic_from_keywords(keywords):
    """
    Infers topic category using deterministic keyword rules.
    """
    joined = " ".join(keywords).lower()

    if any(k in joined for k in ["attack", "terror", "mumbai", "security"]):
        return "Terrorism / National Security"

    if any(k in joined for k in ["north", "korea", "government", "censorship"]):
        return "Geopolitics / Technology"

    if any(k in joined for k in ["phone", "android", "device", "smartphone"]):
        return "Technology"

    return "General"


# --------------------------------------------------
# MOCK AI RESPONSE (SAFE FALLBACK)
# --------------------------------------------------
def mock_ai_response(base_summary, keywords):
    """
    Used when OpenAI is unavailable.
    Ensures system remains functional without AI dependency.
    """
    logging.warning("Running in MOCK AI mode")

    return {
        "summary": base_summary,
        "insights": {
            "topic_category": infer_topic_from_keywords(keywords),
            "difficulty_level": "Intermediate",
            "target_audience": "General",
            "sentiment": {
                "label": "Neutral",
                "confidence": 0.6
            },
            "learning_value_score": min(
                90,
                50 + len(keywords) * 3
            )
        },
        "_meta": {
            "mode": "MOCK",
            "reason": "OpenAI unavailable or quota exceeded"
        }
    }


# --------------------------------------------------
# AI ORCHESTRATION LAYER
# --------------------------------------------------
def analyze_with_ai(transcript, base_summary, keywords):
    """
    Orchestrates AI-based enrichment.
    Falls back to rule-based NLP on failure.
    """
    try:
        summary = call_openai(
            SUMMARY_PROMPT.format(transcript=transcript)
        )

        insights = call_openai(
            INSIGHTS_PROMPT.format(transcript=transcript)
        )

        return {
            "summary": summary,
            "insights": insights,
            "_meta": {"mode": "LIVE"}
        }

    except Exception as e:
        logging.exception("AI analysis failed, switching to fallback")
        return mock_ai_response(base_summary, keywords)
