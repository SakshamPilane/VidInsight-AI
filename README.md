# 🎥 VidInsight AI  
### Interview-Grade Video Intelligence Engine

VidInsight AI is a **video intelligence system** that extracts, cleans, and analyzes YouTube video transcripts using **deterministic, rule-based NLP techniques**, with optional **AI-powered enhancement** for summaries and insights.

Unlike basic “AI-only” summarizers, VidInsight AI prioritizes **structured transcript understanding first**, and uses AI strictly as an **augmentation layer** — with **graceful fallback** when AI is unavailable.  
This makes the system **explainable, reliable, and interview-ready**.

---

## 🚀 Key Features

### 📜 Transcript Processing
- Extracts transcripts from YouTube videos
- Normalizes auto-caption artifacts (spacing errors, noise, symbols)
- Handles missing or disabled transcripts gracefully
- Detects auto-generated captions
- Computes transcript quality metrics

### 🧠 NLP-Based Analysis (No Black Box)
- Keyword extraction using frequency-based NLP
- Stopword filtering with a curated vocabulary
- Sentence relevance scoring
- Rule-based summarization
- Fully deterministic and explainable outputs

> **Note:** NLP in this project is implemented using rule-based techniques  
> (regex, frequency analysis, sentence scoring) — **not machine learning models**.

### 🤖 AI Enhancement (Optional)
- AI-generated summaries and insights using OpenAI
- Strict JSON-based prompt contracts
- Automatic fallback to NLP-only mode on API failure
- Clear UI indication of AI mode (**LIVE / MOCK**)

### 🖥️ Interactive UI
- Built with Streamlit
- Transcript diagnostics panel
- Expandable full transcript view
- Side-by-side analytics and insights
- Clean, minimal, interview-ready layout

### ⚠️ Failure Handling & Edge Cases
- Videos with disabled transcripts are handled with clear user feedback
- Auto-generated captions are detected and normalized
- AI API failures automatically trigger rule-based fallback
- System mode (LIVE / MOCK) is explicitly shown in the UI

---

## 🧩 System Architecture

- 📐 **System Architecture Diagram**  
  → [View](docs/diagrams/system_architecture.png)

- 🔄 **Data Flow Diagram**  
  → [View](docs/diagrams/data_flow.png)

- 🤖 **AI Fallback Flow**  
  → [View](docs/diagrams/ai_fallback_flow.png)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **youtube-transcript-api**
- **Rule-based NLP (regex, frequency analysis)**
- **OpenAI API** (optional)

---

## 📂 Project Structure

📄 **Project Structure Diagram**  
→ [View](docs/diagrams/project_structure.png)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/SakshamPilane/VidInsight-AI.git
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
