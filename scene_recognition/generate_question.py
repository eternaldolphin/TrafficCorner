import argparse
import os
from PIL import Image
import json

 
def generate_question(folder_path, prompt, output_jsonl_path):
    idx = -1
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            image_path = os.path.join(root, file_name)
            idx += 1
            with Image.open(image_path) as img:
                width, height = img.size

            question_info = {
                "question_id": idx,
                "image": root.replace(folder_path+'/','')+'/'+file_name,
                "text": prompt, 
                "category": "detail"
            }

            # 将问题信息字典写入JSONL文件
            with open(output_jsonl_path, 'a') as jsonl_file:
                jsonl_file.write(json.dumps(question_info) + '\n')

    print(f"JSONL文件已创建:{output_jsonl_path}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-path", type=str, default="./dataset")
    parser.add_argument("--output-path", type=str, default="./output/baidu_mid/question.jsonl")
    parser.add_argument("--category-path", type=str, default="./scene_recognition/baidu_mid_categories.json")
    args = parser.parse_args()

    categories_info = json.load(open(args.category_path))
    categories_name = list(categories_info.keys())
    categories_len = len(categories_name)
    categories_description = [categories_name[i]+' refers '+list(categories_info.values())[i][-1] for i in range(categories_len)]

    prompt = f"Type: [one of the candidate types, e.g., {categories_name}]; Reason: [concise phrase explaining the identified issue ]. If no specific corner cases are identified, respond with: Type: normal; Reason: No corner cases found."

    generate_question(args.image_path, prompt, args.output_path)