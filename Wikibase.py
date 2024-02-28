from langchain_community.document_loaders.wikipedia import WikipediaLoader
docs = WikipediaLoader(query=input("Subject: "), load_max_docs=2).load()
"""
    Loads Wikipedia documents based on user input.

    This function prompts the user for a subject to search on Wikipedia,
    loads up to 2 documents related to the subject, and returns them.

    Returns:
        docs: A list of loaded Wikipedia documents.
    """
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(docs)
"""
    Splits the loaded documents into chunks.

    Takes a list of documents and splits them into chunks of 500 characters
    with no overlap between chunks.

    Args:
        docs: A list of documents to be split.

    Returns:
        all_splits: A list of split document chunks.
    """
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())
"""
    Stores the split documents in a vector store.

    Takes the list of split documents and stores them in a Chroma vector store
    using OpenAI embeddings.

    Args:
        all_splits: A list of split document chunks.

    Returns:
        vectorstore: A Chroma vector store containing the split documents.
    """
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
"""
    Initializes the language model for generating responses.

    This function sets up the GPT-3.5-turbo model with a temperature of 0 for
    deterministic responses.

    Returns:
        llm: A ChatOpenAI instance configured for generating responses.
    """
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant and you will be given only information that has been written on the website. Please respond to the user's questions about the given website only based on the given context."),
    ("user", "Question: {question}\nContext: {context}")
])
output_parser = StrOutputParser()
"""
    Sets up the prompt for the chat model and the output parser.

    This function prepares a prompt template for the chat model and an output
    parser to process the responses.

    Returns:
        prompt: A ChatPromptTemplate instance for generating prompts.
        output_parser: A StrOutputParser instance for parsing responses.
    """
question = input('What would you like to know about this subject? ')
context = vectorstore.similarity_search(question, k=3)
chain = prompt | llm | output_parser
chain.invoke({"question": question, "context": context})
"""
    Invokes the chat model with a user's question and context.

    This function takes a user's question, performs a similarity search to find
    relevant context using the vector store, and then invokes the chat model to
    generate a response based on the prompt and context.
"""
