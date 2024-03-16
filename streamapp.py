import streamlit as st
import pickle

# Load the movie database
movies_list = pickle.load(open("movies.pkl", "rb"))

# Load the similarity data
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommend(movie_title):
    try:
        movie_index = movies_list[movies_list["title"] == movie_title].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommendations = []
        for i in movie_list:
            recommendations.append(movies_list["title"][i[0]])  # i is a tuple (id, distance)

        return recommendations
    except IndexError:
        return []

st.title("Movie Recommendation System")

selected_movie = st.selectbox("Choose a movie:", movies_list["title"].values)

if st.button("Get Recommendations"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.write(f"Top 5 recommendations for '{selected_movie}':")
        for movie in recommendations:
            st.write(movie)
    else:
        st.write("Movie not found or no recommendations available.")
