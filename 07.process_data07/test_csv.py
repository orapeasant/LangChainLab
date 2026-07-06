import os
from pathlib import Path

from langchain.document_loaders import UnstructuredCSVLoader
from langchain.document_loaders.csv_loader import CSVLoader
 
file_path = "身高体重表.csv"

 

def test_csv_loader():
    loader = CSVLoader(file_path,csv_args={'delimiter': ','},encoding="utf-8")
    docs = loader.load()
    for doc in docs:
        print (doc)

 
test_csv_loader()