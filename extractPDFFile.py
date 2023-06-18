import os
import PyPDF2

def FileOpen(i):
    

     pdffile = open(i, "rb")
# Extract information from PDF file
     pdf_reader = PyPDF2.PdfReader(pdffile)
     pdf_text = ""
     for page in pdf_reader.pages:
        pdf_text += page.extract_text()

     pdffile.close()
    #print(pdf_text)
     return pdf_text




# Set the directory path
dir_path = "CVs//"
files = os.listdir(dir_path) # Get a list of all files in the directory

pdf_files = [] # Initialize empty lists for PDF 

for file in files:  # Loop through the list of files and append PDF and DOCX files to their respective lists
    if file.endswith(".pdf"):
        pdf_files.append(os.path.join(dir_path, file))

print("PDF files:")
print(pdf_files)

# Open the PDF and DOCX files

for i in pdf_files:
   FileOpen(i)
