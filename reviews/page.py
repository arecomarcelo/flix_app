import streamlit as st
from st_aggrid import AgGrid
import pandas as pd


reviews = [
    {
        'id': 1,
        'stars': 5
    },
    {
        'id': 2,
        'stars': 3
    },
    {
        'id': 3,
        'stars': 2
    },
]
def show_reviews():
    st.write('Lista de Avaliações')

    AgGrid(
        data = pd.DataFrame(reviews),
        reload_data = True,
        key='reviews_grid',
    )