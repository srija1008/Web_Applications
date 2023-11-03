import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Welcome to pubs :wine_glass: in UK')
image = Image.open('data/pub.png')

st.image(image)
df = pd.read_csv('data/pubs.csv')
option = st.sidebar.selectbox(" ", 
                     ('Some Statistical info','Top 5 rows','Last 5 rows','check null values','shape'))
st.subheader('Total  no.of pubs in UK: {}'.format(df.shape[0]))                   
if option =='Some Statistical info':
    st.subheader("Some Statistical information")
    st.dataframe(df.describe())                    
elif option == 'Top 5 rows':
    st.subheader("Top 5 rows")
    st.dataframe(df.head()) 
elif option =='Last 5 rows':
     st.subheader("Last 5 rows")
     st.dataframe(df.tail())
elif option =='Some Statistical info':
     st.subheader("Some Statistical information")
     st.dataframe(df.describe())                            
elif option =='check null values':
     st.subheader('we will see that there are no null values in our dataset')
     st.dataframe(df.isna().sum())
elif option =='shape':
     st.subheader("Total no.of rows and columns")
     st.markdown('**Number of rows:** {}'.format(df.shape[0]))
     st.markdown('**Number of Columns:** {}'.format(df.shape[1]))
