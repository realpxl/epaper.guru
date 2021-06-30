from PyPDF2 import PdfFileReader, PdfFileMerger

def merge_pdf(page_count):
    
#     pdf_file1 = PdfFileReader("1.pdf")
#     pdf_file2 = PdfFileReader("2.pdf")
#     output = PdfFileMerger()
#     output.append(pdf_file1)
#     output.append(pdf_file2)
# 
#     with open("merged.pdf", "wb") as output_stream:
#         output.write(output_stream)
    
    merger = PdfFileMerger()
    
    
    for i in range(1,page_count+1):        
        
        pdf_name = str(i)+".pdf"
        
        
        merger.append(PdfFileReader(pdf_name, 'rb'))
        print("Appending "+pdf_name)
    
    print("starting to merge...")
    merger.write("merged.pdf")
    print("merged.pdf written")
    

        
