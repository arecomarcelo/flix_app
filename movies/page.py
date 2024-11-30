import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


movies = [
    {
        'id': 1,
        'name': 'Titanic'
    },
    {
        'id': 2,
        'name': 'Star Wars'
    },
    {
        'id': 3,
        'name': 'De Volta para o Futuro'
    },
]
def show_movies():
    st.write('Lista de Filmes')

    AgGrid(
        data = pd.DataFrame(movies),
        reload_data = True,
        key='movies_grid',
    )