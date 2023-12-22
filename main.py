import tkinter as tk
from tkinter import messagebox
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd


movies_data = [
    {"title": "The Shawshank Redemption", "genres": "Drama"},
    {"title": "The Godfather", "genres": "Crime, Drama"},
    {"title": "The Dark Knight", "genres": "Action, Crime, Drama"},
    {"title": "Pulp Fiction", "genres": "Crime, Drama"},
    {"title": "The Lord of the Rings: The Return of the King", "genres": "Action, Adventure, Drama"},
    {"title": "Forrest Gump", "genres": "Drama, Romance"},
    {"title": "The Matrix", "genres": "Action, Sci-Fi"},
    {"title": "Inception", "genres": "Action, Adventure, Sci-Fi"},
    {"title": "The Silence of the Lambs", "genres": "Crime, Drama, Thriller"},
    {"title": "Titanic", "genres": "Drama, Romance"},
]


movies = pd.DataFrame(movies_data)


window = tk.Tk()
window.title("Movie Recommender")


label = tk.Label(window, text="Enter your favorite movie:")
entry = tk.Entry(window)
button = tk.Button(window, text="Get Recommendations", command=lambda: recommend_movies(entry.get()))

label.pack(pady=10)
entry.pack(pady=10)
button.pack(pady=10)

def recommend_movies(user_input):

    count_vectorizer = CountVectorizer()
    genre_matrix = count_vectorizer.fit_transform(movies['genres'].fillna(''))




    cosine_sim = cosine_similarity(genre_matrix, genre_matrix)


    input_movie_index = movies[movies['title'].str.lower() == user_input.lower()].index[0]


    sim_scores = list(enumerate(cosine_sim[input_movie_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    print(genre_matrix.toarray())
    print(sim_scores)

    recommended_movies = [movies['title'][i[0]] for i in sim_scores]
    messagebox.showinfo("Recommended Movies", "\n".join(recommended_movies))


window.mainloop()
