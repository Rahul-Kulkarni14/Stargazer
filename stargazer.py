import streamlit as st
from datetime import datetime, date
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os

# Load the key from .env file
load_dotenv()
OAUTH_KEY = os.getenv("OAUTH_KEY")

def calculate_lst(longitude):
    current_utc_time = datetime.utcnow()
    JD = 367*current_utc_time.year - (7*(current_utc_time.year + ((current_utc_time.month + 9)//12)))//4 + (275*current_utc_time.month)//9 + current_utc_time.day + 1721013.5 + ((current_utc_time.second/60 + current_utc_time.minute)/60 + current_utc_time.hour)/24
    T = (JD - 2451545.0) / 36525
    GMST_deg = 280.46061837 + 360.98564736629 * (JD - 2451545.0) + T**2 * (0.000387933 - (T/38710000))
    GMST_deg = GMST_deg % 360
    GMST_hours = GMST_deg / 15
    LST = GMST_hours + (longitude / 15)
    LST = LST % 24
    return LST

def generate_skymap(location_name):
    geolocator = Nominatim(user_agent="stargazer_app")
    location = geolocator.geocode(location_name)
    latitude = location.latitude
    longitude = location.longitude
    lst = calculate_lst(longitude)
    zenith_declination = latitude

    options = {
        "observer": {
            "latitude": latitude,
            "longitude": longitude,
            "date": str(date.today()),
        },
        "view": {
            "type": "area",
            "parameters": {
                "position": {
                    "equatorial": {
                        "rightAscension": round(lst, 2),
                        "declination": round(zenith_declination, 2),
                    }
                },
                "zoom": 2,
            },
        },
    }

    resp = requests.post(
        "https://api.astronomyapi.com/api/v2/studio/star-chart",
        headers={"Authorization": f"Basic {OAUTH_KEY}"},
        json=options,
    )

    if resp.status_code == 200:
        content = resp.json()
        return content["data"]["imageUrl"]
    else:
        return None

def get_celestial_info(search_query):
    base_url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": search_query,
        "prop": "extracts",
        "exintro": True
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))
        title = page["title"]
        extract = page["extract"]
        soup = BeautifulSoup(extract, "html.parser")
        clean_text = soup.get_text()
        return title, clean_text
    else:
        return None, None

# Streamlit web app
st.title("StarGazer")
st.subheader("")
st.text("Explore the night sky")
st.header("Enter Location")
with st.form(key="form1"):
    location = st.text_input("Enter location:")
    submit_location = st.form_submit_button(label="Generate Skymap")

st.header("Enter Celestial Body")
with st.form(key="form2"):
    info = st.text_input("Enter celestial body:")
    submit_info = st.form_submit_button(label="Get Info")

# Handle user input and display results
if submit_location and location:
    skymap_url = generate_skymap(location)
    if skymap_url:
        st.image(skymap_url)
    else:
        st.write("Error: Unable to generate skymap for the provided location.")

if submit_info and info:
    title, extract = get_celestial_info(info)
    if title and extract:
        st.write(f"Name: {title}")
        st.write(f"Information: {extract}")
    else:
        st.write(f"Error: Unable to retrieve information for {info}")
