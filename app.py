# import streamlit as st
# from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEmbeddings
# import ollama
# import time

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="Labour Law AI Assistant", layout="wide")

# # ---------------- HEADER ----------------

# # Top-left logo (clean & small)
# st.logo("logos/labour_ai_logo.png", size="large")

# # Main title
# st.markdown("## 📘 Labour Law AI Assistant")
# st.caption("AI powered assistant for Indian Labour Law documents")

# # ---------------- POWERED BY SECTION ----------------

# col1, col2, col3 = st.columns([1,2,6])

# with col1:
#     st.markdown("**Powered by**")

# with col2:
#     st.image("logos/Wadhwani-Foundation-Logo.png", width=120)

# # ---------------- LANGUAGE SELECT ----------------
# if "language" not in st.session_state:
#     st.session_state.language = "Auto Detect"

# language = st.selectbox(
#     "Response Language",
#     ["Auto Detect","English","Hindi","Malayalam"],
#     index=["Auto Detect","English","Hindi","Malayalam"].index(st.session_state.language)
# )

# st.session_state.language = language

# # ---------------- LOAD EMBEDDINGS ----------------
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
# )

# # ---------------- LOAD VECTOR DB ----------------
# db = FAISS.load_local(
#     "vectorstore",
#     embeddings,
#     allow_dangerous_deserialization=True
# )

# # ---------------- MEMORY ----------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # ---------------- DISPLAY CHAT HISTORY ----------------
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # ---------------- USER INPUT ----------------
# query = st.chat_input("Ask about Indian Labour Laws")

# if query:

#     st.session_state.messages.append({"role":"user","content":query})

#     with st.chat_message("user"):
#         st.markdown(query)

#     # ---------------- HINGLISH NORMALIZATION ----------------
#     query_clean = query.lower()
#     query_clean = query_clean.replace("kya hai","what is")
#     query_clean = query_clean.replace("ka matlab","meaning of")

#     # ---------------- RETRIEVAL (FIXED) ----------------
#     retriever = db.as_retriever(
#         search_type="mmr",
#         search_kwargs={"k": 2}
#     )

#     results = retriever.invoke(query_clean)   # ✅ FIXED

#     context = ""
#     sources = []

#     for doc in results:   # ✅ FIXED (no score unpacking)
#         context += doc.page_content + "\n\n"

#         sources.append(
#             f"{doc.metadata.get('source')} - Page {doc.metadata.get('page')}"
#         )

#     # ✅ FIXED context handling (outside loop)
#     if not context or context.strip() == "":
#         context = "Use general knowledge of Indian Labour Laws."

#     st.info(context)
#     # ---------------- PROMPT ----------------
#     prompt = f"""
# You are an expert assistant for Indian Labour Laws.

# RULES:
# - Answer the question directly and clearly.
# - Do NOT mention "context", "provided text", or "information given".
# - Do NOT say phrases like "according to the context".
# - Give a final, confident answer as if you already know it.
# - Keep the answer short, factual, and easy to understand.
# - If the answer is partial, still respond with the best possible complete answer.

# Language: {language}

# Question:
# {query}

# Answer:
# """

#     with st.chat_message("assistant"):

#         with st.spinner("Thinking..."):
#             response = ollama.chat(
#                 model="gemma:2b",
#                 messages=[{"role":"user","content":prompt}]
#             )

#         answer = response["message"]["content"]

#         # ---------------- STREAMING EFFECT ----------------
#         placeholder = st.empty()
#         full_text = ""

#         for word in answer.split():
#             full_text += word + " "
#             placeholder.markdown(full_text)
#             time.sleep(0.02)

#         placeholder.markdown(answer)
# import streamlit as st
# from langchain_community.vectorstores import FAISS
# from langchain_huggingface import HuggingFaceEmbeddings
# import ollama

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(page_title="Labour Law AI Assistant", layout="wide")

# # ---------------- HEADER ----------------
# st.logo("logos/labour_ai_logo.png", size="large")
# st.markdown("## 📘 Labour Law AI Assistant")
# st.caption("AI powered assistant for Indian Labour Law documents")

