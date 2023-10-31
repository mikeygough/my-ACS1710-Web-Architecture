# json objects allow efficient and uniform transportation of data

# write and read json objects
import json

dictionaryJoke = {
    "type": "success",
    "value": {
        "id": 493,
        "joke": "Chuck Norris can binary search unsorted data.",
        "categories": ["nerdy"]
    }
}

# create .json file
with open('exampleObj.json', 'w') as outfile:
    json.dump(dictionaryJoke, outfile, indent=4)