import os
import glob
import sys
import json
import shutil
import cv2 as cv

def main():
    f = open("settings.json")
    settings = json.load(f)
    try:
        rootDir = settings["rootDir"]
    except KeyError:
        print("Invalid Setting file: 'rootDir' is not exists.")

    try:
        dists = settings["dist"]
    except KeyError:
        print("Invalid Setting file: 'dists' is not exists.")

    imgList = glob.glob("{}*".format(rootDir))
    itr = 0
    cv.namedWindow("img", cv.WINDOW_KEEPRATIO | cv.WINDOW_NORMAL)
    print(len(imgList))
    while itr < len(imgList):
        path = imgList[itr]
        if os.path.isdir(os.path.join(rootDir,path)):
            itr += 1

        elif os.path.splitext(path)[1] == ".gif":
            print("Skip gif image:{}".format(path))
            itr += 1

        elif os.path.splitext(path)[1] == ".ini":
            itr += 1

        else:
            print("{0}:read {1}".format(itr,path))
            img = cv.imread(path)
            cv.imshow("img",img)
            k = cv.waitKey(0)
            if k == ord('q'):
                sys.exit(0)
            elif k == 81:
                if itr != 0:
                    itr -= 1
            elif k == 83:
                itr += 1
            else:
                for key in dists.keys():
                    if k == ord(key):
                        file = os.path.basename(path)
                        distPath = os.path.join(dists[key],file)
                        if os.path.exists(distPath):
                            print("file is already exist.{}".format(distPath))
                        else:
                            shutil.move(path,dists[key])
                            print("{0} move to {1}.".format(path,dists[key]))
                            itr += 1
                            break


if __name__ == '__main__':
    main()
