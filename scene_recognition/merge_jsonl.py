import json

# file1_path = "playground/coda/answer_baseval1_gt.jsonl"
# file2_path = "playground/coda/answer_test_gt.jsonl"
# output_path = "playground/result/groundtruth.jsonl"

# file1_path = "playground/coda/answer_baseval1.jsonl"
# file2_path = "playground/coda/answer_test.jsonl"
# output_path = "playground/result/prediction.jsonl"

# file1_path = "./output/2209/answer_wodef.jsonl"
# file2_path = "./output/normal/answer.jsonl"
# output_path = "./output/0426/answer.jsonl"

file1_path = "./output/0426/answer1.jsonl"
file2_path = "./output/wrong_driving/answer.jsonl"
output_path = "./output/0426/answer.jsonl"

with open(output_path, "w") as output_file:
    with open(file1_path, "r") as file1:
        for line in file1:
            output_file.write(line)
    
    with open(file2_path, "r") as file2:
        for line in file2:
            output_file.write(line)