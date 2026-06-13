import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# ----------------------------
# CONFIG
# ----------------------------
API_KEY = "a3f417b116fa4104b3c547e8ee9d32e1"
BASE_URL = "https://newsapi.org/v2/top-headlines"

st.set_page_config(
    page_title="Advanced News Dashboard",
    page_icon="📰",
    layout="wide"
)

# ----------------------------
# SIDEBAR
# ----------------------------
st.sidebar.title("⚙️ News Filters")

countries = {
    "India": "in",
    "United States": "us",
    "United Kingdom": "gb",
    "Australia": "au",
    "Canada": "ca",
    "Germany": "de",
    "France": "fr",
    "Japan": "jp"
}

categories = [
    "general",
    "business",
    "entertainment",
    "health",
    "science",
    "sports",
    "technology"
]

selected_country = st.sidebar.selectbox(
    "🌍 Select Country",
    countries.keys()
)

selected_category = st.sidebar.selectbox(
    "📰 Select Topic",
    categories
)

keyword = st.sidebar.text_input(
    "🔍 Search Keyword",
    placeholder="AI, Tesla, Cricket..."
)

article_count = st.sidebar.slider(
    "📊 Number of Articles",
    min_value=5,
    max_value=50,
    value=15
)

# ----------------------------
# FETCH NEWS
# ----------------------------
@st.cache_data(ttl=600)
def fetch_news(country, category, query, count):
    params = {
        "apiKey": API_KEY,
        "country": country,
        "category": category,
        "pageSize": count
    }

    if query:
        params["q"] = query

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()
    return None

# ----------------------------
# HEADER
# ----------------------------
st.title("📰 Advanced News Dashboard")
st.markdown(
    "Search top headlines by **country**, **topic**, and **keywords**."
)

# ----------------------------
# LOAD DATA
# ----------------------------
data = fetch_news(
    countries[selected_country],
    selected_category,
    keyword,
    article_count
)

# ----------------------------
# DISPLAY RESULTS
# ----------------------------
if data and data.get("status") == "ok":

    articles = data.get("articles", [])

    st.success(f"Found {len(articles)} articles")

    for article in articles:

        with st.container():

            col1, col2 = st.columns([1, 3])

            with col1:
                if article.get("urlToImage"):
                    st.image(
                        article["urlToImage"],
                        use_container_width=True
                    )

            with col2:
                st.subheader(article.get("title", "No Title"))

                source = article.get("source", {}).get("name", "Unknown")

                published = article.get("publishedAt")

                try:
                    published = datetime.strptime(
                        published,
                        "%Y-%m-%dT%H:%M:%SZ"
                    ).strftime("%d %b %Y %H:%M")
                except:
                    pass

                st.caption(
                    f"Source: {source} | Published: {published}"
                )

                st.write(
                    article.get(
                        "description",
                        "No description available."
                    )
                )

                st.link_button(
                    "Read Full Article",
                    article.get("url")
                )

            st.divider()

    # ------------------------
    # ANALYTICS TABLE
    # ------------------------
    st.subheader("📈 News Summary")

    summary = pd.DataFrame([
        {
            "Title": a["title"],
            "Source": a["source"]["name"],
            "Published": a["publishedAt"]
        }
        for a in articles
    ])

    st.dataframe(summary, use_container_width=True)

else:
    st.error("Unable to fetch news. Check API key or try again later.")