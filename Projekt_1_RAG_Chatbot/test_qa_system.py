from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import os

# 🔐 Sæt din OpenAI API-nøgle (du må gerne sætte denne via miljøvariabel i stedet)
os.environ["OPENAI_API_KEY"] = "XX" #Skjult - Du skal være velkommen til at spørge efter API hvis du gerne vil teste den :)

# 1. Load gemte embeddings fra Chroma
vectorstore = Chroma(
    persist_directory="./chroma_test1",
    embedding_function=OpenAIEmbeddings()
)

# 2. Retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 3. GPT-model og kæde
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# 4. Chat loop
while True:
    query = input("\n🔍 Stil et spørgsmål om årsrapporten (eller skriv 'exit'): ")
    if query.lower() in ["exit", "quit"]:
        break

    result = qa.invoke(query)
    print("\n💬 Svar:\n", result['result'])

    print("\n📄 Kilder:")
    for doc in result['source_documents']:
        print(f" - {doc.metadata.get('source')} | ...{doc.page_content[:100]}...\n")
