import json

with open("example_2.json") as f:
    json_file = json.load(f)
print(json_file)
print(json_file["quiz"]["maths"]["q1"]["answer"])

