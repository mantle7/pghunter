import streamlit as st
import plotly_express as px
import pandas as pd
import time
import plotly.graph_objects as go
import webbrowser
import pickle
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

df,title_df=get_full_data()

city=st.selectbox("Select City:",df['city'].unique().tolist())

df2=df[df['city']==city]
l=sorted(df2['locality'].unique().tolist())
locality=st.selectbox("Locality",l)

food=st.selectbox("Food:",['Food Included','Food Cost Extra','Food Not Included'])

occupancy=st.selectbox("Occupancy:",['Boys','Girls','Coed'])

preferred=st.selectbox("Preferred:",['Students','Professional','Competitive Exams Aspirants','Anyone'])

metro=st.slider("Distance from nearest Metro Station:",0.0,10.0,step=0.1)

institution=st.slider("Distance from nearest Educational Institution:",0.0,10.0,step=0.1)

office=st.slider("Distance from nearest Office:",0.0,10.0,step=0.1)

# ['locality', 'food', 'educational_instituiton', 'office', 'metro',
#        'city', 'preferred_Competitive Aspirants', 'preferred_Professionals',
#        'preferred_Students', 'occupancy_for_Coed', 'occupancy_for_Girls']

if food=='Food Included':
	f=1
elif food=='Food Cost Extra':
	f=0
else:
	f=0

if preferred=='Students':
	f1=0
	f2=0
	f3=1
elif preferred=='Professional':
	f1=0
	f2=1
	f3=0
elif preferred=='Anyone':
	f1=0
	f2=0
	f3=0
else:
	f1=1
	f2=0
	f3=0

if occupancy=='Coed':
	f4=1
	f5=0
elif occupancy=='Girls':
	f4=0
	f5=1
else:
	f4=0
	f5=0

data=[locality,f,institution,office,metro,city,f1,f2,f3,f4,f5]

button=st.button("Click to predict approx. rent for your PG")

pickled_model=pickle.load(open('pghunter.pkl','rb'))
result=pickled_model.predict(data)
if(button):
	st.metric("The approx rent is:",round(result,3))



