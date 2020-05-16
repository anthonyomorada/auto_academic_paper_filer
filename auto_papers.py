from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import date

import os
import json
import time
import shutil

#today = date.today()
#current_date = today.strftime("%Y/%m/%d")

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if filename.endswith('.pdf'):
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)

            
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
