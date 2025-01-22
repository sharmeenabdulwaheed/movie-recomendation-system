import streamlit as st
import pandas as pd
import pickle
import requests

st.title("Movie Recommendation System")
movies_dict=pickle.load(open("C:\\Users\\U$ER\Documents\\chat analysis\\movie_dict.pkl", "rb"))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open("C:\\Users\\U$ER\Documents\\chat analysis\\similarity.pkl", "rb"))

#def fetch_poster(movie_id):
    

    

def recommend(movie):
    movie_index=movies[movies["title"]== movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    for i in movie_list:
        movie_id=i[0]
        recommended_movies.append((movies.iloc[i[0]].title))
    return recommended_movies
    
option=st.selectbox("Enter the movie name: ", movies["title"].values)
if st.button("Recommend"):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)
