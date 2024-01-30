from PyPDF2 import PdfMerger
import os

path = "./pdfs"

merger = PdfMerger()

for file in os.listdir(path):
    print("Viewed ", file)
    if file.endswith('.pdf'):
        print("Merging ", file)
        try:
            full_path = os.path.join(path, file)
            merger.append(full_path)
        except:
            print("Error while merging pdfs")
        else:
            print("Merged ", file)
    merger.write("MergedPDFs.pdf")