import os
import json
import random

#note: this adds no attributes properties

AMOUNT_OF_NFTS = 1000

metadata = {
  "name": None,
  "symbol": "HMSTRTWN",
  "description": "The collection of 10000 unique hamsters based on the solana network",
  "seller_fee_basis_points": 1000,
  "image": "image.png",
  "external_url": "https://hamstertown.xyz/",
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

for number in range(0, AMOUNT_OF_NFTS):
    outputFile = open(f"./Metadata/{number}.json", "a")

    metadata["name"] = f"Hamster #{number+1}"

    json.dump(metadata, outputFile)

    outputFile.close()