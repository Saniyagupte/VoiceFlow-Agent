


# handlers/summarize_file.py

import os
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

class SummarizeFileHandler:
    def __init__(self, task):
        self.task = task

    def run(self):
        file_path = self.task.get("file_path")
        if not file_path or not os.path.exists(file_path):
            print("❌ File not found or not provided.")
            return

        print(f"📄 Summarizing file: {file_path}")

        # Load and split
        loader = PyPDFLoader(file_path)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        splits = splitter.split_documents(docs)

        # Embeddings + Vector store
        embeddings = OpenAIEmbeddings()
        vectordb = FAISS.from_documents(splits, embeddings)

        # Chain
        llm = OpenAI(temperature=0)
        chain = load_qa_chain(llm, chain_type="stuff")

        question = "Please summarize this document in 5 bullet points"
        result = chain.run(input_documents=splits, question=question)

        print("✅ Summary:")
        print(result)
        return result






