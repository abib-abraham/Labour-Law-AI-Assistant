# 📘 Labour Law AI Assistant

**A Multilingual Generative AI-Based Labour Law Assistant Using Retrieval-Augmented Generation (RAG)**

[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/AI-LangChain-green)](https://www.langchain.com/)
[![FAISS](https://img.shields.io/badge/Vector%20Database-FAISS-orange)](https://github.com/facebookresearch/faiss)
[![Ollama](https://img.shields.io/badge/LLM-Ollama-black)](https://ollama.com/)

## 1. Project Overview

The **Labour Law AI Assistant** is a multilingual, AI-powered chatbot designed to help users understand Indian Labour Laws through natural language interaction.

The application uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from uploaded Labour Law FAQ documents and generate contextual responses using a locally running Large Language Model (LLM).

The system supports English, Hindi and Malayalam responses, offline text-to-speech functionality, conversational memory and customer query analytics.

The project aims to make Labour Law information easier to access and understand through Generative AI.

## 2. Key Features

- **RAG-Based Question Answering:** Retrieves relevant information from Labour Law PDF documents using FAISS.
- **Generative AI Integration:** Uses Gemma 2B through Ollama to generate answers.
- **Multilingual Support:** Supports English, Hindi and Malayalam responses.
- **Automatic Language Detection:** Detects Hindi and Malayalam scripts when Auto Detect is selected; defaults to English otherwise.
- **Conversational Memory:** Maintains recent conversation context during a Streamlit session.
- **Voice Output:** Uses Piper TTS for offline text-to-speech in three supported languages.
- **Streaming Responses:** Displays generated answers with a word-by-word visual effect.
- **Suggested Questions:** Provides predefined Labour Law questions for easier interaction.
- **SQLite Analytics:** Records customer questions, classified topics, selected languages and timestamps.
- **FAQ Document Analysis:** Displays configured topic coverage based on the uploaded FAQ documents.
- **Customer Query Dashboard:** Shows frequently asked topics, language distribution and recent queries.
- **CSV Export:** Allows customer query analytics to be downloaded as a CSV file.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| LLM | Gemma 2B |
| Local LLM Runtime | Ollama |
| RAG Framework | LangChain |
| Vector Database | FAISS |
| Embedding Model | paraphrase-multilingual-MiniLM-L12-v2 |
| Document Processing | PyPDF / LangChain document loaders |
| Text-to-Speech | Piper TTS |
| Analytics Database | SQLite |
| Data Analysis | Pandas |
| Visualization | Streamlit Charts |

## 4. System Architecture

The application follows a Retrieval-Augmented Generation architecture.

1. Labour Law FAQ PDFs are loaded and processed.
2. Documents are divided into smaller text chunks.
3. The embedding model converts text chunks into vector representations.
4. FAISS stores the generated vectors for similarity-based retrieval.
5. A user submits a question through the Streamlit interface.
6. The system retrieves relevant document content.
7. Retrieved context is passed to Gemma 2B through Ollama.
8. The LLM generates a contextual response.
9. Piper generates speech from the response.
10. SQLite records the submitted question for analytics.

## 5. Project Structure

```text
Labour-Law-AI-Assistant/
│
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── labour_rules_1.pdf
│   └── labour_rules_2.pdf
│
├── logos/
│   ├── labour_ai_logo.png
│   ├── Wadhwani-Foundation-Logo.png
│   ├── ashoka_emblem.png
│   └── labour_commission_logo.png
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
├── en_US-lessac-medium.onnx
├── en_US-lessac-medium.onnx.json
├── hi_IN-pratham-medium.onnx
├── hi_IN-pratham-medium.onnx.json
├── ml_IN-arjun-medium.onnx
└── ml_IN-arjun-medium.onnx.json
```

The SQLite analytics database is generated locally when the application runs and is excluded from GitHub.

## 6. Installation and Setup

### Prerequisites

- Python 3.12 recommended
- Git
- Ollama
- Gemma 2B model
- Required Python packages

### Step 1: Clone the repository

```bash
git clone https://github.com/abib-abraham/Labour-Law-AI-Assistant.git
cd Labour-Law-AI-Assistant
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Install and configure Ollama

Install Ollama from:

https://ollama.com/

Download the Gemma 2B model:

```bash
ollama pull gemma:2b
```

### Step 5: Generate the vector database

If the FAISS vector database is not available, generate it from the PDF documents:

```bash
python ingest.py
```

### Step 6: Run the application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 7. Analytics Module

The application includes a Labour Law Analytics dashboard powered by SQLite.

It provides two distinct types of analysis:

**A. FAQ Document Analysis**
- Displays topic-wise FAQ coverage.
- Identifies the topics represented in the configured FAQ distribution.
- Provides a visual representation of document coverage.

**B. Customer Query Analysis**
- Total recorded questions.
- Number of topics asked about.
- Most frequently asked topic.
- Topic-wise question distribution.
- Language distribution.
- Recent customer questions.
- CSV export functionality.

Customer query information is stored locally in `labour_analytics.db`. The database is excluded from the public repository.

**Note:** FAQ coverage values are manually configured in the current implementation. They are not automatically calculated from the PDF contents.

## 8. Supported Languages

| Language | Text Response | Voice Output |
|---|---|---|
| English | Yes | Yes |
| Hindi | Yes | Yes |
| Malayalam | Yes | Yes |

The application provides a language selection option and automatic detection for Hindi and Malayalam scripts.

## 9. Current Limitations

- The knowledge base is limited to the Labour Law PDF documents currently included in the project.
- Answer quality depends on document retrieval and the capabilities of the selected LLM.
- Malayalam generation quality may vary depending on the local model.
- Topic classification in analytics currently uses keyword-based rules.
- FAQ document coverage is manually configured.
- Conversational memory is maintained within the active Streamlit session.
- The application does not independently verify legal updates or replace professional legal advice.

## 10. Future Scope

Potential future improvements include:

- PDF source citations and page references.
- Voice-based question input.
- Improved semantic query classification.
- Advanced query trend analysis.
- User feedback and answer-quality evaluation.
- Automated unanswered-question detection.
- Labour complaint letter generation.
- Knowledge-base management and document uploads.
- Improved multilingual model performance.

## 11. Repository

**GitHub:**  
https://github.com/abib-abraham/Labour-Law-AI-Assistant

## 12. Conclusion

The Labour Law AI Assistant demonstrates how Generative AI and Retrieval-Augmented Generation can be applied to make legal information more accessible.

By combining local LLM inference, document retrieval, multilingual interaction, offline speech generation and query analytics, the project provides an integrated approach to Labour Law information assistance.

---

**Project:** Labour Law AI Assistant  
**Domain:** Generative AI | Natural Language Processing | Retrieval-Augmented Generation  
**Repository:** https://github.com/abib-abraham/Labour-Law-AI-Assistant