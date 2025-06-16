# 🎬 Hybrid Movie Recommendation System

A personalized movie recommender that blends content-based filtering and collaborative filtering to deliver smarter suggestions, with an interactive web interface built using Streamlit.

---

## 🔍 Overview

This project implements a **hybrid recommendation system** that combines the strengths of:

- ✅ Content-based filtering (using cosine similarity)
- ✅ Collaborative filtering (using precomputed user-movie scores)

It enriches user experience with movie posters, metadata, and overviews by integrating with **The Movie Database (TMDB) API**. Users can search for a movie, get top 10 recommendations, view detailed information, and see evaluation metrics in a visually appealing dashboard.

---

## 📌 Features

- 🔗 Hybrid recommender using content similarity + collaborative scores
- 🎯 Fuzzy title matching for better user search experience
- 🖼️ Dynamic posters, genres, overview, and rating via TMDB API
- 📊 Simulated evaluation metrics (Precision@10, Genre Coverage, Diversity)
- 🌐 Streamlit-based modern UI with dark mode toggle
- 🔥 Similarity heatmap visualization
- 🕘 Recently viewed history

---

## 📂 Project Structure

├── app.py # Streamlit web application
├── Project_2.ipynb # Colab notebook (training/preprocessing)
├── movie_data.pkl # Pickled movie metadata + similarity matrix
├── collab_scores.pkl # Precomputed collaborative filtering scores
├── .env # TMDB API key (not committed)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## ⚙️ Installation

### ✅ Prerequisites
- Python 3.8+
- TMDB API Key (get from https://www.themoviedb.org/documentation/api)

### 🔧 Setup

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/movie-recommender.git
cd movie-recommender

# 2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your TMDB API key
echo "TMDB_API_KEY=your_api_key_here" > .env

# 5. Run the app
streamlit run app.py
🧠 How It Works
Content-Based Filtering

Computes cosine similarity between movies based on genres, overview, and other metadata.

Collaborative Filtering

Uses precomputed user-item ratings for recommending movies liked by similar users.

Hybrid Score Calculation

final score
=
𝛼
⋅
content similarity
+
(
1
−
𝛼
)
⋅
collaborative score
final score=α⋅content similarity+(1−α)⋅collaborative score
TMDB Integration

Fetches movie posters, genres, overviews, and release dates using TMDB API.

📊 Simulated Evaluation Metrics
🎯 Precision@10: How often relevant recommendations appear in top 10.

🎬 Genre Coverage: Diversity of genres across recommendations.

🌈 Diversity: How varied the suggested movies are.

These metrics are currently simulated for demonstration purposes.

📸 Screenshots
Recommender Tab	Evaluation Dashboard

📚 Tech Stack
Frontend: Streamlit

Backend: Python

Data: Pandas, NumPy, Pickle

Visualization: Seaborn, Matplotlib

API: TMDB (The Movie Database)

Similarity: Scikit-learn

Other: dotenv, difflib (fuzzy matching)

🚀 Future Enhancements
Replace simulated evaluation with real user-based metrics

Add login and profile-based history

Improve collaborative filtering using Surprise or LightFM

Filter by genre, language, or release year

Support multilingual metadata from TMDB

🙌 Acknowledgments
TMDB API for movie metadata

Open-source contributors and recommendation system research

📬 Contact
Metla Umesh Chandra
Email: your_email@example.com
GitHub: @your-username

⚠️ This is an academic project intended for learning purposes. TMDB API usage must comply with their terms and branding guidelines.

vbnet
Copy
Edit

---

Let me know if you also want me to:
- Generate a `requirements.txt`
- Add `.gitignore`
- Help write a GitHub commit message or project description

✅ Just copy this full markdown text into your `README.md` file on GitHub. Let me know if you'd like to make it even fancier with badges or demo GIFs.







