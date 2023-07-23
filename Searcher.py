from whoosh.qparser import QueryParser
from whoosh import index
#import sys

ix = index.open_dir("index")
# searcher = ix.searcher() # should be from extractPDFFile.py file 


with ix.searcher() as searcher:
    # query = input("Enter your search query: ")
    query = 'SAP'
    qp = QueryParser("content", ix.schema)
    q = qp.parse(query)
    results= searcher.search(q,limit=None)
    #results = searcher.search(q)
    # print the results
    print("Number of results:", len(results))
    for hit in results:
        print("----------------------------")
        print(hit["file_name"])
        print(hit.highlights("content"))
        print(hit["phone"])
        print(hit["email"])
        print("----------------------------")