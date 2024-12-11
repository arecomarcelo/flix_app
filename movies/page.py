import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from movies.service import MovieService
from genres.service import GenreService
from actors.service import ActorService

from datetime import datetime


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    genre_service = GenreService()
    genres = genre_service.get_genres()
    genre_names = {genre['name']: genre['id'] for genre in genres}

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actors_names = {actor['name']: actor['id'] for actor in actors}

    if movies:
        st.write('Lista de Filmes')

        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'gender.id'])

        AgGrid(
            data = movies_df,#pd.DataFrame(movies_df),
            reload_data = True,
            key='movies_grid',
            height= 250,
        )
    else:
        st.warning('Nenhum Filme Cadastrado!')

    st.title('Cadastrar Novo Filme')
    title = st.text_input('Nome do Filme')
    release_date = st.date_input(
        label='Data de Lançamento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
        )
    selected_gender_name = st.selectbox('Gênero', list(genre_names.keys()))
    selected_actors_names = st.multiselect('Atores/Atrizes', list(actors_names.keys()))
    selected_actors_ids = [actors_names[name] for name in selected_actors_names]
    resume = st.text_area(label='Resumo')
    
    if st.button('Cadastrar'):
        new_movie = movie_service.create_movies(
                title=title,
                release_date=release_date,
                gender=genre_names[selected_gender_name],
                actors=selected_actors_ids,
                resume=resume,
            )

        if new_movie:
            st.rerun()
        else:
            st.error('Erro ao Cadastrar o Filme. Verifique os Dados!')        