# # ---------------- POWERED BY ----------------
# col1, col2, col3 = st.columns([1,2,6])
# with col1:
#     st.markdown("**Powered by**")
# with col2:
#     st.image("logos/Wadhwani-Foundation-Logo.png", width=120)

# # ---------------- LANGUAGE ----------------
# if "language" not in st.session_state:
#     st.session_state.language = "Auto Detect"

# language = st.selectbox(
#     "Response Language",
#     ["Auto Detect","English","Hindi","Malayalam"],
#     index=["Auto Detect","English","Hindi","Malayalam"].index(st.session_state.language)
# )

# st.session_state.language = language

# # ---------------- CACHE EMBEDDINGS ----------------
# @st.cache_resource
# def load_embeddings():
#     return HuggingFaceEmbeddings(
#         model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
#     )

# embeddings = load_embeddings()

# # ---------------- CACHE VECTOR DB ----------------
# @st.cache_resource
# def load_db():
#     return FAISS.load_local(
#         "vectorstore",
#         embeddings,
#         allow_dangerous_deserialization=True
#     )

# db = load_db()

# # ---------------- MEMORY ----------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # ---------------- DISPLAY CHAT ----------------
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # ---------------- INPUT ----------------
# query = st.chat_input("Ask about Indian Labour Laws")

# if query:

#     st.session_state.messages.append({"role":"user","content":query})

#     with st.chat_message("user"):
#         st.markdown(query)

#     # ---------------- NORMALIZATION ----------------
#     query_clean = query.lower()\
#         .replace("kya hai","what is")\
#         .replace("ka matlab","meaning of")

#     # ---------------- RETRIEVER ----------------
#     retriever = db.as_retriever(
#         search_type="mmr",
#         search_kwargs={"k": 2}   # 🔥 reduced from 3 → faster
#     )

#     results = retriever.invoke(query_clean)

#     context = ""
#     for doc in results:
#         context += doc.page_content + "\n\n"

#     if not context.strip():
#         context = "Use general knowledge of Indian Labour Laws."

#     # ---------------- PROMPT ----------------
#     prompt = f"""
#      You are a strict FAQ assistant for Indian Labour Laws.

#      IMPORTANT RULES:
#     - The answer MUST be taken from the context below.
#     - Do NOT say "not available".
#     - Do NOT refuse.
#     - If answer exists, return it clearly.
#     - Even if answer is partially available, answer using best possible information.
#     - Keep answer short and factual.

#     Language: {language}

#     Context:
#     {context}

#     Question:
#     {query}

#     Answer:
#     """
#     # ---------------- MODEL ----------------
#     with st.chat_message("assistant"):
#         with st.spinner("Thinking..."):
#             response = ollama.chat(
#                 model="gemma:2b",
#                 messages=[{"role":"user","content":prompt}]
#             )

#         answer = response["message"]["content"]

#         # 🔥 FAST OUTPUT (no delay)
#         st.markdown(answer)

#     st.session_state.messages.append({"role":"assistant","content":answer})







import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import ollama
import time
import subprocess
import sys
import tempfile
import os
import sqlite3
from datetime import datetime
import pandas as pd


# ======================================================
#               LABOUR LAW ANALYTICS
# ======================================================

DB_NAME = "labour_analytics.db"


# ---------------- INITIALIZE SQLITE DATABASE ----------------

def init_analytics_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            topic TEXT NOT NULL,
            language TEXT NOT NULL,
            asked_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ---------------- CLASSIFY CUSTOMER QUESTIONS ----------------

