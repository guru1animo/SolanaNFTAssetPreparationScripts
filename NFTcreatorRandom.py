from PIL import Image
import random
import os
import sys
import json

counts={"Head":{},
        "Shirt":{},
        "Accessories":{},
        "Background":{},
        "Beard":{},
        "Face":{},
        "Hair":{},
        "Hat":{},
        "Left arm":{},
        "Legs":{},
        "Pants":{},
        "Right arm":{},
        "Shoes":{},
}

attributes = {}

metadata = {
  "name": "",
  "symbol": "TRADIE",
  "description": None,
  "seller_fee_basis_points": 1000,
  "image": "image.png",
  "external_url": "https://cryptotradiez.com/",
  "attributes": None,
   "collection": {
        "name": "Crypto Tradiez Original Release",
        "family": "Crypto Tradiez"
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

def random_choice(options) -> int:
    return random.randint(0, options-1)

def choose_image(name):
    dir = os.listdir(f"./{name}/")
    
    num_choice = random_choice(len(dir))

    image_choice = dir[num_choice]

    attributes[name]=image_choice.split(".")[0]

    image_location = f"./{name}/{image_choice}"

    try:
        counts[name][image_choice.split(".")[0]] += 1
    except:
        counts[name][image_choice.split(".")[0]] = 1

    return image_location

def getName(type):
    f = open(f"./Names/{type}.txt", "r")
    words = f.read().split('\n')
    name = words[random_choice(len(words))]
    f.close()

    return name

def create_metadata_file(number):   
    if random.randint(0, 1):
        metadata["name"] = f"{getName('adjectives')} {getName('names')}"
    else:
        metadata["name"] = f"{getName('names')} the {getName('adjectives')}"
    metadata["description"] = f"Crypto tradie token #{number+1} which will be used to build the NFT space!"
    attributes_for_metadata = []

    for trait, type in attributes.items():
        new_trait = {}
        new_trait["trait_type"] = trait
        new_trait["value"] = type

        attributes_for_metadata.append(new_trait)

    attributes.clear()

    # add quote
    new_trait = {}
    new_trait["trait_type"] = "Fav slang"
    new_trait["value"] = getName('slang')
    attributes_for_metadata.append(new_trait)

    metadata["attributes"] = attributes_for_metadata

    f = open(f"./.Completed/{number}.json", "w")
    json.dump(metadata, f)
    f.close()

def addTraitToImage(current_image, type, probability):
    if not random.randint(0, probability):
        trait = Image.open(choose_image(type))
        current_image.paste(trait, (0, 0), trait)
    return current_image

def main():
    for i in range(0, int(sys.argv[1])):
        if len(sys.argv) >= 3: 
            if sys.argv[2] == "--no-bg" or sys.argv[2] == "-nb":
                legs_img = choose_image("Legs")
                background = Image.open(legs_img)
        else:
            background = Image.open(choose_image("Background"))
            legs_img = choose_image("Legs")
            trait = Image.open(legs_img)
            background.paste(trait, (0, 0), trait)

        head_choice = random.randint(0, 100)

        if head_choice == 0:
            head = Image.open("./Heads/Alien.png")
            background.paste(head, (0, 0), head)
            current_image = background
            attributes["Head"]="Alien"
        elif head_choice >= 1 and head_choice <= 3:
            head = Image.open("./Heads/Dark.png")
            background.paste(head, (0, 0), head)
            current_image = background
            attributes["Head"]="Dark"
        else:
            current_image = addTraitToImage(background, "Head", 0)

        shirt_img = choose_image("Shirt")
        trait = Image.open(shirt_img)
        current_image.paste(trait, (0, 0), trait)

        current_image = addTraitToImage(current_image, "Left arm", 0)

        shoes_img = choose_image("Shoes")

        while ("Tank" in legs_img) and (("Skate" in shoes_img) or ("Thongs" in shoes_img)):
             shoes_img = choose_image("Shoes")

        trait = Image.open(shoes_img)
        current_image.paste(trait, (0, 0), trait)

        # current_image = addTraitToImage(current_image, "Shoes", 0)
        
        if "Painters" not in shirt_img:
          current_image = addTraitToImage(current_image, "Pants", 0) 

        current_image = addTraitToImage(current_image, "Face", 0)  
        current_image = addTraitToImage(current_image, "Beard", 3)
        
        # basically creates 1/3 chance of hair, hat or neither
        # more importantly you can't get both
        head_gear = random.randint(0, 2)

        if head_gear == 0:
            current_image = addTraitToImage(current_image, "Hair", 0)
        elif head_gear == 1:
            current_image = addTraitToImage(current_image, "Hat", 0)
        
        current_image = addTraitToImage(current_image, "Accessories", 3)
        current_image = addTraitToImage(current_image, "Right arm", 0) 
        
        current_image.save(f"./.Completed/{i}.png","PNG")

        create_metadata_file(i)

    print("*** STATISTICS ***")
    for category, options  in counts.items():
        print()
        print(f"Type: {category}")
        for item, occurences in options.items():
            print(f"Image: {item}, Occurences: {occurences}, Percentage occurences: %{occurences*100/float(sys.argv[1])}")
        
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: python NFTcreator.py [amount] [options]\n")
        print("Options:\n --no-bg : -nb\t\t\tNo background will be added to the images produced")
        exit()
    main()