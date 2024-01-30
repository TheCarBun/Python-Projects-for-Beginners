from PyPDF2 import PdfMerger
import os

path = "./pdfs"

merger = PdfMerger()

for file in os.listdir(path):
    print(file)
    if file.endswith('.pdf'):
        full_path = os.path.join(path, file)
        merger.append(full_path)
    merger.write("MergedPDFs.pdf")