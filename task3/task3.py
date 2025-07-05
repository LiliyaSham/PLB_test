import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def build_value_map(values_data):
    value_map = {}
    for item in values_data.get("values", []):
        value_map[item["id"]] = item["value"]
    return value_map

def fill_values_in_structure(data, value_map):
    if isinstance(data, list):
        for elem in data:
            fill_values_in_structure(elem, value_map)
    elif isinstance(data, dict):
        if "id" in data and data["id"] in value_map:
            data["value"] = value_map[data["id"]]
        for key in data:
            if isinstance(data[key], list):
                fill_values_in_structure(data[key], value_map)

tests_data = load_json('tests.json')
values_data = load_json('values.json')

value_map = build_value_map(values_data)

report_data = json.loads(json.dumps(tests_data))
fill_values_in_structure(report_data, value_map)

with open('report.json', 'w', encoding='utf-8') as file3:
    json.dump(report_data, file3, ensure_ascii=False, indent=2)