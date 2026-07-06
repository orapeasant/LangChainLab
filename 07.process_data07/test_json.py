import json
from pathlib import Path
from pprint import pprint

from langchain.document_loaders import JSONLoader
loader = JSONLoader(file_path='facebook_chat.json',jq_schema='.messages[].content' )
data = loader.load()
 
for s in data:
    print (s.page_content)
    #print (s.'page_content')
 