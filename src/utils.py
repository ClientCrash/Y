import os


def getCurrentOS():
    switcher = {
        "nt": "win"
    }
    return switcher.get(os.name, "other")
