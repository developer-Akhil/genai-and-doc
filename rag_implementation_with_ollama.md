**How to implement RAG using Ollama?**

The code below demonstrates asking general questions and implementing a Retrieval-Augmented Generation (RAG) pipeline using Ollama with the TinyLLaMA model, while leveraging Hugging Face embeddings for vectorization.

*Hugging Face embeddings are numerical vector representations of data such as words, sentences or images generated using pre trained models available on the Hugging Face platform.*

```
# Importing Libraries
from langchain_community.llms import Ollama
import openai
from langchain_community.vectorstores import FAISS
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_core.prompts import PromptTemplate

# Initialize the model
# llm = Ollama(model='tinyllama')

# # Generate answers to a question
# question = "What is population of India ?"
# response = llm.invoke(question)
# print(response)

# # Send question
# question = "Who is Narendra Modi?"
# response = llm.invoke(question)
# print(response)
#

# Read pdf files
pdf_reader = PyPDFLoader("RAGPaper.pdf")
documents = pdf_reader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200,)
chunks = text_splitter.split_documents(documents)

# Create embeddings using a free Hugging Face model
embeddings = HuggingFaceEmbeddings()
db = FAISS.from_documents(documents=chunks, embedding=embeddings)

# Initialize the model
llm = Ollama(model='tinyllama')

CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template("""Given the following conversation and a follow question, rephrase the follow up question to be a standalone question.
                                                        Chat History:{chat_history}
                                                        Follow up Input: {question}
                                                        Standalone question:""")
qa = ConversationalRetrievalChain.from_llm(llm=llm, retriever=db.as_retriever(), condense_question_prompt=CONDENSE_QUESTION_PROMPT, return_source_documents=True,
                                           verbose=False)

chat_history=[]
query="""what is a RAG-sequence model?"""
result = qa({"question":query, "chat_history":chat_history})


print(result['answer'])

```
