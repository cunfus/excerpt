from operator_db import insert_records
import os, sys, json

def transform(records_path):
    with open(records_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]

    # deal with the first line.
    head_line_parts = lines[0].split(' ')
    category = head_line_parts[0]
    source = head_line_parts[1]

    json_data = {
        "category": category,
        "source": source,
        "hitokotos": []
    }

    for line in lines[1:]:
        json_data["hitokotos"].append(line)
    
    trans_json_data = json.dumps(json_data, ensure_ascii=False)
    return trans_json_data

def single_file_reader(records_path):
    trans_json_data = transform(records_path)
    print(trans_json_data)
    insert_records(trans_json_data)

def single_dir_reader(records_dir_path):
    files = os.listdir(records_dir_path)
    for file in files:
        file_path = os.path.join(records_dir_path, file)
        single_file_reader(file_path)
    
if __name__ == '__main__':
    args = sys.argv

    for arg in args[1:]:
        if os.path.isfile(arg):
            single_file_reader(arg)
        elif os.path.isdir(arg):
            single_dir_reader(arg)
        else:
            print("path error!")