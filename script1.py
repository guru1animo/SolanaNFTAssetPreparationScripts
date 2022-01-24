import os
import json
import random

# time so far 1:45 mins
# 1.56 SOL for upload approx. $300

i=0

for file_name in os.listdir("./PNG Images (926)"):
    data = {}

    attributes = file_name.split('.')
    attributes.remove("PNG")
    try:
        attributes.remove('')
    except:
        pass

    attributes = [x.strip() for x in attributes]
    attributes = [x.replace(" of ", "/") for x in attributes]

    
    traits = []
    for att in attributes[1:]:
        #add to array
        trait = {"trait_type": att, "value": True}
        traits.append(trait)

    
    data["name"] = attributes[0]
    data["symbol"] = "NFTPro"
    data["description"]  = "How the mighty have fallen! The Greek Gods of Mt Olympus, reduced to pixel art NFTs, held captive on the Solana blockchain, and traded at the whim of mortals."
    # data["collection"]={"name": "Rogue Sols Original Release", "family": "Rogue Sols"}
    data["seller_fee_basis_points"] = 500
    data["image"] = "image.png"
    data["attributes"] = traits
    data["properties"]={
        "files": [{"uri": "image.png", "type": "image/png"}], 
        "category": "image", 
        "creators": [{"address": "GY5mGWDr9jj7Y4jCzC6NeevFY43DDwfAkk7K4RSsfRNs", "share": 100}]
        }
    
    newfile = open(f"./PROD (926)/{i}.json","w")

    json.dump(data, newfile)
    newfile.close()

    # # renames png file to a number
    os.rename(f"./PNG Images (926)/{file_name}", f"./PROD (926)/{i}.png")

    i+=1
