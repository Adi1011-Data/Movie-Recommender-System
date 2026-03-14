# Movie Recommender System
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Model File
The trained model file `similarity.pkl` is not included in this repository 
because it exceeds GitHub's file size limit.
To generate them:
   -Open the notebook movie_recommender.ipynb.
   -Run all the cells in the notebook.
   -At the final step, the notebook will create the required .pkl files inside the models folder.
   -After the models are generated, you can run the Flask application.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
A content-based movie recommendation system built using Python and Flask.

The application recommends similar movies based on their features such as genres, keywords, cast, crew, and movie overview.
Users can search for a movie and receive the top recommended movies based on similarity scores.

Features:

-Movie search functionality
-Autocomplete movie suggestions while typing
-Top 5 movie recommendations
-Interactive dark themed UI
-Flask-based web dashboard

Fast recommendation using precomputed similarity matrix

1. Project Folder Structure
   movie-recommender-system/
   │
   ├── data/
   │ ├── movies.csv
   │ └── ratings.csv
   │
   ├── notebooks/
   │ └── recommender.ipynb
   │
   ├── src/
   │ ├── data_loader.py
   │ ├── model.py
   │ └── recommend.py
   │
   ├── models/
   │ └── similarity.pkl
   │
   ├── app.py
   ├── requirements.txt
   └── README.md

2. Install Requirements
   pip install -r requirements.txt

3. Dataset
   This project uses the TMDB 5000 Movie Dataset.
   kaggle dataset link: https://www.kaggle.com/code/himanshukumar7079/tmdb-5000-movie-dataset

   Key columns used:

   tmdb_5000_movies.csv:
   1.movie_id
   2.title
   3.overview
   4.genres
   5.keywords
   tmdb_5000_credits.csv:
   1.title
   2.cast
   3.crew

   These datasets are merged to build the final movie feature set.

4.Machine Learning Approach

    The project uses Content-Based Filtering.

    Steps used in the recommendation pipeline:

    -Merge movies and credits datasets
    -Select relevant features
    -Clean and preprocess text data
    -Extract important information such as:
        -genres
        -keywords
        -top cast members
        -director
    -Combine these features into a single column called tags
    -Convert text data into vectors using CountVectorizer
    -Compute cosine similarity between movie vectors
    -Recommend movies with highest similarity scores

    Cosine similarity measures how similar two movie vectors are.

5.Recommendation Pipeline

    Dataset Loading
    ↓
    Data Cleaning
    ↓
    Feature Extraction
    ↓
    Tag Creation
    ↓
    Text Vectorization
    ↓
    Similarity Matrix Calculation
    ↓
    Model Saving (Pickle)
    ↓
    Flask Web Application

6.  Model Files

    The trained data is saved using pickle.

    movies.pkl
    Contains the processed movie dataset.

    similarity.pkl
    Contains the cosine similarity matrix.

    These files allow the web app to generate recommendations instantly without retraining.

7.  Installation

    Clone the repository

         git clone

    Navigate into the project directory

         cd movie-Recommender-system

    Create a virtual environment

         python -m venv MovieRecommender

    Activate the virtual environment

    Windows:
    MovieRecommender\Scripts\activate

    Install dependencies

         pip install -r requirements.txt

8.  Learning Outcomes

This project demonstrates:

    Building a recommender system
    Feature engineering for NLP data
    Vectorization of text data
    Similarity based recommendation algorithms
    Backend development using Flask
    Building a simple web interface for machine learning models
