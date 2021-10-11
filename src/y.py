import yaml
import sys
import category
from utils import *
from dataclasses import dataclass


def runDotY(filename):
    input_text = ""  # File content
    with open(filename, "r") as file:
        try:
            input_text = file.read()
            file.close()
        except:
            FileNotFoundError
            print("CANT READ " + filename)
            sys.exit()
    category_strings = category.getCategoryStrings(input_text)
    category_strings.pop(0)
    category_strings.pop(len(category_strings)-1)
    categorys = []
    for c_string in category_strings:
        print("putting string to parse : " + c_string)
        categorys.append(category.parseCategoryStringToCategory(c_string))
    for category_i in categorys:
        if(category_i.os == getCurrentOS()):
            runCategory(category_i)


def runCategory(category):
    pass


def readYamlFromFile(filename):
    with open(filename, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print("Cant read YFILE")
            print(exc)
            sys.exit()
