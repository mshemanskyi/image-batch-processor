import sys
import getopt

from images_watcher import ImagesWatcher

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