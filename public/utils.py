# encoding: utf-8
import os

def create_dir(dir_path):
    if os.path.isdir(dir_path):
        raise OSError("Direct almost exist")
    else:
        os.mkdir(dir_path)

