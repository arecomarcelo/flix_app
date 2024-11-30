import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


actors = [
    {
        'id': 1,
        'name': 'Leonardo de Caprio'
    },
    {
        'id': 2,
        'name': 'Chris Rock'
    },
    {
        'id': 3,
        'name': 'Stalone'
    },
]
def show_actors():
    st.write('Lista de Atores/Atrizes')

    AgGrid(
        data = pd.DataFrame(actors),
        reload_data = True,
        key='actors_grid',
    )

    st.title('Cadastrar Novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    
    if st.button('Cadastrar'):
            st.success(f'Ator/Atriz {name} - Cadastrado(a) com Sucesso!')