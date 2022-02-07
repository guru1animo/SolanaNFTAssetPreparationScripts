import os
import json
import random
import csv

metadata = {
  "name": None,
  "symbol": "WKING",
  "description": "1555 Wukong Kings on Solana",
  "seller_fee_basis_points": 500,
  "image": "image.png",
  "external_url": "https://wukongkings.live/",
  "attributes": [],
  "properties": {
    "files": [{ "uri": "image.png", "type": "image/png" }],
    "category": "image",
    "creators": [
      {
        "address": "REDACTED",
        "share": 100
      }
    ]
  }
}

inputFile = open("traits.csv")

csvreader = csv.reader(inputFile)

trait_types = next(csvreader)[0].split(";")

print(trait_types)

for row in csvreader:
    traits = row[0].split(";")

    number = int(traits[0])-1

    outputFile = open(f"./Metadata/{number}.json", "w")

    metadata["name"] = f"Wukong king #{number+1}"

    metadata["attributes"] = []

    for index, trait in enumerate(traits[1:]):
        print(f"{index}: {trait}")
        if trait != "":
            metadata["attributes"].append({ "trait_type": f"{trait_types[index+1]}", "value": f"{trait}" })

    json.dump(metadata, outputFile)

    outputFile.close()