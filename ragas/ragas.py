import openai
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI

# Reading the file and splitting them
pdf_reader = PyPDFLoader("your_pdf_path/Power+BI+Ebook.pdf")
documents = pdf_reader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200,)
chunks = text_splitter.split_documents(documents)


# Create embeddings
embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
db = FAISS.from_documents(documents=chunks, embedding=embeddings)


llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="sk-or-v1-e1b264341b9546a557fb085cd8d45bd5f8f50dfs2ecc4355630040282b41a12d2d7",
    model_name="deepseek/deepseek-chat"
)

# sets up a conversational retrieval chain using LangChain
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_core.prompts.prompt import PromptTemplate

CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template("""Given the following conversation and a follow up question, rephrase the follow up question to be a standalone question.

Chat History:
{chat_history}
Follow up Input: {question}
Standalon question:""")

qa = ConversationalRetrievalChain.from_llm(llm=llm,
                                           retriever=db.as_retriever(),
                                           condense_question_prompt=CONDENSE_QUESTION_PROMPT,
                                           return_source_documents=True,
                                           verbose=False
                                           )


# chat_history=[]
# query = """?What are the components of Power BI?"""
# result = qa({"question": query, "chat_history": chat_history})
# print(result['answer'])


# RAG Evaluation

sample_queries = [
    {
        "question": "What are the main components of Power BI?",
        "answer": "The main components of Power BI are Power BI Desktop, Power BI Service, and Power BI Mobile.",
        "reference": "Power BI has three main components: Desktop (Windows app for creating reports), Service (cloud platform for sharing and collaboration), and Mobile (app for viewing reports on mobile devices)."
    },
    {
        "question": "What are the key features of Power BI Desktop?",
        "answer": "Key features include data connection and transformation, data modeling, interactive visualizations, report publishing, and collaboration tools.",
        "reference": "Power BI Desktop allows users to get data, analyze it with DAX, visualize using 150+ visuals, publish to cloud or on-premises, and collaborate with team members."
    },
    {
        "question": "How does Power BI integrate with Excel?",
        "answer": "Power BI can analyze data in Excel, import Excel data, connect to Excel workbooks, and pin Excel ranges to dashboards.",
        "reference": "Power BI integrates with Excel by enabling analysis in Excel, data import, connection to workbooks, and uploading Excel files for dashboard pinning."
    },
    {
        "question": "What is the Power Query Editor used for?",
        "answer": "Power Query Editor is used for data transformation and cleansing before importing data into models or visualizations.",
        "reference": "Power Query Editor includes tools like ribbon tabs, data preview, query settings, and footer with data stats for transforming and shaping data."
    },
    {
        "question": "How can you group data in Power BI?",
        "answer": "You can group data using the 'Group By' feature in the Transform tab of the Query Editor by selecting columns and specifying aggregate calculations.",
        "reference": "In Power BI's Query Editor, the Group By dialog allows users to select columns and apply aggregate functions to group data."
    }
]

import pandas as pd

df = pd.DataFrame(sample_queries)



def process_query(query):
  chat_history = []
  result = qa({"question": query, "chat_history": chat_history})
  retriever = db.as_retriever()
  relevant_docs = retriever.invoke(query)
  print(result['answer'])
  return result['answer'], relevant_docs

# process_query("What is the Power Query Editor used for?")

# RAGAS Framework

results = []

for _, row in df.iterrows():
  question = row['question']
  ground_truth = row['answer']

  answer, relevant_docs = process_query(question)

  results.append({
      "user_input": question,
      "reference": ground_truth,
      "response": answer,
      "retrieved_contexts": [relevant_docs[0].page_content]
  })


from ragas import EvaluationDataset
from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.metrics import LLMContextRecall, Faithfulness, FactualCorrectness

evaluation_dataset = EvaluationDataset.from_list(results)

evaluator_llm = LangchainLLMWrapper(llm)

ragas_result = evaluate(
    dataset=evaluation_dataset,
    metrics=[LLMContextRecall(), Faithfulness(), FactualCorrectness()],
    llm = evaluator_llm
)

print(ragas_result)
