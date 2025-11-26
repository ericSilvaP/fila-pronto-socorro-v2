import re


def replaceNonNumbers(string: str):
    return re.sub("[^0-9]+", "", string)
