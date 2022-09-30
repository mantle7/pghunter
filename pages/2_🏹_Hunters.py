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

st.sidebar.header("Select your accomodation preferences...")

# win=st.sidebar.selectbox("City",)
# attr=st.sidebar.multiselect('Attributes',options=attributes,default=attributes)

df,title_df=get_full_data()
df=df.drop(df.columns[0],axis='columns')

df=pd.concat([title_df,df],axis='columns')

dict1={2:"Food Included",0:"Food not Included",1:"Food Charge extra"}
df.food=df.food.replace(dict1)

city=st.sidebar.selectbox("City",df['city'].unique().tolist())
sub_df=df[df['city']==city]

l=sorted(sub_df['locality'].unique().tolist())
# l_upper = [name.upper() for name in l]
locality=st.sidebar.selectbox("Locality",l)

df1=df[df['city']==city]
df2=df1[df1['locality']==locality]

df2=df2.drop(['city','locality'],axis='columns')
df2=df2.drop_duplicates()

df2=df2.reset_index(drop=True)

st.dataframe(df2)

# locality=st.sidebar.multiselect('Locality')