import os
from pathlib import Path
import datetime



def directory_listing(name):
    entries = Path(name)
    for entry in entries.iterdir():
        if os.path.isdir(entry):
            print(entry)
            directory_listing(entry)
        else:
            print("\t", entry, end="  ")
            info = entry.stat()
            print(str(info.st_size/(1024*1024))+"MB", "\t",
                  datetime.datetime.fromtimestamp(info.st_mtime).strftime("%d/%m/%y,%H:%M:%S"))

    # for file in os.listdir(name):



name = input("Enter directory path:")
directory_listing(name)
