from app import app
from flask import render_template
import folium
import json


# Home page
@app.route('/')
@app.route("/home")
def home():
    print(app.static_folder)
    # Read data on markers
    with open(app.static_folder+"\markers.json", "r") as data:
        markers = json.load(data)["markers"]

    # Create map
    start_coords = (52.08047199559282, 1.5519507329068511)
    folium_map = folium.Map(location=start_coords, zoom_start=12)

    # Add each marker to the map

    for marker in markers:
        folium.Marker(
            marker["Coordinates"],
            popup=f"<p>{marker['Description']}</p> <br> <a>See more<a>",
            tooltip=f"<b>{marker['Title']}</b>"
        ).add_to(folium_map)

    map_html = folium_map._repr_html_()

    return render_template("home.html", map=map_html)
