import os
import PyPDF2
import docx 
from whoosh.fields import SchemaClass, TEXT, ID
from whoosh.index import create_in, open_dir 

import re 

# create Schema class for the file name and text 
class IndexFile(SchemaClass):
    file_name = ID(stored=True)
    content = TEXT(stored=True)
    phone = TEXT(stored=True)
    email = TEXT(stored=True)
    hash_value = TEXT(stored=True)


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
def ExtractDocxFile(j):
    docxfile = docx.Document(j)
    docx_text = ""
    for para in docxfile.paragraphs:
        docx_text += para.text
    # if info_type in docx_text:
#     #         print("The information is present in example.docx")
    return docx_text

def ExtractNumbewr(text):
    phone_numbers = set()

    _lines =  text.split("\n")
    
    # Use regular expressions to find phone numbers
    phone_regex = re.compile(r'''(
    ("+"\d{0}|\(\d{11}\)|\d{0}\(\d{10}\))? # area code
    (\d{0}) # first 3 digits
    (\d{11}) # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{0,3}))? # extension
    )''', re.VERBOSE)
    matches = re.findall(phone_regex, text)

    for match in matches:
        phones = list(match)
        for phone in phones:
            phone_numbers.add(phone)

    # # Add the phone numbers to the list
    # phone_numbers.extend(matches)

    return list(phone_numbers)

def ExtractEmile(text):
    email_addresses=[]

    # Use regular expressions to find email addresses
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    matches = re.findall(email_regex, text)

        # Add the email addresses to the list
    email_addresses.extend(matches)

    return email_addresses

# def get_filetype(filename):
#     _filetype = ''
#     _i = filename.rfind('.')
#     _filetype = filename[_i+1:]

#     return _filetype


def get_file_list(dir_path):
    files = os.scandir(dir_path) # Get a list of all files in the directory
    file_list = [] # Initialize empty lists for PDF file 
    for file in files:  # Loop through the list of files and append PDF and DOCX files to their respective lists
        if os.path.isdir(file):
            list_subfile = get_file_list(file)
            for subfile in list_subfile:
                file_list.append(subfile)
        else: 
            file_list.append(file.path)

    return file_list



# Set the directory path
dir_path = "CVs"
files = get_file_list(dir_path)

# print("PDF files:")
# print(pdf_files)

# if index file not exists will be created 
if not os.path.exists("index"):
   os.mkdir("index")
 
ix = create_in("index", schema= IndexFile)
ix = open_dir("index") # open index
writer = ix.writer()

for i in files:
   if i[-3:] == 'pdf':
        try:
            _text = ExtractPDFFile(i)
            _phone = ExtractNumbewr(_text)
            _email = ExtractEmile(_text)
            writer.add_document(
                file_name=i, 
                content=_text,
                phone=str(_phone),
                email=str(_email)
                )
        except:
            pass
   else:
        pass

# for j in docx_files:
#       ExtractDocxFile(j)
#       writer.add_document(file_name=j, content=ExtractDocxFile(j))

writer.commit()