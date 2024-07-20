import streamlit as st
import pickle
import pandas as pd
import requests

# Load the data
movies_data = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_data)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Fetch poster from The Movie Database (TMDb)
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=2f3dbb17d5fe162e20f05d2759b622a2&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_rcm = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_rcm:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        # recommended_movies_posters.append(fetch_poster(movie_id=movie_id))
    return recommended_movies

# Streamlit UI
st.title("Movie Recommender System")

select_movie_name = st.selectbox("Search your Movie", movies['title'].values)

if st.button('Recommend'):
    names = recommend(select_movie_name)
    
    for  name in names:
            # st.image(poster)
            st.text(name)
