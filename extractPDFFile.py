import os
import PyPDF2
#import docx 
from whoosh.fields import SchemaClass, TEXT, ID
from whoosh.index import create_in, open_dir 


# create Schema class for the file name and text 
class IndexFile(SchemaClass):
    file_name = ID(stored=True)
    content = TEXT()


# function to extract from PDF file    
def ExtractPDFFile(i):
    
     pdffile = open(i, "rb")

 # Extract information from PDF file
     pdf_reader = PyPDF2.PdfReader(pdffile)
     pdf_text = ""
     for page in pdf_reader.pages:
        pdf_text += page.extract_text()

     pdffile.close()
    #print(pdf_text)
     return pdf_text

# Function to extract from Docx file
# def ExtractDocxFile(j):
#     docxfile = docx.Document()
#     docx_text = ""
#     for para in docxfile.paragraphs:
#         docx_text += para.text
#     # if info_type in docx_text:
#     #         print("The information is present in example.docx")
#     return docx_text



# Set the directory path
dir_path = "CVs//"
files = os.listdir(dir_path) # Get a list of all files in the directory
pdf_files = [] # Initialize empty lists for PDF file 
docx_files = [] #  Initialize empty lists for docx file
for file in files:  # Loop through the list of files and append PDF and DOCX files to their respective lists
    if file.endswith(".pdf"):
        pdf_files.append(os.path.join(dir_path, file))
    elif file.endswith(".docx"):
        docx_files.append(os.path.join(dir_path, file))


# print("PDF files:")
# print(pdf_files)

# if index file not exists will be created 
if not os.path.exists("index"):
   os.mkdir("index")
 
ix = create_in("index", schema= IndexFile)
ix = open_dir("index") # open index
writer = ix.writer()

for i in pdf_files:
   ExtractPDFFile(i)
   writer.add_document(file_name= i, content= ExtractPDFFile(i))


# for j in docx_files:
#       ExtractDocxFile(j)
#       writer.add_document(file_name= j, content=    ExtractDocxFile(j))

writer.commit()
