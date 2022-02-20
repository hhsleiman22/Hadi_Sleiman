from operator import index
from re import T
import pandas as pd

import pandas as pd
import numpy as np
import scipy as sp
import plotly.express as px
import matplotlib as plt
import streamlit as st


st.set_page_config(page_title="World Cup",page_icon=":soccer:",layout="wide")




header=st.container()
data=st.container()

with header:
    st.title("Welcome to Hadi's webpage :relaxed:")
    st.markdown("We will analyze the World Cup tournaments throughout the years!")
with data:
    st.header("This is our dataset")
  
url = "https://drive.google.com/file/d/1axUsUMkVujv053-NIsJjdZvL1Rjkqzv4/view?usp=sharing"

path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]

worldcup = pd.read_csv(path)


st.write(worldcup)

st.header("Attendance in each Country")
st.markdown("In the below interactive visualization we will see where did the world cup happen and how many people attended and how many goals were scored")
fig2 = px.bar(worldcup, x="Country", y="Attendance", color="GoalsScored",
  animation_frame="Year", animation_group="Country", range_y=[0,4000000])
st.write(fig2)

st.sidebar.header('Filter :')
country=st.sidebar.multiselect("Select the Country:",options=worldcup["Country"].unique())



cs= worldcup.query("Winner== @country")
cs.reset_index(drop=True, inplace=True) 
st.title(":soccer: World Cup")
st.subheader(":arrow_left: Please use the filter to check each country ")
st.markdown("##")
Trophies= cs["Winner"].count()
Years=cs["Year"]

left_column, middle_column= st.columns(2)
with left_column:
    st.subheader("Number of Trophies : :trophy:")
    
    st.subheader(Trophies)
    
with middle_column:
     st.subheader("Won in ::date:")
     st.subheader(list(Years))
    
    
    

st.header("Geographic map ")
st.subheader("You forgot where is the winner country located? Go ahead and search for it! :point_down:")



fig1= px.choropleth_mapbox(worldcup, geojson="Country", color='Winner', range_color=(0, 12), mapbox_style="carto-positron",zoom=3, center = {"lat": 37.0902, "lon": -95.7129},labels={'Winner':'Winners'})
fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

st.write(fig1= px.choropleth_mapbox(worldcup, geojson="Country", color='Winner', range_color=(0, 12), mapbox_style="carto-positron",zoom=3, center = {"lat": 37.0902, "lon": -95.7129},labels={'Winner':'Winners'}))

st.write(fig1.update_layout(margin={"r":0,"t":0,"l":0,"b":0}))



