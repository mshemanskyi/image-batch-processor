import sys
import time
import os
import getopt

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
            filePath = os.path.join(self.__src_path, filename)

            ImageProcessor.threshold(self, filePath, self.params)
            original_path = os.path.join(os.getcwd(), os.path.join('original', filename))

        print(self.params['listen'])
        if not self.params['listen']:
            #self.stop()
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

def runFromUI(blur, threshold, path, uiValues):
    blur = blur if blur else "5"
    threshold = threshold if threshold else "11"

    params = {
        'path': path if path else "input",
        'blur': int(blur),
        'threshold': int(threshold),
        'threshAdaptiveMethod': uiValues['threshAdaptiveMethod'],
        'threshType': uiValues['threshType'],
        'contAlgorithm': uiValues['contAlgorithm'],
        'debugThreshold': uiValues['debugThreshold'],
        'debugTrashLevel': uiValues['debugTrashLevel'],
        'filledContours': uiValues['filledContours'],
        'threshConstant': int(uiValues['threshConstant']),

        'saveOriginal': uiValues['saveOriginal'],

    }

    print('params:')
    for param in params:
        print(param + '=' +str(params[param]))
    print('_______')

    ImagesWatcher(params).run()

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:p:b:t:", ["path=", "blur=", "threshold="])
    except getopt.GetoptError:
        print("img-tool.py -p <folder> -b 5 -t 11")
        sys.exit(2)

    path = ""
    blur = ""
    threshold = ""
    threshAdaptiveMethod = ""
    threshType = ""
    thresholdConstant = ""
    listen = False

    for opt, arg in opts:
        if opt in ('-h', "--help"):
            print("img-tool.py -p <folder> -b 5 -t 11")
            sys.exit(2)
        elif opt in ("--path"):
            path = arg
        elif opt in ("--blur"):
            blur = arg
        elif opt in ("--threshold"):
            threshold = arg
        elif opt in ("--threshAdaptiveMethod"):
            threshAdaptiveMethod = arg
        elif opt in ("--threshType"):
            threshType = arg
        elif opt in ("--thresholdConstant"):
            thresholdConstant = arg
        elif opt in ("--listen"):
            listen = arg


    params = {
        'path': path if path else "input",
        'blur': blur if blur else 5,
        'threshold': threshold if threshold else 11,
        'threshAdaptiveMethod': threshAdaptiveMethod if threshAdaptiveMethod else "ADAPTIVE_THRESH_MEAN_C",
        'threshType': threshType if threshType else "THRESH_BINARY",
        'thresholdConstant': thresholdConstant if thresholdConstant else 2,
        'listen': listen if listen else False
    }

    print('params:')
    print(params)
    print('_______')

    ImagesWatcher(params).run()

if __name__ == "__main__":
    main()