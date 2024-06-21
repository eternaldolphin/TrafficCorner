import os 
import json
import argparse
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, average_precision_score,precision_score,f1_score,recall_score,classification_report

# accident_types = {
#         "road debris": 0,
#         "traffic accident": 1,# for debug
#         "construction": 2,
#         "parking violations": 3,
#         "intrusion of non-motorized vehicles": 4,
#         "pedestrian violations": 5,
#         "obstacles": 6,
#         "wrong-way driving": 7,
#         "normal": 8,
#         "traffic congestion": 9,
#         # "running a red light": 10,
#         "crossing solid lines": 11,
#         # "failure to follow the designated lane": 12,
#         "traffic signal malfunction": 13
# }
# accident_types = {
#         "road debris": 0,
#         "traffic accident": 1,# for debug
#         "construction": 2,
#         "pedestrian violations": 5,
#         "normal": 8,
#         "traffic congestion": 9,
# }

from sklearn.metrics import confusion_matrix, precision_recall_fscore_support

def classification_metric(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    precisions = []
    # import ipdb;ipdb.set_trace()
    for class_id in range(6):
        tp = cm[class_id, class_id]
        fp = cm[:, class_id].sum() - tp
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        s = (np.array(y_true).astype(int) == class_id).sum()
        print(f"Class {class_id} - TP: {tp}, FP: {fp}, Support: {s}, Precision: {precision:.4f}")
        # print(f"Class {class_id} - TP: {tp}, FP: {fp}, Precision: {precision:.4f}, Support: {s}")
    weighted_precision = precision_score(y_true, y_pred, average='weighted')
    print("\nIntermediate variables:")
    # print("Precisions:", precisions)
    print(f"Weighted precision: {weighted_precision:.4f}")

    recalls = []
    for class_id in range(6):
        tp = cm[class_id, class_id]
        fn = cm[class_id, :].sum() - tp
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        s = (np.array(y_true).astype(int) == class_id).sum()
        print(f"Class {class_id} - TP: {tp}, FN: {fn}, Support: {s}, Recall: {recall:.4f}")
        # print(f"Class {class_id} - TP: {tp}, FN: {fn}, Recall: {recall:.4f}, Support: {s}")
    weighted_recall = recall_score(y_true, y_pred, average='weighted')
    print("\nIntermediate variables:")
    # print("Recalls:", recalls)
    print(f"Weighted recall: {weighted_recall:.4f}")

    # cm = confusion_matrix(y_true, y_pred)
    # conf_matrix = pd.DataFrame(cm, index=list(accident_types.keys()), columns=list(accident_types.keys()))
    # fig, ax = plt.subplots(figsize = (20,20))
    # sns.heatmap(conf_matrix, annot=True, annot_kws={"size": 12}, fmt='.20g', cmap="Blues")
    # plt.ylabel('True label', fontsize=12)
    # plt.xlabel('Predicted label', fontsize=12)
    # plt.xticks(fontsize=12)
    # plt.yticks(fontsize=12)
    # plt.savefig('confusion.pdf', bbox_inches='tight')
    # plt.show()
    # print('------Weighted------')
    # print('Weighted precision', precision_score(y_true, y_pred, average='weighted'))
    # print('Weighted recall', recall_score(y_true, y_pred, average='weighted'))
    # print('Weighted f1-score', f1_score(y_true, y_pred, average='weighted'))
    # print('------Macro------')
    # print('Macro precision', precision_score(y_true, y_pred, average='macro'))
    # print('Macro recall', recall_score(y_true, y_pred, average='macro'))
    # print('Macro f1-score', f1_score(y_true, y_pred, average='macro'))
    # print('------Micro------')
    # print('Micro precision', precision_score(y_true, y_pred, average='micro'))
    # print('Micro recall', recall_score(y_true, y_pred, average='micro'))
    # print('Micro f1-score', f1_score(y_true, y_pred, average='micro'))
    # print('------ClassificationReport------')
    # print(classification_report(y_true, y_pred, target_names=list(accident_types.keys())))

def extract_result(file_path):
    label_names = [] 
    with open(file_path, "r") as file:
        for line in file:
            data = json.loads(line)
            name = data['text'].split(";")[0].split(":")[1].strip().lower()
            if name == "traffic accidents":
                name = "traffic accident"
            label_names.append(name)
    result = [accident_types[label] for label in label_names if label in accident_types.keys()]
    return result

def extract_gt_pred(file_path, accident_types):
    groundtruths = []
    predictions = [] 
    with open(file_path, "r") as file:
        for line in file:
            data = json.loads(line)
            groundtruth = data["image_name"].split("/")[-2]
            # import ipdb;ipdb.set_trace()
            groundtruth = groundtruth.replace(groundtruth.split('_')[-1], "").replace("_", " ").strip()
            # if groundtruth == "traffic light damaged":
            #     groundtruth = "traffic signal malfunction"
            groundtruths.append(groundtruth)
            prediction = data['text'].split(";")[0].split(":")[1].strip().lower()
            # if prediction == "traffic light damaged":
            #     prediction = "traffic signal malfunction"
            predictions.append(prediction)

    _groundtruths = [accident_types[label] for label in groundtruths if label in accident_types.keys()]
    _predictions = [accident_types[label] for label in predictions if label in accident_types.keys()]

    assert len(_predictions) == len(_groundtruths)
    return _predictions, _groundtruths

def extract_accident_type(category_path):
    data = json.load(open(category_path))
    accident_types = {}
    for i, cat in enumerate(data.keys()):
        accident_types[cat] = i
    return accident_types        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ann_pred", default='output/baidu_mid/answer.jsonl')
    parser.add_argument("--category_path", default='scene_recognition/baidu_mid_categories.json')
    args = parser.parse_args()
    
    accident_types = extract_accident_type(args.category_path)
    y_pred, y_true = extract_gt_pred(args.ann_pred, accident_types)

    print(accident_types)
    classification_metric(y_true, y_pred)


