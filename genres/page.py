import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from genres.service import GenreService


def show_genres():
    genre_service = GenreService()
    genres = genre_service.get_genres()

    if genres:
        st.write('Lista de Gêneros')

        genres_df = pd.json_normalize(genres)

        AgGrid(
            data = pd.DataFrame(genres_df),
            reload_data = True,
            key='genres_grid',
            height= 250,
        )
    else:
        st.warning('Nenhum Gênero Cadastrado!')

    st.title('Cadastrar Novo Gênero')
    name = st.text_input('Nome do Gênero')
    
    if st.button('Cadastrar'):
        new_genre = genre_service.create_genres(
                name=name,
            )

        if new_genre:
            st.rerun()
        else:
            st.error('Erro ao Cadastrar o Gênero. Verifique os Dados!')