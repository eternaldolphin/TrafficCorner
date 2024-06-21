import json
import os
all_path = "./output/0426/answer.jsonl"
output_path = "./output/baidu_mid/answer.jsonl"
extra = os.listdir('dataset/coda/traffic_congestion_59')

# with open(output_path, "w") as output_file:
#     with open(all_path, "r") as file1:
#         for line in file1:
#             if json.loads(line)["image_name"].split('/')[-1] in extra:
#                 input_data = json.loads(line)
#                 # import ipdb;ipdb.set_trace()
#                 input_data["image_name"] = os.path.join('coda/traffic_congestion_59', json.loads(line)["image_name"].split('/')[-1])
#                 output_file.write(json.dumps(input_data)+'\n')

#             if os.path.exists(os.path.join('dataset', json.loads(line)["image_name"].replace("construction_182", "construction_186").replace("normal_1203", "normal_1140"))):
#                 input_data = json.loads(line)
#                 input_data["image_name"] = os.path.join('dataset', json.loads(line)["image_name"].replace("construction_182", "construction_186").replace("normal_1203", "normal_1140"))
#                 output_file.write(json.dumps(input_data)+'\n')

# answer_files = []
# with open(output_path, "r") as file1:
#         for line in file1:
#             answer_files.append(json.loads(line)["image_name"].split('/')[-1])

# ques_path = "output/baidu_mid/question.jsonl"
# question_files = []
# with open(ques_path, "r") as file1:
#     for line in file1:
#         question_files.append(json.loads(line)["image"].split('/')[-1])
# import ipdb;ipdb.set_trace()
# for path in question_files:
#     if path not in answer_files:
#         print(path)