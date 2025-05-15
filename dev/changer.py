import yaml
import json

def convert_yml_to_json(yml_path, json_path):
    with open(yml_path, 'r', encoding='utf-8') as yml_file:
        data = yaml.safe_load(yml_file)

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=2, ensure_ascii=False)

# 예시 사용
convert_yml_to_json('input.yml', 'output.json')