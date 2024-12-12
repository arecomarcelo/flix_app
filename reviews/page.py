import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():

    review_service = ReviewService()
    reviews = review_service.get_reviews()

    movie_service = MovieService()
    movies = movie_service.get_movies()

    movie_titles = {movie['title']: movie['id'] for movie in movies}


    if reviews:
        st.write('Lista de Avaliações')

        reviews_df = pd.json_normalize(reviews)

        AgGrid(
            data = pd.DataFrame(reviews_df),
            reload_data = True,
            key='reviews_grid',
            height= 250,
        )
    else:
        st.warning('Nenhuma Avaliação Cadastrada!')

    st.title('Cadastrar Avaliação')
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas', 
        min_value=0, 
        max_value=5,
        step=1,
    )

    comment = st.text_area('Comentário')

    if st.button('Cadastrar'):
        new_review = review_service.create_reviews(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )

        if new_review:
            st.rerun()
        else:
           st.warning('Erro ao Cadastrar Avaliação. Verifique os Dados!') 


    