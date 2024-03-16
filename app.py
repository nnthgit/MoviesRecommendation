
import streamlit as st
import pickle

# On charge la BD
movies_list = pickle.load( open("movies.pkl" , "rb" ) )


# On charge la BD
similarity = pickle.load( open("similarity.pkl" , "rb" ) )

def recommend(movie) :
    movie_index = movies_list[ movies_list["title"] == film ].index[0]
    distances = similarity[movie_index]
    movie_list = sorted( list(enumerate (distances)  ), reverse=True , key = lambda x : x[1])[1:6]

    recommandations = []
    for i in movie_list:
        recommandations.append( movies_list["title"] [ i[0] ] ) # i est un tuple (id,distance)

    return recommandations




st.title("Système de Recommandation de films")

film = st.selectbox( ("Choisissez un film") , movies_list["title"].values )


if st.button( "Recommandation" ):
    st.write(  "Voici les 5 meilleurs recommandation pour le film  " ,"'" , film , "'")
    re = recommend(film)
    for i in re:
        st.write( i )

