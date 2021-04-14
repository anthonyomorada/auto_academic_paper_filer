from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import shutil

## HANDLER
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            # Rename only pdf files
            if filename.endswith('.pdf'):
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename + ".pdf"
                os.rename(src,new_destination)

folder_to_track = "/Users/anthonymorada/Downloads"
folder_destination = "/Users/anthonymorada/Desktop/Papers to Read"

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
