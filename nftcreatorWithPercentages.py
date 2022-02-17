from PIL import Image
import random
import os
import sys
import json

#this needs to be adjusted to the folder names of your images and the order they should be layered 
TRAIT_ORDER=["Background", "Body", "Eyes_Mouth", "Shirt", "Eyewear"]

#this should also be changed to what you want
metadata = {
  "name": "",
  "symbol": "AFGNHNDS",
  "description": None,
  "seller_fee_basis_points": 1000, 
  "image": "image.png",
  "external_url": "https://thewildathome.io/",
  "attributes": None,
   "collection": {
        "name": "Afghan Hounds Original Release",
        "family": "The Wild At Home"
   },
  "properties": {
    "files": [
      {
        "uri": "image.png",
        "type": "image/png"
      }
    ],
    "category": "image",
    "creators": [
      {
        "address": "REDACTED",
        "share": 100
      }
    ]
  }
}

#this is the chance of occurence in % of each trait, naming is important here
chance_of_each_trait = {
    "Background": {
        "Black":10,
        "Blue":10,
        "Green":10,
        "Orange":10,
        "Violet blue":10,
        "ART1":8,
        "ART2":8,
        "ART3":9,
        "ART4":8,
        "ART5":8,
        "ART6":9,
    }, 
    "Body": {
        "Normal":50,
        "Greyscale":25,
        "Rainbow":25
    },
    "Eyes_Mouth": {
        "Angry":50,
        "Normal":50
    },
    "Eyewear": {
        "3d Glasses":50,
        "Cheetah Glasses":25,
        "Art Glasses":25
    },
    "Shirt": {
        "Brown":25,
        "Tube":25,
        "Blue":25,
        "White grey":25
    },
}

counts={}
attributes = {}

def random_choice(options) -> int:
    return random.randint(0, options-1)

def add_to_count(name, trait_choice):
    if name not in counts.keys():
        counts[name] = {}

    if trait_choice in counts[name].keys():
        counts[name][trait_choice] += 1
    else:
        counts[name][trait_choice] = 1
         
def choose_image(name):
    dir = os.listdir(f"./{name}/")
    
    num_choice = random_choice(len(dir))

    image_choice = dir[num_choice]

    attributes[name]=image_choice.split(".")[0]

    image_location = f"./{name}/{image_choice}"

    add_to_count(name, image_choice.split(".")[0])

    return image_location

#optional for adding random names from a text file for your NFTs

# def get_name(type):
#     f = open(f"./Names/{type}.txt", "r")
#     words = f.read().split('\n')
#     name = words[random_choice(len(words))]
#     f.close()

#     return name

def get_item_using_stats(trait_name):
    chance = random.uniform(0, 99.99)

    current_range = 0

    for key, value in chance_of_each_trait[trait_name].items():
        if (chance-current_range) <= value:
            return key
        current_range+=value

def choose_value_using_stats(name):
    choice = get_item_using_stats(name)

    attributes[name]=choice

    add_to_count(name, choice)

def choose_image_using_stats(name):
    image_choice = get_item_using_stats(name)

    # if image_choice == "None" or image_choice == None:
    #     return None

    attributes[name]=image_choice

    image_location = f"./{name}/{image_choice}.png"

    add_to_count(name, image_choice)

    # try:
    #     counts[name][image_choice] += 1
    # except:
    #     counts[name][image_choice] = 1

    return image_location

def create_metadata_file(number):   
    metadata["name"] = f"Afghan hound #{number+1}"
    metadata["description"] = "Afghan hounds on solana!"
    attributes_for_metadata = []

    for trait, type in attributes.items():
        new_trait = {}
        new_trait["trait_type"] = trait
        new_trait["value"] = type

        attributes_for_metadata.append(new_trait)

    # clears so next NFT has correct attributes in metadata
    attributes.clear()

    metadata["attributes"] = attributes_for_metadata

    f = open(f"./.Completed/{number}.json", "w")
    json.dump(metadata, f)
    f.close()

def main():
    for i in range(0, int(sys.argv[1])):
        background = Image.open(choose_image_using_stats(TRAIT_ORDER[0]))

        for trait_name in TRAIT_ORDER[1:]:
            try:
                trait = Image.open(choose_image_using_stats(trait_name))
                background.paste(trait, (0, 0), trait)
            except:
                pass
        
        background.save(f"./.Completed/{i}.png","PNG")

        create_metadata_file(i)

    print("*** STATISTICS ***")
    for category, options in counts.items():
        print()
        print(f"Type: {category}")
        for item, occurences in options.items():
            print(f"Value: {item}, Occurences: {occurences}, Percentage occurences: %{occurences*100/float(sys.argv[1])}")
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python nftCreatorWithPercentages.py [amount]\n")
        exit()
    main()