from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

path_to_observe = r"C:\Users\Biplob\Downloads"

def on_create(event):
    print (f"new file created {event.src_path}")


class Watcher():
    def __init__(self,path):
        self.path = path
        self.observer = Observer()

    def start(self):
        event_handler = FileSystemEventHandler()
        event_handler.on_created = on_create
        self.observer.schedule (event_handler,self.path,recursive=False)
        self.observer.start()

    def stop (self):
        self.observer.stop()
        self.observer.join()


watcher = Watcher(path_to_observe)

try :
    print(f"watching folder : {path_to_observe}")
    watcher.start()
    while True:
        time.sleep(30)

except KeyboardInterrupt:
    print("\n stopping warcher ")
    watcher.stop()
    print("watcher stoped")