def classify_labour_topic(question):

    q = question.lower()

    topic_keywords = {

        "Gratuity": [
            "gratuity",
            "retirement benefit",
            "15 days wages",
            "five years",
            "5 years"
        ],

        "Minimum Wages & Floor Wage": [
            "minimum wage",
            "minimum wages",
            "floor wage",
            "daily wage",
            "wage rate"
        ],

        "Wage Definition & 50% Rule": [
            "50%",
            "50 percent",
            "wages definition",
            "allowances",
            "basic pay",
            "dearness allowance"
        ],

        "Overtime": [
            "overtime",
            "extra hours",
            "working hours"
        ],

        "Bonus": [
            "bonus",
            "30 days",
            "accounting year"
        ],

        "Wage Deductions": [
            "deduction",
            "deductions",
            "salary cut"
        ],

        "Employee Coverage": [
            "temporary employee",
            "contractual",
            "part-time",
            "casual worker",
            "employee coverage",
            "unorganised"
        ],

        "Equality & Non-discrimination": [
            "transgender",
            "gender discrimination",
            "equal pay",
            "discrimination"
        ],

        "Inspector & Penalties": [
            "inspector",
            "penalty",
            "penalties",
            "punishment",
            "compounding"
        ],

        "Transition Rules": [
            "transition",
            "old rules",
            "new rules"
        ],

        "Leave Encashment": [
            "leave encashment",
            "unused leave"
        ]
    }

    for topic, keywords in topic_keywords.items():

        if any(keyword in q for keyword in keywords):
            return topic

    return "Other"


# ---------------- SAVE CUSTOMER QUESTION ----------------

