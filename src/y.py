import os
import yaml
import re
import sys


def runDotY(filename):
    filec = ""  # File content
    with open(filename, "r") as file:
        try:
            filec = file.read()
            file.close()
        except:
            FileNotFoundError
            print("CANT READ " + filename)
            sys.exit()
    file_data_categorys = re.split("\[|\]", filec)
    for category in file_data_categorys:
        print(category)  # just for debug


def readYamlFromFile(filename):
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("Cant read YFILE")
            print(exc)
            sys.exit()
