from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
import os
import re

print("📂 Loading PDFs...")

chunks = []

# ---------------- PROCESS FILES ----------------
for file in os.listdir("data"):
    if file.endswith(".pdf"):
        print(f"Processing {file}")

        loader = PyPDFLoader(f"data/{file}")
        pages = loader.load()

        full_text = ""

        for page in pages:
            page.metadata["source"] = file
            full_text += "\n" + page.page_content.strip()

        # ---------------- AUTO Q&A EXTRACTION ----------------

        # Normalize text
        text = re.sub(r"\s+", " ", full_text)

        # Split into sentences
        sentences = re.split(r"(?<=[?.])\s+", text)

        current_q = ""
        current_a = ""

        for sent in sentences:

            # Detect question
            if "?" in sent or sent.lower().startswith(("what", "whether", "is", "are", "how", "does")):

                # Save previous Q&A
                if current_q and current_a:
                    chunks.append(Document(
                        page_content=current_q.strip() + "\n" + current_a.strip(),
                        metadata={"source": file}
                    ))

                current_q = sent
                current_a = ""

            else:
                current_a += " " + sent

        # Save last pair
        if current_q and current_a:
            chunks.append(Document(
                page_content=current_q.strip() + "\n" + current_a.strip(),
                metadata={"source": file}
            ))

print(f"✅ Total chunks created: {len(chunks)}")

# ---------------- EMBEDDINGS ----------------
print("🧠 Creating embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# ---------------- VECTOR STORE ----------------
print("💾 Creating FAISS vector database...")

db = FAISS.from_documents(chunks, embeddings)

db.save_local("vectorstore")

print("✅ Vector DB Created Successfully!")