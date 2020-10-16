import os
import time
from watchdog.events import RegexMatchingEventHandler
from image_processor import ImageProcessor

class ImagesEventHandler(RegexMatchingEventHandler):

    def __init__(self, params):
        super().__init__()
        self.params = params

    def on_created(self, event):
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            time.sleep(1)

        self.process(event)

    def process(self, event):
        #process image
        ImageProcessor.do(self, event.src_path, self.params)