import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from actors.service import ActorService
from datetime import datetime

def show_actors():
    actor_service = ActorService()

    actors = actor_service.get_actors()

    if actors:
        st.write('Lista de Ator/Atriz')

        actors_df = pd.json_normalize(actors)

        AgGrid(
            data = pd.DataFrame(actors_df),
            reload_data = True,
            key='actors_grid',
            height= 250,
        )
    else:
        st.warning('Nenhum Ator/Atriz Cadastrado!')

    st.title('Cadastrar Novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
    birthday = st.date_input(
        label='Data de Nascimento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
        )
    nationality_dropdown = ['BR', 'USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )
    
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actors(
                name=name,
                birthday=birthday,
                nationality=nationality,
            )

        if new_actor:
            st.rerun()
        else:
            st.error('Erro ao Cadastrar o Ator/Atriz. Verifique os Dados!')