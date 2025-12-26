import os
import pandas as pd     # Library for Excel
from pypdf import PdfReader as pr  # Library for PDF

# parent class for file processing
class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.filename = os.path.basename(file_path)
        #Uses os.path.basename to get only the file name from the full path
    def read_file(self):
        # check to see if the file exists before subclasses try to open it
        if not os.path.exists(self.file_path):
            return f"Error: The file '{self.filename}' was not found at {self.file_path}"
        return None

# child class for TEXT files
class TextProcessor(FileProcessor):
    def read_file(self):
        check = super().read_file()
        if check: return check # stop if the file does not exist
        #encoding is done to avoid errors with special characters
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def process_file(self):
        content = self.read_file()
        return f"Processed Text: Found {len(content.split())} words."
#---------------------------------2--------------------------------------------------
# child class for PDF files
class PDFProcessor(FileProcessor):
    def read_file(self):
        check = super().read_file()
        if check: return check
        
        try:
            reader = pr(self.file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            return text
        except Exception as e:
            return f"Error reading PDF: {e}"

    def process_file(self):
        reader = pr(self.file_path)
        return f"Processed PDF: Extracted text from {len(reader.pages)} pages."

#child class for EXCEL files
class ExcelProcessor(FileProcessor):
    def read_file(self):
        check = super().read_file()
        if check: return check
        
        try:
            df = pd.read_excel(self.file_path) #converts that table into a readable text format for printing
            #returns a string representation of the spreadsheet data
            return df.to_string()
        except Exception as e:
            return f"Error reading Excel: {e}"

    def process_file(self):
        df = pd.read_excel(self.file_path)
        return f"Processed Excel: Found {len(df)} rows and {len(df.columns)} columns."
#---------------------------------3--------------------------------------------------
# Execution and Demonstration of Polymorphism
# Create a list containing different types of objects
files = [
    TextProcessor(r"C:\Users\srest\OneDrive\Documents\hello.txt"),
    PDFProcessor(r"C:\Users\srest\OneDrive\Documents\ASSIGNMENT-8.pdf"),
    ExcelProcessor(r"C:\Users\srest\OneDrive\Documents\workseet1.xlsx")
]

for f in files:
    print(f"--- Currently Reading: {f.filename} ---")
    # We call the same methods regardless of the file type (Polymorphism)
    print(f.read_file()[:200] + "...") # Printing only first 200 chars for brevity
    print(f.process_file())
    print("-" * 50)