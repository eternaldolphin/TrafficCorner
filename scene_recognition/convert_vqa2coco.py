# Copyright (c) Facebook, Inc. and its affiliates.
import os
import argparse
import json
from PIL import Image

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ann", default='scene_recognition/corner_case.json')
    parser.add_argument("--image-path", type=str, default="./dataset")
    args = parser.parse_args()

    print('Loading', args.ann)
    data = json.load(open(args.ann, 'r'))
    cats = []
    for i, cat in enumerate(list(data.keys())):
        cur_cat = {"id": i, "def": data[cat][0], "description": data[cat][1], "name": cat}
        cats.append(cur_cat)

    idx = -1
    images = []
    for root, dirs, files in os.walk(args.image_path):
        for file_name in files:
            image_path = os.path.join(root, file_name)
            idx += 1

            with Image.open(image_path) as img:
                width, height = img.size

            image_info = {
                "filename": root.replace(args.image_path+'/','')+'/'+file_name,
                "height": height,
                "width": width,
                "id": idx
            }
            images.append(image_info)
    coco_annotations = {"images": images, "categories": cats}
    import ipdb;ipdb.set_trace()    

    out_path = args.ann[:-5] + '_coco.json'
    print('Saving to', out_path)
    json.dump(coco_annotations, open(out_path, 'w'))
    