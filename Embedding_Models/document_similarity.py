from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embedding= HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L12-v2")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query= "Tell me about Bumrah"

doc_embeddings= embedding.embed_documents(documents)
query_embedding= embedding.embed_query(query)
scores=cosine_similarity([query_embedding],doc_embeddings)[0]  #both of them should be 2d vector 
index,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1] #sort on the basis of score and get the last one which is the highest score with index

print(query)
print(documents[index])
print("similarity score is:",score)