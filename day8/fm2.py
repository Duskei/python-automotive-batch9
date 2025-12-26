# Base class
class FileProcessor:
    def read_file(self):
        pass

    def process_file(self):
        pass


# PDF file class
class PDFFile(FileProcessor):
    def read_file(self):
        print("Reading content from PDF file")

    def process_file(self):
        print("Processing PDF file data")


# Excel file class
class ExcelFile(FileProcessor):
    def read_file(self):
        print("Reading data from Excel file")

    def process_file(self):
        print("Processing Excel file data")


# Text file class
class TextFile(FileProcessor):
    def read_file(self):
        print("Reading text from Text file")

    def process_file(self):
        print("Processing Text file data")


# -------- Main Execution --------
files = [
    PDFFile(),
    ExcelFile(),
    TextFile()
]

for file in files:
    file.read_file()
    file.process_file()
    print("--------------------")