from app import app
from flask import render_template, request
import folium
import json
import os

# Home page
@app.route('/')
@app.route("/home")
def home():
    print(app.static_folder)
    # Read data on markers
    with open(app.static_folder + "\markers.json", "r") as data:
        markers = json.load(data)["markers"]

    # Create map
    start_coords = (52.08047199559282, 1.5519507329068511)
    folium_map = folium.Map(location=start_coords, zoom_start=14)

    # Add each marker to the map

    for marker in markers:
        folium.Marker(
            marker["Coordinates"],
            popup=f"<div class='popup'> <h6 class='popup-title'><b>{marker['Title']}</b></h6>"
                  f"<p class='popup-description'>{marker['Description']}</p>"
                  f"<p><a href='/info?id={marker['ID']}' target='_blank' class=popup-link'>See more</a></p> </div>",
            tooltip=f"<b>{marker['Title']}</b>"
        ).add_to(folium_map)

    map_html = folium_map._repr_html_()

    return render_template("home.html", map=map_html)


@app.route("/info")
def info():
    page_id = request.args.get('id', type=str, default="001")
    file_path = "info/" + page_id + ".html"

    images = []
    image_folder = app.static_folder + "\\images\\" + page_id + "\\"

    for file in os.listdir(image_folder):
        filename = os.fsdecode(file)
        image_path = "\\static\\images\\" + page_id + "\\" + filename
        images.append(image_path)
    print(images)

    return render_template(file_path, images=images)
