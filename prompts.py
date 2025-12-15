SUMMARY_PROMPT = """
You are an expert content analyst.

Your task is to summarize a YouTube video transcript clearly and accurately.

RULES:
- Do NOT invent facts.
- Do NOT use filler words.
- Focus on what the video is actually about (events, concepts, timeline).
- Keywords must be meaningful nouns or noun phrases.
- Avoid stopwords like: after, there, these, which, people, their.

Return ONLY valid JSON in this exact structure:

{
  "short_summary": "2–3 sentence high-level overview of the video",
  "detailed_summary": "A concise but informative paragraph explaining the main narrative",
  "key_points": [
    "Bullet point capturing a major event, idea, or insight",
    "Another important takeaway"
  ],
  "keywords": [
    "important_keyword_1",
    "important_keyword_2",
    "important_keyword_3"
  ],
  "hashtags": [
    "#keyword1",
    "#keyword2",
    "#keyword3"
  ]
}

Transcript:
{transcript}
"""

INSIGHTS_PROMPT = """
You are analyzing a video transcript to extract high-level insights.

RULES:
- Base your analysis ONLY on the transcript.
- Be realistic and conservative.
- Confidence values must be between 0.0 and 1.0.
- Learning value should reflect informational depth, not entertainment.

Return ONLY valid JSON in this exact structure:

{
  "topic_category": "Broad domain such as Technology, Geopolitics, Security, Education",
  "difficulty_level": "Beginner | Intermediate | Advanced",
  "target_audience": "Who would benefit most from this video",
  "sentiment": {
    "label": "Positive | Neutral | Negative",
    "confidence": 0.0
  },
  "learning_value_score": 0
}

Transcript:
{transcript}
"""
