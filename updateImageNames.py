import os
import json
import random

# time so far 1:45 mins
# 1.56 SOL for upload approx. $300

i=0

INPUT_DIR = "./json"
OUTPUT_DIR = "./updated"

for file_name in os.listdir(INPUT_DIR):
    if ".png" in file_name:
        # # renames png file to a number
        os.rename(f"{INPUT_DIR}/{file_name}", f"{OUTPUT_DIR}/{file_name}")
        continue
    input_file = open(f"{INPUT_DIR}/{(i+1)}.json", "r")
    data = json.load(input_file)
    input_file.close()

    data["symbol"] = "DISDONK"
    data["seller_fee_basis_points"] = 1000
    data["image"] = "image.png"
    data["external_url"] = "https://discodonkeys.store/"
    data["collection"] = { "name": "Disco Donkeys Original Release", "family": "Disco Donkeys" },

    data.pop("dna")
    data.pop("edition")
    data.pop("date")
    data.pop("compiler")
    
    data["properties"]={
        "files": [{"uri": "image.png", "type": "image/png"}], 
        "category": "image", 
        "creators": [{"address": "DT2nRzvurYhLkWh4EXisjvnx6SKgKqEfiy9orYkN4K68", "share": 100}]
        }
    
    newfile = open(f"{OUTPUT_DIR}/{i}.json","w")

    json.dump(data, newfile)
    newfile.close()

    i+=1
