import json
import numpy as np
from pprint import pprint
from collections import Counter


def get_train_class_dist(data_path, output_path):
    with open(data_path,'r') as f:
        sentence = f.readlines()

    output = {}
    for i in range(len(sentence)):
        #print(dataset[i])
        if sentence[i]=='\n':
            # word_newlineCount+=1
            continue
        
        tokens, bio_label=sentence[i].split() # B-PER
        # print(word, bio_label)

        output[bio_label] = {}

    for i in range(len(sentence)):
        #print(dataset[i])
        if sentence[i]=='\n':
            continue
        
        tokens, bio_label=sentence[i].split() # B-PER
        for key in output.keys():
            if key == bio_label:
                try:
                    output[key][tokens] += 1
                except KeyError:
                   output[key][tokens] = 1         
            else:
                if tokens not in output[key]:
                    output[key][tokens] = 0
    
  
    # pprint(output)
    with open(output_path, 'w') as f:
        json.dump(output, f, ensure_ascii=False)

if __name__ == "__main__":
    data_path = 'datasets/NER/WNUT2017/train.txt'
    output_path = "demo_train_class_distribution.json"
    get_train_class_dist(data_path, output_path)