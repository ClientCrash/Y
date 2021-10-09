import os
import yaml
Y_VERSION = "0.1.0"


def parseYConfig():
    o = {"y": "1.0.0"}
    with open("YFILE", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("Cant read YFILE")
            print(exc)
            os.exit()


def main():
    print("Y - " + Y_VERSION)
    config = parseYConfig()
    if(config["y"] != Y_VERSION):
        print("WARNING : THE Y VERSION IN THE YFILE DOES NOT MATCH THIS Y VERSION")
        print("THIS_Y_VERSION : " + Y_VERSION)
        print("Y_FILE_Y_VERSION : " + config["y"])


main()
