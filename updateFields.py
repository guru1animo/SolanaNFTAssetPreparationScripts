import os
import json
import random

# time so far 1:45 mins
# 1.56 SOL for upload approx. $300

i=0

INPUT_DIR = "./json"
OUTPUT_DIR = "./output"

for file_name in os.listdir(INPUT_DIR):
    if ".png" in file_name:
        # # renames png file to a number
        os.rename(f"{INPUT_DIR}/{file_name}", f"{OUTPUT_DIR}/{file_name}")
        continue
    input_file = open(f"{INPUT_DIR}/{i}.json", "r")
    data = json.load(input_file)
    input_file.close()

    # data["name"] = f"Lizard #{i+1}"
    # data["external_url"] = "https://boryokulizardz.live/"
    data["seller_fee_basis_points"] = 250
    # data["image"] = "image.png"
    
    # data["properties"]={
    #     "files": [{"uri": "image.png", "type": "image/png"}], 
    #     "category": "image", 
    #     "creators": [{"address": "JCsPh85J3mycMqA9DjeXh6CQcbhnUQ3ToZYbCuFRc7Wj", "share": 100}]
    #     }
    
    newfile = open(f"{OUTPUT_DIR}/{i}.json","w")

    json.dump(data, newfile)
    newfile.close()

    i+=1
