import sys
import streamlit as st
import pandas as pd
import pickle
import warnings

import gdown
import os

# Corrected Google Drive URL using file ID
file_id = '1-gA4Ufds45H6LJCsSaOaq9Al15lbMthv'
url = f'https://drive.google.com/uc?id={file_id}'

# Download only if not present
if not os.path.exists('similarity.pkl'):
    gdown.download(url, 'similarity.pkl', quiet=False)

# Load data
with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

def recommend(movie):
    movie_index= movies[movies['title']== movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommend_movies=[]
    for i in movies_list:
        movie_id=i[0]
        #fetch poster from api
        
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies
    
   
        

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
# movies_list=movies_list['title'].values
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')


selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)


if st.button("Recommend"):
    recommendations= recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
# else:
#     st.write("Goodbye")

# if st.button("Aloha", type="tertiary"):
#     st.write("Ciao")



# st.write("You selected:", option)

# import sys
# print("warnings" in sys.modules)
# print(movies_dict)

