import json

file_name = "data.json"

with open(file_name) as data:
    datos = json.load(data)

contado = 0
for key, value in datos.items():
    if contado < 4:
        if key == "version" and isinstance(value, list):
            print(f"{key}: {value[0]}")
        else:
            print(f"{key}: {value}")
        contado += 1
    else:
        break