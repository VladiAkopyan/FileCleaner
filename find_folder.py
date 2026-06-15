from pathlib import Path

def FindFileFromFolder(folder_in, folder_type):
    for file in Path(folder_in).rglob(folder_type):
        print(file)