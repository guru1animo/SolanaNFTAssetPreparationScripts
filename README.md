# SolanaNFTAssetPreparationScripts
A bunch of random scripts that help to generate both randomly generate art from layers as well as metadata (json) files and renaming/updating all files to be compatible with Metaplex candy machine.

All metadata and images are prepared with reference to the metaplex standard here: https://docs.metaplex.com/candy-machine-v2/preparing-assets#-metadata-0json

Includes:
1) **createMetadata.py** script for creating json files from nothing. No attributes. 
2) **updateFields.py** script for updating certain fields in incorrectly generated metadata, usually supplied from Hashlips repo but the important detail this metadata has is the "attributes" from the art generation so it can't be created from scratch (unless you are the art creator which as a dev I have many situations where I don't generate the art itself).
3) **nftCreator.py** script generates layered art (.png format) with associated metadata includnig attributes in the art and numbered correctly. Has the ability to choose percentages for different art layers or other details. Several version of this generator with slight differences. 

**SET UP:**
to run the nftCreator.py you will need to set up the art layers in folders such as:
"Background"/"Blue.png"
where the name of the trait is the folder and the images are names are the actual attribute they are (this name will show up in the json metadata files generated).

A config file to specify desired percentage of occurences is also available at the top of one of the nftcreator files. It should be noted, it will not exactly follow these percentages as their is a degree of randomness and so will always spit out the statistics regarding the actual occurences as well. 
