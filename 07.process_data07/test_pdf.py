from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("openManus.pdf")
pages = loader.load_and_split()
for page in pages:
    print (page)