def save_customer_query(question, language):

    topic = classify_labour_topic(question)

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customer_queries
        (question, topic, language, asked_at)
        VALUES (?, ?, ?, ?)
    """, (
        question,
        topic,
        language,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


# ---------------- SHOW ANALYTICS DASHBOARD ----------------

def show_labour_analytics():

    st.header("📊 Labour Law Analytics")

    st.caption(
        "Explore FAQ document coverage and actual questions "
        "submitted to the Labour Law Assistant."
    )

    # ------------------------------------------
    # FAQ DOCUMENT ANALYSIS
    # ------------------------------------------

    faq_coverage = {

        "Gratuity": 4,

        "Minimum Wages & Floor Wage": 3,

        "Wage Definition & 50% Rule": 4,

        "Bonus": 2,

        "Employee Coverage": 2,

        "Overtime": 1,

        "Wage Deductions": 1,

        "Equality & Non-discrimination": 1,

        "Inspector & Penalties": 1,

        "Transition Rules": 1,

        "Leave Encashment": 1,

        "Other Labour Code FAQs": 2
    }

    st.subheader("1. FAQ Document Analysis")

    st.caption(
        "Number of FAQ entries assigned to each topic in your uploaded PDFs. "
        "These are document coverage counts, not real-world popularity statistics."
    )

    faq_df = pd.DataFrame({

        "Topic": list(faq_coverage.keys()),

        "FAQ Count": list(faq_coverage.values())

    }).sort_values("FAQ Count", ascending=False)

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "FAQ entries analysed",
            int(faq_df["FAQ Count"].sum())
        )

    with col2:

        st.metric(
            "Topics identified",
            len(faq_df)
        )

    st.markdown("### FAQ Topic Distribution")

    st.bar_chart(
        faq_df.set_index("Topic"),
        y="FAQ Count",
        horizontal=True
    )

    st.divider()

    # ------------------------------------------
    # CUSTOMER QUERY ANALYSIS
    # ------------------------------------------

    st.subheader("2. Customer Query Analysis")

    conn = sqlite3.connect(DB_NAME)

    query_df = pd.read_sql_query(
        "SELECT * FROM customer_queries ORDER BY asked_at DESC",
        conn
    )

    conn.close()

    if query_df.empty:

        st.info(
            "No customer questions have been recorded yet. "
            "Ask questions through the chatbot to start building real analytics."
        )

        return

    # ------------------------------------------
    # KEY PERFORMANCE INDICATORS
    # ------------------------------------------

    total_queries = len(query_df)

    unique_topics = query_df["topic"].nunique()

    most_common_topic = query_df["topic"].value_counts().idxmax()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Questions",
        total_queries
    )

    col2.metric(
        "Topics Asked About",
        unique_topics
    )

    col3.metric(
        "Most Asked Topic",
        most_common_topic
    )

    st.divider()

    # ------------------------------------------
    # FREQUENTLY ASKED TOPICS
    # ------------------------------------------

    st.markdown("### 3. Most Frequently Asked Topics")

    topic_counts = (
        query_df["topic"]
        .value_counts()
        .reset_index()
    )

    topic_counts.columns = [
        "Topic",
        "Questions"
    ]

    st.bar_chart(
        topic_counts.set_index("Topic"),
        y="Questions",
        horizontal=True
    )

    # ------------------------------------------
    # LANGUAGE DISTRIBUTION
    # ------------------------------------------

    st.markdown("### 4. Language Distribution")

    language_counts = (
        query_df["language"]
        .value_counts()
        .reset_index()
    )

    language_counts.columns = [
        "Language",
        "Questions"
    ]

    st.bar_chart(
        language_counts.set_index("Language"),
        y="Questions"
    )

    # ------------------------------------------
    # RECENT CUSTOMER QUESTIONS
    # ------------------------------------------

    st.markdown("### 5. Recent Customer Questions")

    st.dataframe(
        query_df[
            ["asked_at", "question", "topic", "language"]
        ],
        use_container_width=True,
        hide_index=True
    )

    # ------------------------------------------
    # DOWNLOAD ANALYTICS
    # ------------------------------------------

    csv_data = query_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "⬇️ Download Analytics CSV",
        data=csv_data,
        file_name="labour_law_analytics.csv",
        mime="text/csv"
    )

    # ------------------------------------------
    # CLEAR ANALYTICS
    # ------------------------------------------

    if st.button("Clear Customer Analytics Data"):

        conn = sqlite3.connect(DB_NAME)

        conn.execute(
            "DELETE FROM customer_queries"
        )

        conn.commit()
        conn.close()

        st.success(
            "Customer analytics data cleared."
        )

        st.rerun()


# ---------------- CREATE DATABASE ----------------

init_analytics_db()


# ======================================================
#                   PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Labour Law AI Assistant",
    layout="wide"
)


# ======================================================
#                       HEADER
# ======================================================

st.logo(
    "logos/labour_ai_logo.png",
    size="large"
)

st.markdown("## 📘 Labour Law AI Assistant")

st.caption(
    "AI powered assistant for Indian Labour Law documents"
)


# ---------------- POWERED BY SECTION ----------------

col1, col2, col3 = st.columns([.5, .3, 6])

with col1:

    st.markdown("Powered by")

with col2:

    st.image(
        "logos/Wadhwani-Foundation-Logo.png",
        width=120
    )


# ======================================================
#                  LANGUAGE SELECT
# ======================================================

if "language" not in st.session_state:

    st.session_state.language = "Auto Detect"


language = st.selectbox(

    "Response Language",

    [
        "Auto Detect",
        "English",
        "Hindi",
        "Malayalam"
    ],

    index=[
        "Auto Detect",
        "English",
        "Hindi",
        "Malayalam"
    ].index(st.session_state.language)
)

st.session_state.language = language


# ======================================================
#                  LOAD EMBEDDINGS
# ======================================================

embeddings = HuggingFaceEmbeddings(

    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

)


# ======================================================
#                  LOAD VECTOR DATABASE
# ======================================================

db = FAISS.load_local(

    "vectorstore",

    embeddings,

    allow_dangerous_deserialization=True

)


# ======================================================
#                  LANGUAGE DETECTION
# ======================================================

def detect_language(text):

    # Malayalam

    if any('\u0D00' <= ch <= '\u0D7F' for ch in text):

        return "Malayalam"

    # Hindi

    if any('\u0900' <= ch <= '\u097F' for ch in text):

        return "Hindi"

    # Default English

    return "English"


# ======================================================
#                  PIPER VOICE GENERATION
# ======================================================

def generate_audio(text, language):

    voice_models = {

        "English": "en_US-lessac-medium",

        "Hindi": "hi_IN-pratham-medium",

        "Malayalam": "ml_IN-arjun-medium"

    }

    model = voice_models[language]

    temp_file = tempfile.NamedTemporaryFile(

        suffix=".wav",

        delete=False

    )

    audio_path = temp_file.name

    temp_file.close()

    try:

        subprocess.run(

            [
                sys.executable,
                "-m",
                "piper",
                "-m",
                model,
                "-f",
                audio_path,
                "--",
                text
            ],

            check=True,

            capture_output=True,

            text=True

        )

        with open(audio_path, "rb") as audio_file:

            audio_bytes = audio_file.read()

        return audio_bytes

    finally:

        if os.path.exists(audio_path):

            os.remove(audio_path)


# ======================================================
#                       MEMORY
# ======================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ======================================================
#                 SUGGESTED QUESTIONS
# ======================================================

suggested_questions = [

    "What are wages?",

    "What is floor wage?",

    "How is overtime calculated?",

    "When is gratuity payable?",

    "What is the 50% wage rule?",

    "Who is eligible for bonus?",

    "Can employers deduct more than 50% of wages?",

    "Are temporary employees covered?"

]


# ---------------- STORE CLICKED QUESTION ----------------

if "pending_query" not in st.session_state:

    st.session_state.pending_query = None


# ======================================================
#                 DISPLAY CHAT HISTORY
# ======================================================

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])


# ======================================================
#              WELCOME AND SUGGESTED QUESTIONS
# ======================================================

if True:

    st.markdown("### 👋 Welcome!")

    st.markdown(
        "How can I help you with Indian Labour Laws today? "
        "Choose a question below or type your own question."
    )

    st.markdown("#### Frequently asked questions")

    # ---------------- FIRST ROW ----------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(

            "💰 What are wages?",

            use_container_width=True,

            key="suggest_1"

        ):

            st.session_state.pending_query = suggested_questions[0]

            st.rerun()

    with col2:

        if st.button(

            "🏛️ What is floor wage?",

            use_container_width=True,

            key="suggest_2"

        ):

            st.session_state.pending_query = suggested_questions[1]

            st.rerun()


    # ---------------- SECOND ROW ----------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(

            "⏰ How is overtime calculated?",

            use_container_width=True,

            key="suggest_3"

        ):

            st.session_state.pending_query = suggested_questions[2]

            st.rerun()

    with col2:

        if st.button(

            "📅 When is gratuity payable?",

            use_container_width=True,

            key="suggest_4"

        ):

            st.session_state.pending_query = suggested_questions[3]

            st.rerun()


    # ---------------- THIRD ROW ----------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(

            "📊 What is the 50% wage rule?",

            use_container_width=True,

            key="suggest_5"

        ):

            st.session_state.pending_query = suggested_questions[4]

            st.rerun()

    with col2:

        if st.button(

            "👥 Who is eligible for bonus?",

            use_container_width=True,

            key="suggest_6"

        ):

            st.session_state.pending_query = suggested_questions[5]

            st.rerun()


    # ---------------- FOURTH ROW ----------------

    col1, col2 = st.columns(2)

    with col1:

        if st.button(

            "➖ Can employers deduct more than 50% of wages?",

            use_container_width=True,

            key="suggest_7"

        ):

            st.session_state.pending_query = suggested_questions[6]

            st.rerun()

    with col2:

        if st.button(

            "📄 Are temporary employees covered?",

            use_container_width=True,

            key="suggest_8"

        ):

            st.session_state.pending_query = suggested_questions[7]

            st.rerun()


# ======================================================
#                    USER INPUT
# ======================================================

user_input = st.chat_input(
    "Ask about Indian Labour Laws"
)


# ---------------- CHECK SUGGESTED QUESTION ----------------

if st.session_state.pending_query is not None:

    query = st.session_state.pending_query

    st.session_state.pending_query = None

else:

    query = user_input


# ======================================================
#                  PROCESS USER QUERY
# ======================================================

if query:

    # ---------------- STORE USER MESSAGE ----------------

    st.session_state.messages.append({

        "role": "user",

        "content": query

    })

    with st.chat_message("user"):

        st.markdown(query)


    # ---------------- SELECT RESPONSE LANGUAGE ----------------

    if language == "Auto Detect":

        response_language = detect_language(query)

    else:

        response_language = language


    # ---------------- SAVE QUESTION FOR ANALYTICS ----------------

    save_customer_query(
        query,
        response_language
    )


    # ==================================================
    #               LANGUAGE INSTRUCTIONS
    # ==================================================

    language_instructions = {

        "English": """

        Answer ONLY in English.

        Use clear and simple English.

        """,

        "Hindi": """

        Answer ONLY in Hindi.

        Use Devanagari script.

        Do not answer in Malayalam or English.

        """,

        "Malayalam": """

        Answer ONLY in Malayalam.

        Use Malayalam script for the entire answer.

        Do NOT answer in Hindi.

        Do NOT use Devanagari script.

        Do NOT answer in English.

        Translate the relevant labour law information into natural Malayalam.

        """

    }


    # ==================================================
    #              HINGLISH NORMALIZATION
    # ==================================================

    query_clean = query.lower()

    query_clean = query_clean.replace(
        "kya hai",
        "what is"
    )

    query_clean = query_clean.replace(
        "ka matlab",
        "meaning of"
    )


    # ==================================================
    #                     RETRIEVAL
    # ==================================================

    retriever = db.as_retriever(

        search_type="mmr",

        search_kwargs={"k": 2}

    )

    results = retriever.invoke(query_clean)

    context = ""

    for doc in results:

        context += doc.page_content + "\n\n"

    if not context.strip():

        context = "No relevant information found in the uploaded documents."

    st.info(context)


    # ==================================================
    #                       PROMPT
    # ==================================================

    prompt = f"""

