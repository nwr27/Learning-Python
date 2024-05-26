import json

# Data to be written
data = [
    {"name": "John Doe", "age": 30},
    {"name": "Jane Smith", "age": 25}
]

# File path
file_path = 'data.jsonl'

# Writing JSON objects to a .jsonl file
with open(file_path, 'w') as file:
    for item in data:
        json_string = json.dumps(item)
        file.write(json_string + '\n')
