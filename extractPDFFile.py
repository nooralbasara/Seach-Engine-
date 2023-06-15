import os
import docx
import PyPDF2

# Set the directory path
dir_path = "CVs//"

# Get a list of all files in the directory
files = os.listdir(dir_path)

# Initialize empty lists for PDF and DOCX files
pdf_files = []
docx_files = []

# Loop through the list of files and append PDF and DOCX files to their respective lists
for file in files:
    if file.endswith(".pdf"):
        pdf_files.append(os.path.join(dir_path, file))
    elif file.endswith(".docx"):
        docx_files.append(os.path.join(dir_path, file))

# Print the lists of PDF and DOCX files
print("PDF files:")
print(pdf_files)
print("DOCX files:")
print(docx_files)

# Take user input for information to extract
info_type = input("Enter the  features you want to extract: ")

# Open the PDF and DOCX files
pdffile = open("pdf_files", mode="rb")
docxfile = docx.Document("docx_files")

# Extract information from PDF file
pdf_reader = PyPDF2.PdfFileReader(pdffile)
pdf_text = ""
for page_num in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page_num)
    pdf_text += page.extractText()
if info_type in pdf_text:
    print("The information is present in pdf_files")

# Extract information from DOCX file
docx_text = ""
for para in docxfile.paragraphs:
    docx_text += para.text
if info_type in docx_text:
    print("The information is present in docx_files")

pdffile.close()


