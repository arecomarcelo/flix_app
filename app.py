import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from login.page import show_login


def main():


    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix App')
        
        menu_options = st.sidebar.selectbox(
            'Selecione uma Opção:',
            ['',
            'Início',
            'Gêneros',
            'Atores/Atrizes',
            'Filmes',
            'Avaliações'
            ]
        )

        if menu_options == 'Início':
            st.write('Início')

        if menu_options == 'Gêneros':
            show_genres()
        
        if menu_options == 'Atores/Atrizes':
            show_actors()
        
        if menu_options == 'Filmes':
            show_movies()
        
        if menu_options == 'Avaliações':
            show_reviews()
    
if __name__ == '__main__':
    main()
