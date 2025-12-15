# 🎥 VidInsight AI  
### Interview-Grade Video Intelligence Engine

VidInsight AI is a **video intelligence system** that extracts, cleans, and analyzes YouTube video transcripts using **rule-based NLP techniques**, with optional **AI-powered enhancement** for summaries and insights.

Unlike basic AI summarizers, this project focuses on **deterministic transcript understanding first**, and uses AI only as an enhancement layer — with graceful fallback when AI is unavailable.

---

## 🚀 Key Features

### 📜 Transcript Processing
- Extracts transcripts from YouTube videos
- Normalizes auto-caption artifacts (spacing, noise, symbols)
- Handles missing or disabled transcripts gracefully
- Detects auto-generated captions and transcript quality

### 🧠 NLP-Based Analysis (No Black Box)
- Keyword extraction using frequency-based NLP
- Stopword filtering with curated vocabulary
- Sentence relevance scoring
- Rule-based summarization
- Deterministic, explainable outputs

### 🤖 AI Enhancement (Optional)
- AI-generated summaries and insights using OpenAI
- Strict JSON-based prompt control
- Automatic fallback to NLP-only mode if API quota fails
- Clear UI indication of AI mode (LIVE / MOCK)

### 🖥️ Interactive UI
- Built using Streamlit
- Transcript diagnostics panel
- Expandable full transcript view
- Side-by-side analytics and insights
- Clean, interview-ready presentation

---

## 🧩 System Architecture
- 📐 [System Architecture](docs/diagrams/system_architecture.png)
- 🔄 [Data Flow Diagram](docs/diagrams/data_flow.png)
- 🤖 [AI Fallback Flow](docs/diagrams/ai_fallback_flow.png)


---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **youtube-transcript-api**
- **Regex-based NLP**
- **OpenAI API** (optional)

---

## 📂 Project Structure

📄 [View Project Structure Diagram](docs/diagrams/project_structure.png)


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/VidInsight-AI.git
cd VidInsight-AI
```

### 2️⃣ Create Virtual Environment
```bash
conda activate base
# or
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install streamlit youtube-transcript-api python-dotenv openai
```

### 4️⃣ Add OpenAI API Key
#### Create a .env file:
```bash
OPENAI_API_KEY=your_api_key_here
```
If no API key is provided, the system automatically runs in safe demo mode.

### 5️⃣ Run the App
```bash
streamlit run app.py
```

---

## 🧪 Example Outputs

- Transcript diagnostics (language, word count, quality)
- NLP-extracted keywords
- Rule-based summaries
- AI-generated insights (if enabled)
- Full transcript viewer

---

## 🎯 Design Philosophy

AI should enhance understanding, not replace structured analysis.
This project prioritizes:
- Explainability
- Reliability
- Graceful degradation
- Interview-level clarity

---

## 👤 Author
Saksham Pilane
B.Tech CSE (Final Year)
Aspiring Backend / Software Developer


---

## 📌 License

This project is licensed under the **MIT License** and is intended for
educational and interview demonstration purposes.

🔗 [View License](https://github.com/SakshamPilane/VidInsight-AI/blob/main/LICENSE)
