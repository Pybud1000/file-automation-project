from pathlib import Path
import shutil
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def load_matrix():
    matrix = {}
    with open("matrix.csv") as File:
        for line in File:
            line = line.strip()
            parts = line.split(";")
            if parts[0] == "extension":
                continue
            matrix[parts[0]] = parts[1]
    return matrix

dir_path = Path(config["IO folders"]['source'])
output_path = Path(config["IO folders"]['output'])

keywords = load_matrix()

for file in dir_path.iterdir():

    ext = file
    folder_name = "" 

    if ext.suffix.lower() in keywords: # Bug-fix 2: Word case issue
        folder_name = keywords[ext.suffix.lower()]
    else:
        folder_name = "Unkown" # Bug-fix 1: if the file extension does not exist in the matrix or is unrecognizable

    folder_path = output_path/folder_name
    folder_path.mkdir(parents=True, exist_ok=True)

    shutil.copy2(file, folder_path)



