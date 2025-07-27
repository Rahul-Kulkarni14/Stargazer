
# 🌌 StarGazer

**StarGazer** is a simple and interactive Streamlit web app that allows you to:

- 🔭 Generate a skymap for any location on Earth using AstronomyAPI
- 🌠 Get information about celestial bodies using Wikipedia

Whether you're an astronomy enthusiast or just curious about the night sky, this app gives you a real-time visual and educational experience.

---

## ✨ Features

- 📍 Generate a star chart based on your location and time
- 🌕 Search any planet, constellation, or celestial object to get quick information
- 🔐 Keeps your API key secure using environment variables (`.env`)

---

## 🛠 Installation & Setup

Follow these steps to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Stargazer.git
cd Stargazer
````

### 2. Install dependencies

Make sure you have Python 3.8+ installed, then:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setting up the AstronomyAPI Key

### 1. Go to [astronomyapi.com](https://astronomyapi.com)

* Sign up for a free account
* Go to your **Dashboard > Apps > Create App**
* Copy the **API Key** (it will look like a long string with `:` in it)

### 2. Create a `.env` file in your project folder

In the same directory as your `stargazer.py`, create a file named `.env` and add:

```env
OAUTH_KEY=your_api_key_here
```


## ▶️ Running the App

Once everything is set up, run:

```bash
streamlit run stargazer.py
```

Then go to `http://localhost:8501` in your browser to see the app.

---

## 🧰 Technologies Used

* [Streamlit](https://streamlit.io/) – for the web UI
* [AstronomyAPI](https://astronomyapi.com/) – for skymaps
* [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) – for object info
* [Geopy](https://geopy.readthedocs.io/en/stable/) – to convert location to coordinates
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – for parsing Wikipedia text
* [python-dotenv](https://pypi.org/project/python-dotenv/) – to manage secrets
