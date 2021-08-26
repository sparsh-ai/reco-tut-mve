import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['Movie Name'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]]['Movie Name'])

    return recommended_movie_names

page_bg_img = '''
<style>
.stApp {
  background-image: url("https://payload.cargocollective.com/1/11/367710/13568488/MOVIECLASSICSerikweb_2500_800.jpg");
  background-size: cover;
}
</style>
'''

# st.markdown(page_bg_img, unsafe_allow_html=True)
# st.markdown(unsafe_allow_html=True)


st.header('Movie Recommendation System')
movies = pickle.load(open('./artifacts/imdb_movie_list.pkl','rb'))
similarity = pickle.load(open('./artifacts/imdb_cosine_similarity.pkl','rb'))

movie_list = movies['Movie Name'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        st.write(i)