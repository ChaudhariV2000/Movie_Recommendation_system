import streamlit as st
import pickle
import requests
import  os
import  gdown
@st.cache_resource
def download_if_missing():
    files = {
        "movies_ved.pkl": "https://drive.google.com/uc?id=12-i0lHt3jyxPk6bc9ASXrQ1ydgdmQvz6",
        "similarity.pkl": "https://drive.google.com/uc?id=1kIxYqNYzZI9JhmEjZruoQUU-hF3Tro8q",
         }

    for filename, url in files.items():
        if not os.path.exists(filename):
            gdown.download(url, filename, quiet=False)

def fetchPoser(movie_id):
    res=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5d3b3a6453491bec997217afe8ba01f5&language=en-US'.format(movie_id))
    data=res.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']
def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies=[]
    recommended_movie_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movie_poster.append(fetchPoser(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,recommended_movie_poster


download_if_missing()
movies=pickle.load(open('movies_ved.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies_list=movies['title'].values

st.title('Movie Recommendation System by Vedant')
option=st.selectbox('How would  you like to contacted',movies_list)

if st.button('Recommemd'):
    # st.write(option)
    name,poster=recommend(option)


    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(name[0])
        st.image(poster[0])
    with col2:
        st.text(name[1])
        st.image(poster[1])
    with col3:
        st.text(name[2])
        st.image(poster[2])
    with col4:
        st.text(name[3])
        st.image(poster[3])
    with col5:
        st.text(name[4])
        st.image(poster[4])

