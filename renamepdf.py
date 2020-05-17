import os
from pdfrw import PdfReader

path = r'C:\Users\anthonymorada\Desktop\newFolder'


def renameFileToPDFTitle(path, fileName):
    fullName = os.path.join(path, fileName)
    # Extract pdf title from pdf file
    newName = PdfReader(fullName).Info.Title
    # Remove surrounding brackets that some pdf titles have
    newName = newName.strip('()') + '.pdf'
    newFullName = os.path.join(path, newName)
    os.rename(fullName, newFullName)


for fileName in os.listdir(path):
    # Rename only pdf files
    fullName = os.path.join(path, fileName)
    if (not os.path.isfile(fullName) or fileName[-4:] != '.pdf'):
        continue
    renameFileToPDFTitle(path, fileName)