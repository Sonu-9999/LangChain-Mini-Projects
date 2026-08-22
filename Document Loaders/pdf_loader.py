from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader("Document Loaders/Debarghya_Mukherjee_Resume.pdf")

docs= loader.load()


print(len(docs))

print(docs[0].page_content)