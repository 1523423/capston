import json

def find_all_refs(obj, key):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                yield v
            elif isinstance(v, (dict, list)):
                yield from find_all_refs(v, key)
    elif isinstance(obj, list):
        for item in obj:
            yield from find_all_refs(item, key)

def extract_version_ref(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    refs = list(find_all_refs(data, "bom-ref"))