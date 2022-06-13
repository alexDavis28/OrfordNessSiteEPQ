import json
import os

title = input("Title: ")
latitude = float(input("Latitude: "))
longitude = float(input("Longitude: "))
description = input("Short description: ")

ids = []
with open("app/static/markers.json", "r") as file:
    file_data = json.load(file)

for marker in file_data["markers"]:
    ids.append(int(marker["ID"]))

last_id = max(ids)
new_id = f"{last_id+1:03}"

marker_data = {
    "Title": title,
    "ID": new_id,
    "Coordinates": [latitude, longitude],
    "Description": description
}

file_data["markers"].append(marker_data)

with open("app/static/markers.json", "w") as file:
    json.dump(file_data, file)

with open("app/static/info_base.html", "r") as base, open(f"app/templates/info/{new_id}.html", "w+") as new_file:
    base_text = base.read()
    base_text = base_text.replace("TITLE", title)
    base_text = base_text.replace("DESCRIPTION", description)
    new_file.write(base_text)

os.mkdir(f"app/static/images/{new_id}")
