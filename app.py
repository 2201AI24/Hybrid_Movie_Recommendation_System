# ✅ Enhanced Movie Recommendation System (Streamlit + Hybrid Model)

import streamlit as st
import pandas as pd
import pickle
import requests
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from difflib import get_close_matches
import os
from dotenv import load_dotenv

# Load content-based movie data and similarity
movies, similarity = pickle.load(open('movie_data.pkl', 'rb'))

# Load collaborative scores
with open("collab_scores.pkl", "rb") as f:
    collab_scores = pickle.load(f)

load_dotenv()
api_key = os.getenv("TMDB_API_KEY")


# Fetch poster and metadata from TMDB
@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        poster_path = data.get('poster_path')
        if not poster_path:
            return ("No Poster", "N/A", "", "Metadata not available", "N/A")

        poster_url = "https://image.tmdb.org/t/p/w500/" + poster_path
        rating = data.get('vote_average', 'N/A')
        genres = ", ".join([genre['name'] for genre in data.get('genres', [])])
        overview = data.get('overview', 'No overview available.')
        release_date = data.get('release_date', 'N/A')

        return poster_url, rating, genres, overview, release_date
    except:
        return ("No Poster", "N/A", "", "Metadata not available", "N/A")

# Match title
def get_best_match(title, movie_list):
    matches = get_close_matches(title, movie_list, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Hybrid recommender
def hybrid_recommend(movie, user_id=1, alpha=0.5):
    if movie not in movies['title'].values:
        return None

    index = movies[movies['title'] == movie].index[0]
    content_scores = similarity[index]

    hybrid_scores = []
    for i in range(len(movies)):
        movie_id = movies.iloc[i].movie_id
        collab_score = collab_scores.get(user_id, {}).get(movie_id, 0.0) / 5
        final_score = alpha * content_scores[i] + (1 - alpha) * collab_score
        hybrid_scores.append((i, final_score))

    top = sorted(hybrid_scores, key=lambda x: x[1], reverse=True)[1:11]
    results = []
    for i, _ in top:
        m = movies.iloc[i]
        results.append({
            "title": m.title,
            "movie_id": m.movie_id
        })
    return results

# Simulated evaluation

def simulated_precision_at_k():
    return round(random.uniform(0.6, 0.9), 2)

def simulated_coverage():
    return round(random.uniform(0.4, 0.7), 2)

def simulated_diversity():
    return round(random.uniform(0.5, 0.8), 2)

def plot_similarity_heatmap():
    fig, ax = plt.subplots()
    sample_indices = random.sample(range(len(similarity)), 10)
    sample_matrix = similarity[sample_indices][:, sample_indices]
    sns.heatmap(sample_matrix, cmap="YlGnBu", xticklabels=False, yticklabels=False, ax=ax)
    ax.set_title("Similarity Heatmap (Sample)")
    st.pyplot(fig)

# UI Setup
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommendation System")
tabs = st.tabs(["🔍 Recommender", "📊 Evaluation Dashboard"])

# Sidebar: Dark Mode Toggle
st.sidebar.markdown("## ⚙️ Settings")
dark_mode = st.sidebar.checkbox("🌙 Enable Dark Mode")
if dark_mode:
    st.markdown("""
        <style>
        body, .stApp {
            background-color: #1e1e1e;
            color: white;
        }
        .stButton button { background-color: #333 !important; color: white !important; }
        .stMarkdown a { color: #4db8ff !important; }
        </style>
    """, unsafe_allow_html=True)

# Session State
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'scroll_to' not in st.session_state:
    st.session_state.scroll_to = None
if 'history' not in st.session_state:
    st.session_state.history = []

# Main Tab: Recommendation
with tabs[0]:
    movie_input = st.text_input("Search for a movie to get recommendations:")
    matched_movie = get_best_match(movie_input, movies['title'].values) if movie_input else None

    if matched_movie:
        if st.button("Recommend"):
            raw_recs = hybrid_recommend(matched_movie)
            if raw_recs is None:
                st.error("Movie not found in database.")
            else:
                recs = []
                for rec in raw_recs:
                    poster, rating, genres, overview, release_date = fetch_movie_details(rec['movie_id'])
                    if poster != "No Poster":
                        recs.append({
                            "title": rec['title'],
                            "movie_id": rec['movie_id'],
                            "poster": poster,
                            "rating": rating,
                            "genres": genres,
                            "overview": overview,
                            "release_date": release_date
                        })
                if not recs:
                    st.warning("No valid movie posters could be retrieved. Please try a different movie.")
                    st.stop()
                st.session_state.recommendations = recs
                st.session_state.scroll_to = None

    if st.session_state.recommendations:
        recommendations = st.session_state.recommendations

        st.markdown("<div id='top'></div>", unsafe_allow_html=True)
        st.markdown("## 🎬 Top 10 Movie Recommendations")
        for i in range(0, len(recommendations), 5):
            row = recommendations[i:i+5]
            cols = st.columns(5)
            for j, rec in enumerate(row):
                with cols[j]:
                    st.image(rec['poster'], use_column_width=True)
                    if st.button(rec['title'], key=f"title_btn_{i+j}"):
                        st.session_state.scroll_to = i + j

        st.markdown("---")
        st.markdown("## 📄 Movie Details")

        for idx, rec in enumerate(recommendations):
            if st.session_state.scroll_to == idx:
                st.markdown("""
                <div style='border:2px solid #ccc; padding:20px; border-radius:10px; margin-bottom:20px; background-color: #f8f8f8;'>
                """, unsafe_allow_html=True)
                cols = st.columns([1, 3])
                with cols[0]:
                    st.image(rec['poster'], use_column_width=True)
                with cols[1]:
                    st.markdown(f"### {rec['title']}")
                    st.markdown(f"**Genres:** {rec['genres']}")
                    st.markdown(f"**Rating:** {rec['rating']} ⭐")
                    st.markdown(f"**Release Date:** {rec['release_date']}")
                    st.markdown(f"**Overview:** {rec['overview']}")
                    st.markdown(f"[🔗 View on TMDB](https://www.themoviedb.org/movie/{rec['movie_id']})", unsafe_allow_html=True)
                    if st.button("⬆️ Back to Top"):
                        st.session_state.scroll_to = None
                    if rec['title'] not in st.session_state.history:
                        st.session_state.history.insert(0, rec['title'])
                        st.session_state.history = st.session_state.history[:5]
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("---")

        if st.session_state.history:
            st.markdown("### 🕘 Recently Viewed Movies")
            st.markdown(", ".join(st.session_state.history))

    elif movie_input:
        st.warning("No close match found. Please try a different title.")

# Evaluation Tab
with tabs[1]:
    st.header("📊 Model Evaluation Dashboard (Simulated)")
    st.metric("Precision@10", f"{simulated_precision_at_k()*100:.0f}%")
    st.metric("Genre Coverage", f"{simulated_coverage()*100:.0f}%")
    st.metric("Diversity", f"{simulated_diversity()*100:.0f}%")
    st.markdown("### 🔥 Similarity Matrix Heatmap (Sample)")
    plot_similarity_heatmap()
