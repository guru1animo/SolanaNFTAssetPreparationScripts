import os
import json
import random

i=0

INPUT_DIR = "./json"
OUTPUT_DIR = "./output"

for file_name in os.listdir(INPUT_DIR):
    input_file = open(f"{INPUT_DIR}/{i}.json", "r")
    data = json.load(input_file)
    input_file.close()
    # attributes = file_name.split('.')
    # attributes.remove("PNG")
    # try:
    #     attributes.remove('')
    # except:
    #     pass

    # attributes = [x.strip() for x in attributes]
    # attributes = [x.replace(" of ", "/") for x in attributes]

    data["external_url"] = "https://solanasantanft.live/"
    
    # traits = []
    # for att in attributes[1:]:
    #     #add to array
    #     trait = {"trait_type": att, "value": True}
    #     traits.append(trait)
    
    # data["name"] = attributes[0]
    # data["symbol"] = "NFTPro"
    # data["description"]  = "How the mighty have fallen! The Greek Gods of Mt Olympus, reduced to pixel art NFTs, held captive on the Solana blockchain, and traded at the whim of mortals."
    # data["collection"]={"name": "Rogue Sols Original Release", "family": "Rogue Sols"}
    # data["seller_fee_basis_points"] = 500
    # data["image"] = "image.png"
    # data["attributes"] = traits
    # data["properties"]={
    #     "files": [{"uri": "image.png", "type": "image/png"}], 
    #     "category": "image", 
    #     "creators": [{"address": "REDACTED", "share": 100}]
    #     }
    
    newfile = open(f"{OUTPUT_DIR}/{i}.json","w")

    json.dump(data, newfile)
    newfile.close()

    # # renames png file to a number
    # os.rename(f"{INPUT_DIR}/{file_name}", f"{OUTPUT_DIR}/{i}.png")

    i+=1
