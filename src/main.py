import os
import y
Y_VERSION = "0.1.0"
YFILEFILENAME = "YFILE"


def main():
    print("Y - " + Y_VERSION)
    config = y.readYamlFromFile(YFILEFILENAME)
    if(config["y"] != Y_VERSION):
        print("WARNING : THE Y VERSION IN THE YFILE DOES NOT MATCH THIS Y VERSION")
        print("THIS_Y_VERSION : " + Y_VERSION)
        print("Y_FILE_Y_VERSION : " + config["y"])
    y.runDotY(config["start"])


main()
