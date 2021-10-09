import os
import yaml


def runDotY(stream):
    pass


def parseYConfig():
    o = {"y": "1.0.0"}
    with open("YFILE", "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("Cant read YFILE")
            print(exc)
            os.exit()
