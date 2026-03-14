import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

movies = pickle.load(open("models\movies.pkl","rb"))
similarity = pickle.load(open("models\similarity.pkl","rb"))

movie_list = movies['title'].values.tolist()


def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x:x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


@app.route("/")
def home():
    return render_template("index.html")


# suggestion API
@app.route("/suggest")
def suggest():

    query = request.args.get("q")

    suggestions = [m for m in movie_list if query.lower() in m.lower()][:5]

    return jsonify(suggestions)


# recommendation API
@app.route("/recommend")
def recommend_api():

    movie = request.args.get("q")

    recs = recommend(movie)

    return jsonify(recs)


if __name__ == "__main__":
    app.run(debug=True)
