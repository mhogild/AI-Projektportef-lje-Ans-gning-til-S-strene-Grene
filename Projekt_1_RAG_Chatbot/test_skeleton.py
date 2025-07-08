import os
import re
import pandas as pd
from io import StringIO
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Set API key
os.environ["OPENAI_API_KEY"] = "XX" #Skjult - Du skal være velkommen til at spørge efter API hvis du gerne vil teste den :)

# === 1. Load markdown content ===
with open("Projekt_1_RAG_Chatbot/test_pdf/test_carlsberg_key_figures.md", "r", encoding="utf-8") as file:
    md_text = file.read()

# === 2. Find alle markdown-tabeller ===
table_pattern = r"((?:\|.+?\|\n)+)"
tables = re.findall(table_pattern, md_text)

# === 3. Konverter tabeller til pandas DataFrames og lav documents ===
table_docs = []
for idx, table_md in enumerate(tables):
    try:
        df = pd.read_table(StringIO(table_md), sep="|", engine="python")
        df_clean = df.dropna(axis=1, how="all").dropna(axis=0, how="all")
        table_text = df_clean.to_string(index=False)
        table_docs.append(Document(page_content=table_text, metadata={"source": f"table_{idx}"}))
    except Exception as e:
        print(f"⚠️ Kunne ikke parse tabel {idx}: {e}")

# === 4. Split resterende tekst ===
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
text_docs = text_splitter.create_documents([md_text])

# === 5. Kombinér tekst og tabeller ===
all_docs = text_docs + table_docs

# === 6. Embed og gem i Chroma ===
embedding = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(all_docs, embedding, persist_directory="./Projekt_1_RAG_Chatbot/chroma_test")
vectorstore.persist()

print("✅ Embedding færdig. Klar til spørgsmål!")
