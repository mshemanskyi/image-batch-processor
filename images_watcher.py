import sys
import time
import os

from watchdog.observers import Observer
from events_handler import ImagesEventHandler
from image_processor import ImageProcessor

class ImagesWatcher:
    def __init__(self, params):
        self.params = params
        self.__src_path = params['path']
        self.__event_handler = ImagesEventHandler(params)
        self.__event_observer = Observer()

    def run(self):
        #On Start, check if any images exists in folder
        for filename in os.listdir(self.__src_path):
            if filename == '.keep':
                continue

            filePath = os.path.join(self.__src_path, filename)

            ImageProcessor.do(self, filePath, self.params)

        print(self.params['watch'])
        if not self.params['watch']:
            sys.exit(2)

        self.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )