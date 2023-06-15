import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/Photo.jpg")
with col2:
    st.title("Anthony Korepanov")
    st.info("Hi, I am Anthony! I am a Python Programmer")

st.write("Below you can find some of the apps I have built in Python."
         " Feel free to contact me!")

col3,col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")