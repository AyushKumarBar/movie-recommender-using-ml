import pickle
import pandas as pd
import streamlit as st
import requests
import zipfile
import io


def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=<Your API Key>&language=en-US'.format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    overview = data['overview']
    poster_path = data['poster_path']
    full_path = 'https://image.tmdb.org/t/p/w500/' + poster_path
    return full_path, overview


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_overview = []
    for i in distances[1:7]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        poster, overview = fetch_poster(movie_id)
        recommended_movie_posters.append(poster)
        recommended_movie_overview.append(overview)
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_overview


st.header('Movie Recommendations')

zip_file_path = 'data.zip'
file_name_1 = 'pickle.zip'

with open(zip_file_path, 'rb') as zip_file:
    # Create a ZipFile object
    with zipfile.ZipFile(io.BytesIO(zip_file.read()), 'r') as zip_ref:
        # Extract the specific ZIP file into memory
        with zip_ref.open(file_name_1) as extracted_zip:
            # Create a new ZipFile object for the extracted ZIP file
            with zipfile.ZipFile(io.BytesIO(extracted_zip.read()), 'r') as extracted_zip_ref:
                # Extract the pickle files into memory
                with extracted_zip_ref.open('similarity.pkl') as similarity_pickle, \
                        extracted_zip_ref.open('movie_dict.pkl') as movie_dict_pickle:
                    # Load the pickle data
                    similarity = pickle.load(similarity_pickle)
                    movies_dict = pickle.load(movie_dict_pickle)

movies = pd.DataFrame(movies_dict)

selected_movie = st.selectbox(
    "Select movie:",
    movies['title'].values
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, recommended_movie_overview = recommend(selected_movie)
    col1, col2, col3, col4 = st.columns(4, gap="small")
    with col1:
        st.subheader(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text('Overview:')
        st.caption(recommended_movie_overview[0])

    with col3:
        st.subheader(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col4:
        st.text('Overview:')
        st.caption(recommended_movie_overview[1])

    col5, col6, col7, col8 = st.columns(4, gap="small")

    with col5:
        st.subheader(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col6:
        st.text('Overview:')
        st.caption(recommended_movie_overview[2])

    with col7:
        st.subheader(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col8:
        st.text('Overview:')
        st.caption(recommended_movie_overview[3])

    col9, col10, col11, col12 = st.columns(4, gap="small")

    with col9:
        st.subheader(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col10:
        st.text('Overview:')
        st.caption(recommended_movie_overview[4])

    with col11:
        st.subheader(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])

    with col12:
        st.text('Overview:')
        st.caption(recommended_movie_overview[5])
