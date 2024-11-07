import json

file_path = "groceries.json"

with open(file_path, "r") as file:
    data = file.read()

parsed_data = json.loads(data)

for key, value in parsed_data.items():
    print(f"Fruit: {key} Amount, {value}")
