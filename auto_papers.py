#pip install watchdog
#pip install pdfrw

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import date
from PyPDF2 import PdfFileReader

import os
import json
import time
import shutil

## PDF Title
def get_pdf_title(pdf_file_path):

    pdf_reader = PdfFileReader(open(pdf_file_path, "rb")) 
    return pdf_reader.getDocumentInfo().title

## HANDLER
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            # Rename only pdf files
            if filename.endswith('.pdf'):
                src = folder_to_track + "/" + filename
                new_filename = get_pdf_title(src)
                input = PdfFileReader(src)
                if input.isEncrypted:
                    new_destination = folder_destination + "/" + filename + ".pdf"
                    os.rename(src,new_destination)
                else:
                    new_destination = folder_destination + "/" + new_filename + ".pdf"
                    os.rename(src,new_destination)

folder_to_track = "/Users/anthonymorada/Desktop/myFolder"
folder_destination = "/Users/anthonymorada/Desktop/newFolder"

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join