You are an expert assistant for Indian Labour Laws.

IMPORTANT LANGUAGE INSTRUCTIONS:

{language_instructions[response_language]}

STRICT RULES:

- Answer the exact question asked by the user.
- Use ONLY the labour law information provided below.
- Do NOT use outside knowledge.
- Do NOT invent facts, figures or legal provisions.
- Do NOT change the meaning of the source information.
- Keep the answer short and factual.
- Use simple language understandable to ordinary people.
- Do not include unnecessary introductions.
- Do not mix two languages.
- The complete answer must be in {response_language}.

LABOUR LAW INFORMATION:

{context}

USER QUESTION:

{query}

Write the final answer only in {response_language}.

"""


    # ==================================================
    #                    BUILD MEMORY
    # ==================================================

    chat_history = [

        {

            "role": "system",

            "content": f"""

You are a specialised Indian Labour Law Assistant.

Your current response language is {response_language}.

STRICT LANGUAGE RULE:

{language_instructions[response_language]}

Always follow this language instruction,
even if previous conversation messages use another language.

Never copy the language of previous answers
when it conflicts with the current response language.

"""

        }

    ]

    previous_messages = st.session_state.messages[:-1]

    for msg in previous_messages[-4:]:

        chat_history.append({

            "role": msg["role"],

            "content": msg["content"]

        })


    chat_history.append({

        "role": "user",

        "content": prompt

    })


    # ==================================================
    #                       MODEL
    # ==================================================

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = ollama.chat(

                model="gemma:2b",

                messages=chat_history

            )

        answer = response["message"]["content"].strip()


        # ---------------- STREAMING EFFECT ----------------

        placeholder = st.empty()

        full_text = ""

        for word in answer.split():

            full_text += word + " "

            placeholder.markdown(full_text)

            time.sleep(0.02)

        placeholder.markdown(answer)


        # ---------------- PIPER VOICE OUTPUT ----------------

        st.markdown("**🔊 Listen to answer**")

        try:

            audio_bytes = generate_audio(

                answer,

                response_language

            )

            st.audio(

                audio_bytes,

                format="audio/wav"

            )

        except Exception as e:

            st.warning(
                f"Audio generation failed: {e}"
            )


    # ---------------- STORE ASSISTANT RESPONSE ----------------

    st.session_state.messages.append({

        "role": "assistant",

        "content": answer

    })


# ======================================================
#              DISPLAY LABOUR LAW ANALYTICS
# ======================================================

with st.expander(
    "📊 Open Labour Law Analytics Dashboard",
    expanded=False
):

    show_labour_analytics()
