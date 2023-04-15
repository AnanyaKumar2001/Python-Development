sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]

new_dict = {k: sampleDict[k] for k in keys}

print(new_dict)
