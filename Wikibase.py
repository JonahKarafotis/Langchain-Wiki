

#load relevent data
from langchain_community.document_loaders.wikipedia import WikipediaLoader
docs = WikipediaLoader(query=input("Subject: "), load_max_docs=2).load()

#Split
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
all_splits = text_splitter.split_documents(docs)

#Store splits
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())



# LLM
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

# RetrievalQA
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant and you will be given only information that hass been written on the website. Please respond to the user's questions about the given website only based on the given context."),
    ("user", "Question: {question}\nContext: {context}")
])

output_parser = StrOutputParser()
question = input('What would you like to know about your website?  ')
context = vectorstore.similarity_search(question,k=3)


chain = prompt | llm | output_parser
chain.invoke({"question": question, "context": context})

