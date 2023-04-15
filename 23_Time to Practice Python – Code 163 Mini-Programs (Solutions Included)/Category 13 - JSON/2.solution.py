import json

sample_json = """{"key1": "value1", "key2": "value2"}"""

data = json.loads(sample_json)
print(data["key2"])
