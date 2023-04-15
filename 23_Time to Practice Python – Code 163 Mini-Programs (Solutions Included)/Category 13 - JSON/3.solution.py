import json

sample_json = {"id": 1, "name": "value2", "age": 29}

with open("sample_json.json", "w") as file:
    json.dump(sample_json, file, indent=4, sort_keys=True)

print("Done")
