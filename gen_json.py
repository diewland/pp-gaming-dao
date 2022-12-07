import json, glob, random
from pprint import pprint as pp
 
NAME = "PoPose Gaming DAO"
DESC = "No utility, No roadmap. Just buy PoPose some stuff 👾"
IMG = "ipfs://xxxxxxxxxxxxxxx/{}_{}_{}_{}.png" # XXX XXX XXX
ENGINE = "Jigsaw Engine"

SRC_PATH = "./assets/*.png"
OUTPUT_DIR = "./json"
SHUFFLE_TIME = 99

if __name__ == '__main__':

    # load items from asset folder
    items = [ p.split('/')[-1] for p in glob.glob(SRC_PATH) ]

    # build chunk
    chunk = []
    for item in items:
        (keys, head, bg, qty) = item.split('.')[0].split('_')
        for i in range(0, int(qty)):
            # craft
            metadata = {
              "name": "***",
              "description": DESC,
              "image": IMG.format(keys, head, bg, qty),
              "attributes": [
                { "trait_type": "Keys",  "value": keys },
                { "trait_type": "Head",  "value": head },
                { "trait_type": "Background",  "value": bg },
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
