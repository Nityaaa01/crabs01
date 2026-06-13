from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")

BASE_URL = "https://newsapi.org/v2/top-headlines"

COUNTRIES = {
    "India": "in",
    "United States": "us",
    "United Kingdom": "gb",
    "Australia": "au",
    "Canada": "ca",
    "Germany": "de",
    "France": "fr",
    "Japan": "jp"
}

CATEGORIES = [
    "business",
    "entertainment",
    "general",
    "health",
    "science",
    "sports",
    "technology"
]