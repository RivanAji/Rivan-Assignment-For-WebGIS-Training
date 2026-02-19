import streamlit as st
import folium
from streamlit_folium import st_folium
import requests
st.set_page_config(layout="wide")
st.title("WebGIS - Indeks Kualitas Lingkungan (IKL)")
api_url = "http://127.0.0.1:5000/api/ikl"
response = requests.get(api_url)
if response.status_code != 200:
    st.error("API tidak dapat diakses. Pastikan Flask server berjalan.")
    st.stop()
ikl_geojson = response.json()

m = folium.Map(
    location=[-6.125, 106.880],
    zoom_start=12,
    tiles="cartodbpositron"
)

def style_function(feature):
    kelas = feature["properties"].get("IKL_KELAS", "")

    color_dict = {
        "Sangat Rendah": "#ffffcc",
        "Rendah": "#c2e699",
        "Sedang": "#78c679",
        "Tinggi": "#31a354",
        "Sangat Tinggi": "#006837"
    }

    return {
        "fillColor": color_dict.get(kelas, "#cccccc"),
        "color": "black",
        "weight": 0.5,
        "fillOpacity": 0.7
    }

folium.GeoJson(
    ikl_geojson,
    name="IKL",
    style_function=style_function,
    tooltip=folium.GeoJsonTooltip(
        fields=["IKL", "IKL_KELAS"],
        aliases=["Nilai IKL:", "Kelas IKL:"],
        localize=True
    )
).add_to(m)

folium.LayerControl().add_to(m)
st_folium(m, width=1200, height=700)

# ===== cara run =====
# cd "Assignment/Rivan-Assignment 6" 
# ../../.venv/bin/python -m streamlit run "Rivan - APP ikl.py"