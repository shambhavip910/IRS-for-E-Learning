# IRS for E-Learning Platforms

An Intelligent Recommendation System (IRS) that suggests relevant courses to users on an e-learning platform, combining **content-based filtering** and **collaborative filtering** approaches.

## Overview

This project analyzes course metadata and user interaction data to recommend courses that a learner is likely to be interested in. It uses:

- **Content-Based Filtering** — recommends courses similar to ones a user has already engaged with, based on course content (e.g., title, description, tags) using TF-IDF vectorization and cosine similarity.
- **Collaborative Filtering** — recommends courses based on patterns across similar users' interactions and preferences.

A Streamlit web app is included to interact with the recommendation system through a simple UI.

## Project Structure

```
├── E-learning.ipynb              # Main notebook: data cleaning, model building, experimentation
├── clean_courses.csv             # Cleaned course dataset
├── research_courses.csv          # Raw/research course dataset
├── research_interactions.csv     # User-course interaction data
├── research_users.csv            # User dataset
├── tfidf.pkl                     # Saved TF-IDF vectorizer
├── course_indices.pkl            # Course index mapping
├── courses.pkl                   # Processed course data
├── streamlit_1/
│   ├── app.py                    # Streamlit app entry point
│   ├── config.py                 # App configuration
│   ├── content_based.py          # Content-based recommendation logic
│   ├── generate_interactions.py  # Script to generate synthetic interaction data
│   ├── generate_user_similarity.py  # Script to generate user similarity matrix
│   └── test.py                   # Test/experiment script
└── .gitignore
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/shambhavip910/IRS-for-E-Learning.git
   cd IRS-for-E-Learning
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` isn't present yet, install the core libraries manually: `pandas`, `numpy`, `scikit-learn`, `streamlit`)*

3. **Regenerate large similarity files** (excluded from the repo due to GitHub's file size limits)

   Two files — `cosine_similarity.pkl` and `user_similarity.pkl` — are **not included** in this repo because they exceed GitHub's 100MB file limit. Regenerate them locally before running the app:
   ```bash
   python streamlit_1/generate_user_similarity.py
   ```
   For `cosine_similarity.pkl`, run the relevant cell(s) in `E-learning.ipynb` or the corresponding function in `content_based.py`.

4. **Run the Streamlit app**
   ```bash
   cd streamlit_1
   streamlit run app.py
   ```

## How It Works

1. Course text data (titles, descriptions) is vectorized using **TF-IDF**.
2. **Cosine similarity** is computed between course vectors to power content-based recommendations.
3. User interaction data is used to build a **user similarity matrix** for collaborative filtering.
4. The Streamlit app lets users select a course or profile and view personalized recommendations.

## Notes

- `cosine_similarity.pkl` and `user_similarity.pkl` are intentionally excluded from version control (see `.gitignore`) as they are large, regeneratable artifacts rather than source files.
- Data files (`research_*.csv`) are used for experimentation; `clean_courses.csv` is the processed dataset used by the app.

## Author

Shambhavi
