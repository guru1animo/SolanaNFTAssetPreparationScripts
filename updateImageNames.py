import os
import json
import random

i=0

#useful when people always label images from 1-n instead of 0-n which metaplex upload requires

INPUT_DIR = "./assets"
OUTPUT_DIR = "./updated"

for file_name in os.listdir(INPUT_DIR):
    if ".png" in file_name:
        # # renames png file to a number
        new_name=int(file_name.replace(".png", ""))-1

        os.rename(f"{INPUT_DIR}/{file_name}", f"{OUTPUT_DIR}/{new_name}.png")
