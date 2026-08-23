from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv # Load environment variables from .env file


load_dotenv()  # Load environment variables from .env file

model=ChatGoogleGenerativeAI(model="gemini-3.6-flash")

video_id="OzjF2-e0fp0"
try:
    ytt_api = YouTubeTranscriptApi()
    transcript_list = ytt_api.fetch(video_id,languages=["en"])
    #convert to plain text
    transcript=" ".join(chunk.text for chunk in transcript_list)

except TranscriptsDisabled:
    print("No captions available for this video")

#use text splitter to split the document into chunks
splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks=splitter.create_documents([transcript])


#generate embeddings and store in chromadb
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)
vector_store=Chroma.from_documents(chunks,embeddings)

#retrieval
retriever=vector_store.as_retriever(search_type="similarity",search_kwargs={"k":4})

#augmentation
prompt = PromptTemplate(
    template="""
      You are a helpful assistant.
      Answer ONLY from the provided transcript context.
      If the context is insufficient, just say you don't know.

      {context}
      Question: {question}
    """,
    input_variables = ['context', 'question']
)
question = "what is google deepmind"
retrieved_docs = retriever.invoke(question)
context_text="\n\n".join(doc.page_content for doc in retrieved_docs)

final_prompt=prompt.invoke({"context":context_text,"question":question})

answer=model.invoke(final_prompt)
print(answer.text)