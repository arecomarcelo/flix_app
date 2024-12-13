import streamlit as st
import plotly.express as px
from movies.service import MovieService
import pandas as pd
from st_aggrid import AgGrid


def show_home():
    movie_service = MovieService()
    movies_stats = movie_service.get_movie_stats()
    
    st.title('Estatísticas de Filmes')

    if len(movies_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Gênero')
        fig = px.pie(
            movies_stats['movies_by_genre'],
            values='total',
            names='gender__name',
            # title='Filmes por Gênero',
        )

        st.plotly_chart(fig)

    st.subheader('Total de Filmes Cadastrados:')
    st.write(movies_stats['total_movies'])

    st.subheader('Total de Filmes por Gênero:')
    movies_list = []

    for genre in movies_stats['movies_by_genre']:
        # st.write(f"{genre['gender__name']}: {genre['total']}")
        
        dado = {
            'genero': genre['gender__name'],
            'total': genre['total']
        }
        movies_list.append(dado)

    movies_df = pd.DataFrame(movies_list)

    AgGrid(
        data=movies_df,
        reload_data=True,
        key='movies_grid',
        height=150,
    )        

    st.subheader('Total de Avaliações Cadastradas:')
    st.write(movies_stats['total_reviews'])
    
    st.subheader('Média Geral de Estrelas nas Avaliações:')
    st.write(movies_stats['average_stars'])