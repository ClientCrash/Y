
from dataclasses import dataclass
import re


def getCategoryStrings(input):
    file_data_categorys = re.split("\[|\]", input)
    categorys_strings = []
    for category in file_data_categorys:
        categorys_strings.append(category)
    return categorys_strings


@dataclass
class Category:
    os: str
    instructions: list


def parseCategoryStringToCategory(input_s):
    print(input_s)  # debug
    os = input_s.split(',')[0]
    print(os)
    inst = input_s.split(',')[1].split('\n')
    return Category(os, inst)
