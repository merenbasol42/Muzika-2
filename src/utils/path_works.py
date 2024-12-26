from os import path

def add(path1: str, *paths: str):
    return path.join(path1, *paths)