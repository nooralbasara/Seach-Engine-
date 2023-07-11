from whoosh.qparser import QueryParser
from whoosh import index
#import sys

ix = index.open_dir("index")
# searcher = ix.searcher() # should be from extractPDFFile.py file 


with ix.searcher() as searcher:
    # query = input("Enter your search query: ")
    query = 'noor'
    qp = QueryParser("content", ix.schema)
    q = qp.parse(query)
    results = searcher.search(q)
    # print the results
    print("Number of results:", len(results))
    for hit in results:
        print(hit["file_name"])
        print(hit.highlights("content"))