import json, random
from pprint import pprint as pp
 
NAME = "PoPose Gaming DAO"
DESC = "No utility, No roadmap. Just buy PoPose some stuff 👾"
ENGINE = "Jigsaw Engine"

OUTPUT_DIR = "./json"
SHUFFLE_TIME = 99

CONFIG = (
    ( 87, "W", "***" ),
    ( 65, "A", "***" ),
    ( 83, "S", "***" ),
    ( 68, "D", "***" ),
    ( 3,  "X", "***" ),
)


# build chunk
chunk = []
for cfg in CONFIG:
    (qty, key, img) = cfg
    for i in range(0, qty):
        # craft
        metadata = {
          "name": "***",
          "description": DESC,
          "image": img,
          "attributes": [
            { "trait_type": "Key",  "value": key },
          ],
          "compiler": ENGINE,
        }
        # add to chunk
        chunk.append(metadata)

# shuffle
for rnd in range(1, SHUFFLE_TIME+1):
    random.shuffle(chunk)

# update name
for idx, metadata in enumerate(chunk):
    metadata["name"] = "{} #{}".format(NAME, idx+1)

# write file
for idx, metadata in enumerate(chunk):
    with open("./{}/{}.json".format(OUTPUT_DIR, idx+1), "w") as f:
        json.dump(metadata, f, ensure_ascii=False)
