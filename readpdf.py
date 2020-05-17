from PyPDF2 import PdfFileReader

def get_pdf_title(pdf_file_path):

    pdf_reader = PdfFileReader(open(pdf_file_path, "rb")) 
    
    return pdf_reader.getDocumentInfo().title

title = get_pdf_title('/Users/anthonymorada/Desktop/myFolder/jgo-10-01-144.pdf')

#get_pdf_title('/Users/anthonymorada/Desktop/myFolder/jgo-10-01-144.pdf')
#print(title)
#print(len(title))