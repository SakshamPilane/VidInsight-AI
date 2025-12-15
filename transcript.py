from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound
)
import re


# --------------------------------------------------
# URL → VIDEO ID EXTRACTION
# --------------------------------------------------
def extract_video_id(url: str) -> str:
    """
    Extracts YouTube video ID from a standard YouTube URL.
    """
    if not url or "v=" not in url:
        raise ValueError("Invalid YouTube URL format")

    return url.split("v=")[1].split("&")[0]


# --------------------------------------------------
# TRANSCRIPT CLEANING & NORMALIZATION
# --------------------------------------------------
def clean_text(text: str) -> str:
    """
    Normalizes raw transcript text:
    - Fixes auto-caption character spacing (e.g. 'I t w a s')
    - Removes bracketed annotations [Music], [Applause]
    - Normalizes whitespace and punctuation
    """
    if not text:
        return ""

    # Fix extreme auto-caption spacing
    if re.search(r"(?:\b\w\s){5,}", text):
        text = re.sub(r"\b(\w)\s+(?=\w\b)", r"\1", text)

    text = re.sub(r"\[.*?\]", "", text)
    text = text.replace("′", "'")
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# --------------------------------------------------
# TRANSCRIPT QUALITY HEURISTICS
# --------------------------------------------------
def assess_quality(text: str) -> dict:
    """
    Heuristically determines transcript quality.
    Used for UI diagnostics & fallback decisions.
    """
    words = text.split()
    if not words:
        return {
            "quality_score": 0.0,
            "auto_captions_detected": True
        }

    avg_word_len = sum(len(w) for w in words) / len(words)
    sentence_count = (
        text.count(".") +
        text.count("?") +
        text.count("!")
    )

    auto_caption = avg_word_len < 4 or sentence_count < 5
    score = round(
        min(1.0, (avg_word_len / 5) + (sentence_count / 100)),
        2
    )

    return {
        "quality_score": score,
        "auto_captions_detected": auto_caption
    }


# --------------------------------------------------
# TRANSCRIPT FETCHING
# --------------------------------------------------
def fetch_transcript(video_url: str) -> dict:
    """
    Fetches and processes transcript for a YouTube video.
    Gracefully handles disabled or missing subtitles.
    """
    video_id = extract_video_id(video_url)
    api = YouTubeTranscriptApi()

    try:
        transcript_list = api.list(video_id)

        try:
            # Prefer English transcripts
            transcript = transcript_list.find_transcript(["en"])
        except NoTranscriptFound:
            # Fallback to first available transcript
            transcript = next(iter(transcript_list))

        transcript_data = transcript.fetch()

    except TranscriptsDisabled:
        raise RuntimeError(
            "Subtitles are disabled for this video. "
            "VidInsight AI requires transcripts to function."
        )

    except NoTranscriptFound:
        raise RuntimeError(
            "No transcript found for this video. "
            "Please try a different video."
        )

    except Exception:
        raise RuntimeError(
            "Failed to retrieve transcript due to an unexpected error."
        )

    # youtube-transcript-api returns objects, not dicts
    raw_text = " ".join(item.text for item in transcript_data)

    clean = clean_text(raw_text)
    quality = assess_quality(clean)

    return {
        "video_id": video_id,
        "language": transcript.language_code,
        "word_count": len(clean.split()),
        "text": clean,
        "quality": quality
    }
