import streamlit as st
import requests

st.title("Netflix Movie Recommender")

user_id = st.number_input("USER ID", 1)
movie = st.text_input("Movie Name")
if st.button("Recommend"):
    res = requests.get(
        f"http://localhost:8000/recommend?user_id={user_id}&movie_name={movie}"
    )
    st.write(res.json())
    