import streamlit as st
import plotly_express as px
import pandas as pd
import time
import plotly.graph_objects as go
import webbrowser

from pghunter import get_full_data

st.set_page_config(
	page_title="PGHunter",
	layout='wide')

hide_streamlit_style = """
            <style>
            
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

#ALIGN TITLE IN CENTER
st.markdown("<h1 style='text-align: center;'>Are you a...</h1>", unsafe_allow_html=True) 
st.write("###")
st.write("###")
st.write("###")
st.write("###")
st.write("###")
st.write("###")
st.write("###")

c1,c2,c3,c4=st.columns((1.5,2,2,0.5))

with c2:
	hunt=st.button("PG Accomodation Hunter?")
	if(hunt):
		webbrowser.open("http://localhost:8501/Hunters")

with c3:
	own=st.button("PG Accomodation Owner?")
	if(hunt):
		webbrowser.open("http://localhost:8501/Owners")