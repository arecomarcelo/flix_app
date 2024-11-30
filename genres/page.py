import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


genres = [
    {
        'id': 1,
        'name': 'Ação'
    },
    {
        'id': 2,
        'name': 'Comédia'
    },
    {
        'id': 3,
        'name': 'Terros'
    },
]
def show_genres():
    st.write('Lista de Gêneros')

    AgGrid(
        data = pd.DataFrame(genres),
        reload_data = True,
        key='genres_grid',
    )

    st.title('Cadastrar Novo Gênero')
    name = st.text_input('Nome do Gênero')
    
    if st.button('Cadastrar'):
        if name == 'Sexo':
            st.error(f'O Gênero {name} não é Permitido!')
        else:
            st.success(f'Genêro {name} - Cadastrado com Sucesso!')