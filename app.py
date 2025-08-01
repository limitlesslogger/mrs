import streamlit as st
import pickle
import pandas as pd
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)
st.title('Movie Reccomender System')
selected_movie_name=st.selectbox('What to watch?',movies['title'].values)
def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies_list:
        # movie_id=i[0]
        # fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
if st.button("Recommend"):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

