import streamlit as st
from transcript import fetch_transcript
from analytics import basic_analytics, extract_keywords, rule_based_summary
from ai_service import analyze_with_ai


# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="VidInsight AI",
    page_icon="🎥",
    layout="wide"
)

# -------------------- HEADER --------------------
st.title("🎥 VidInsight AI")
st.caption("Interview-Grade Video Intelligence Engine")

st.markdown(
    """
    Analyze YouTube videos using **transcript normalization, rule-based NLP,**
    and **AI-powered insights** — with graceful fallback when AI is unavailable.
    """
)

st.divider()

# -------------------- INPUT SECTION --------------------
video_url = st.text_input(
    "🔗 Enter YouTube Video URL",
    placeholder="https://www.youtube.com/watch?v=XXXXXXXXXXX"
)

generate = st.button("🚀 Generate Insights", use_container_width=True)

# -------------------- MAIN LOGIC --------------------
if generate:

    if not video_url.strip():
        st.error("❌ Please enter a valid YouTube URL before proceeding.")
        st.stop()

    try:
        with st.spinner("🔍 Fetching transcript and analyzing content..."):
            data = fetch_transcript(video_url)

            transcript = data["text"]
            quality = data["quality"]

            analytics = basic_analytics(transcript)
            keywords = extract_keywords(transcript)
            base_summary = rule_based_summary(transcript)

            ai_data = analyze_with_ai(
                transcript,
                base_summary,
                keywords
            )

        st.success("✅ Analysis Complete")

    except RuntimeError as e:
        st.error(f"⚠️ {str(e)}")
        st.stop()

    except Exception:
        st.error(
            "🚨 Unexpected error occurred while processing the video.\n\n"
            "Please try another video or check transcript availability."
        )
        st.stop()

    # -------------------- STATUS BANNER --------------------
    if ai_data.get("_meta", {}).get("mode") == "MOCK":
        st.warning(
            "⚠️ AI is running in **Demo Mode**.\n\n"
            "Insights are generated using rule-based NLP due to API limitations."
        )

    # -------------------- DIAGNOSTICS --------------------
    st.subheader("📊 Transcript Diagnostics")

    st.json({
        "language": data["language"],
        "word_count": data["word_count"],
        "quality_score": quality["quality_score"],
        "auto_captions_detected": quality["auto_captions_detected"],
        "ai_mode": ai_data["_meta"]["mode"]
    })

    # -------------------- TRANSCRIPT VIEW --------------------
    with st.expander("📜 View Full Transcript", expanded=False):
        st.write(transcript)

    st.divider()

    # -------------------- ANALYTICS & INSIGHTS --------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📈 Rule-Based NLP Analytics")
        st.json(analytics)

        st.subheader("🔑 Extracted Keywords")
        if keywords:
            st.markdown(
                " ".join([f"`{k}`" for k in keywords])
            )
        else:
            st.write("No significant keywords detected.")

    with col2:
        st.subheader("🧠 AI / Heuristic Insights")
        st.json(ai_data["insights"])

    st.divider()

    # -------------------- SUMMARY SECTION --------------------
    st.subheader("📝 Video Summary")

    st.markdown("### 🔹 Short Summary")
    st.write(ai_data["summary"]["short_summary"])

    st.markdown("### 🔹 Detailed Summary")
    st.write(ai_data["summary"]["detailed_summary"])

    st.markdown("### 🔹 Key Points")
    for idx, point in enumerate(ai_data["summary"]["key_points"], start=1):
        st.markdown(f"**{idx}.** {point}")
