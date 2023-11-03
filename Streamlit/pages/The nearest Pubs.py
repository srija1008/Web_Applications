from email.headerregistry import Address
import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
st.header('Lets have some drinks :beers:and fun :sunglasses: to night')

st.sidebar.markdown('**Here are Nearest five Pubs based on user enter  Latitude and longitude**')
df = pd.read_csv('data/pubs.csv')

 
# Calculate the Euclidean distance
# between two points
def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** ( 1 / 2)
 
# Function to calculate K closest points
def kClosest(points, target, K):
    pts = []
    n = len(points)
    d = []
 
    for i in range(n):
        d.append({
            "first": distance(points[i][0], points[i][1], target[0], target[1]),
            "second": i
        })
    
    
     
    d = sorted(d, key=lambda l:l["first"])
    
    for i in range(K):
        pt = []
        pt.append(points[d[i]["second"]][0])
        pt.append(points[d[i]["second"]][1])
        pts.append(pt)
    df_nearest_loc = pd.DataFrame(pts,columns=['latitude','longitude'])
    st.map(df_nearest_loc)
    
df_lat_log=df[['latitude','longitude']]
points = df_lat_log.values.tolist()

lat = st.sidebar.number_input('Your Latitude',format="%.5f")
log = st.sidebar.number_input('Your Longitude',format="%.6f",key=int)

target = [lat,log]
K = 5

kClosest(points, target, K)
