import streamlit as st


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

    st.table(genres)

    st.title('Cadastrar Novo Gênero')
    name = st.text_input('Nome do Gênero')
    
    if st.button('Cadastrar'):
        if name == 'Sexo':
            st.error(f'O Gênero {name} não é Permitido!')
        else:
            st.success(f'Genêro {name} - Cadastrado com Sucesso!')