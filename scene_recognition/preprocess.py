import os 
import argparse
import shutil
import json

def rename_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if not file_name.endswith('.jpg'):
                new_file_path = os.path.join(root, file_name + '.jpg')
                os.rename(file_path, new_file_path)
                print(f'Renamed: {file_path} -> {new_file_path}')

def check_normal(file_path, out_dir, data_dir):
    with open(file_path, "r") as file:
        for line in file:
            data = json.loads(line)
            prediction = data['text'].split(";")[0].split(":")[1].strip().lower()
            if prediction != "normal":
                print(prediction)
                # import ipdb;ipdb.set_trace()
                save_dir = out_dir + f"/{prediction}"
                shutil.move(os.path.join(data_dir, data['image_name']), os.path.join(save_dir, data['image_name'].split('/')[-1]))
                # shutil.copyfile(os.path.join(data_dir, data['image_name']), os.path.join(save_dir, data['image_name'].split('/')[-1]))

            

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default='./dataset')
    parser.add_argument("--normal_json", default='output/normal/answer.jsonl')
    parser.add_argument("--out-dir", default='./dataset/coda')

    args = parser.parse_args()
    check_normal(args.normal_json, args.out_dir, args.data_dir)
    # rename_files(args.data_dir)