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

```
├── app.py                   # Streamlit web application
├── model.ipynb              # Colab notebook (training/preprocessing)
├── movie_data.pkl           # Pickled movie metadata + similarity matrix
├── collab_scores.pkl        # Precomputed collaborative filtering scores
├── .env                     # TMDB API key (not committed)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ Installation

### ✅ Prerequisites

- Python 3.8+
- TMDB API Key (get from https://www.themoviedb.org/documentation/api)

### 🔧 Setup

```bash
# 1. Clone the repo
git clone https://github.com/2201AI24/Hybrid_Movie_Recommendation_System.git
cd Hybrid_Movie_Recommendation_System

# 2. Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your TMDB API key
echo "TMDB_API_KEY=your_api_key_here" > .env

# 5. Run the app
streamlit run app.py
```

---

## 🧠 How It Works

1. **Content-Based Filtering**  
   - Computes cosine similarity between movies based on genres, overview, and other metadata.  

2. **Collaborative Filtering**  
   - Uses precomputed user-item ratings for recommending movies liked by similar users.  

3. **Hybrid Score Calculation**  
   final score = (α)⋅content similarity + (1−α)⋅collaborative score

4. **TMDB Integration**  
   - Fetches movie posters, genres, overviews, and release dates using TMDB API.

---

## 📊 Simulated Evaluation Metrics

- 🎯 **Precision@10:** How often relevant recommendations appear in top 10.  
- 🎬 **Genre Coverage:** Diversity of genres across recommendations.  
- 🌈 **Diversity:** How varied the suggested movies are.  

> These metrics are currently simulated for demonstration purposes.

---

## 📸 Screenshots
![image_1](https://github.com/user-attachments/assets/8ef07367-99b4-40d5-b950-076c3ab08ed4)
![image_2](https://github.com/user-attachments/assets/4a9d3409-cf82-44b2-a103-4340431263b6)
![image_4](https://github.com/user-attachments/assets/0e59ed3f-a6a1-487a-ab91-0bfa9151d46f)


---

## 📚 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python  
- **Data**: Pandas, NumPy, Pickle  
- **Visualization**: Seaborn, Matplotlib  
- **API**: TMDB (The Movie Database)  
- **Similarity**: Scikit-learn  
- **Other**: dotenv, difflib (fuzzy matching)  

---

## 🚀 Future Enhancements

- Replace simulated evaluation with real user-based metrics  
- Add login and profile-based history  
- Improve collaborative filtering using `Surprise` or `LightFM`  
- Filter by genre, language, or release year  
- Support multilingual metadata from TMDB  

---

## 🙌 Acknowledgments

- [TMDB API](https://www.themoviedb.org/documentation/api) for movie metadata  
- Open-source contributors and recommendation system research  

---

## 📬 Contact

**Metla Umesh Chandra**  
Email: metlaumeshchandra2005@example.com  
GitHub: [@2201AI24](https://github.com/your-username)  

---

> ⚠️ This is an academic project intended for learning purposes. TMDB API usage must comply with their terms and branding guidelines.
