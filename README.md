# 🧠 ToxiGuard AI

## Hybrid Explainable Toxicology Triage System

ToxiGuard AI is a **Hybrid Retrieval-Augmented Generation (RAG) based Toxicology Assistant** designed to deliver **evidence-grounded, explainable, and safety-aware poisoning triage recommendations**.

This system combines:

* 📄 Vector-based document retrieval
* 🧠 LLM-powered reasoning (Cohere)
* 🛡 Rule-assisted safety guardrails
* ⚡ FastAPI production deployment

---

## 🚀 Features

* ✅ Hybrid RAG Architecture (Documents + Dynamic Reasoning)
* ✅ PDF-based Knowledge Ingestion
* ✅ FAISS Vector Database
* ✅ Cohere Embeddings + Command Model
* ✅ Rule-Based Clinical Safety Layer
* ✅ Explainable Step-by-Step Reasoning
* ✅ Structured JSON Output
* ✅ FastAPI REST API Deployment
* ✅ Swagger UI Testing Interface

---

## 🏗 System Architecture

```
User Input
    ↓
Safety Rule Engine
    ↓
Hybrid RAG Retrieval
    ├── Vector Search (FAISS + PDF)
    └── Contextual LLM Reasoning
    ↓
Explainable AI Generation
    ↓
Structured Triage Output
```

---

## 🛠 Technologies Used

* Python 3.12
* FastAPI
* Cohere API (Command Model + Embeddings)
* FAISS (Vector Similarity Search)
* Pydantic
* PyPDF
* LangChain Text Splitter
* Uvicorn
* VS Code + Virtual Environment

---

## 📂 Project Structure

```
RAG/
│
├── data/
│   └── toxicology_study.pdf
│
├── config.py
├── rag_engine.py
├── safety_layer.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/toxiguard-ai.git
cd toxiguard-ai
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add Cohere API Key

Create a `.env` file:

```
COHERE_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --port 8001
```

Open in browser:

```
http://127.0.0.1:8001/docs
```

---

## 🧪 Example API Request

POST `/triage`

```json
{
  "case_description": "A 28 year old farmer ingested organophosphate pesticide and is vomiting."
}
```

---

## 📤 Example API Response

```json
{
  "risk_level": "HIGH",
  "reason": "High-risk toxic exposure detected",
  "recommended_action": "Urgent emergency evaluation required",
  "explainable_analysis": "Step-by-step reasoning..."
}
```

---

## 🛡 Safety Layer

The rule engine classifies cases into:

* 🔴 CRITICAL
* 🟠 HIGH
* 🟡 MODERATE

Based on:

* Red-flag symptoms
* Toxic exposure keywords
* Pediatric cases
* Severity indicators

---

## 🧠 Hybrid RAG Design

### Document Mode

* Ingests `toxicology_study.pdf`
* Chunks text
* Generates embeddings
* Stores in FAISS
* Retrieves top-k relevant passages

### Augmented Generation

* Retrieved context injected into prompt
* Cohere Command model generates structured explanation

---

## 🏥 Disclaimer

This project is for educational and research purposes only.
It does not replace professional medical advice.

---

## 📈 Future Improvements

* Persistent FAISS storage
* Confidence scoring
* Structured citation extraction
* Toxic category classifier
* Docker deployment
* Cloud hosting (AWS / Azure)

---

## 📌 Keywords

Hybrid RAG, Retrieval-Augmented Generation, Explainable AI, Medical AI, Toxicology AI, FastAPI, Cohere API, Vector Database, FAISS, Clinical Decision Support, Healthcare AI

---

## 👨‍💻 Author

**ToxiGuard AI Project**
Hybrid Explainable Toxicology Triage System


