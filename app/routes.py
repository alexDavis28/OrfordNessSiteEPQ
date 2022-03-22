from app import app
from flask import render_template
import folium


# Home page
@app.route('/')
@app.route("/home")
def home():

    # Create map
    start_coords = (52.08047199559282, 1.5519507329068511)
    folium_map = folium.Map(location=start_coords, zoom_start=12)

    # Add marker for armoury building
    folium.Marker(
        [52.08047199559282, 1.5519507329068511],
        popup='See more',
        tooltip="<b>Armoury</b>"
    ).add_to(folium_map)

    map_html = folium_map._repr_html_()

    return render_template("home.html", map=map_html)
