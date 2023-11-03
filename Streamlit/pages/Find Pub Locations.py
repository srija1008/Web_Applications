import streamlit as st
import pandas as pd
import numpy as np
st.title('Pub :cocktail: locations')
df = pd.read_csv('data/pubs.csv')
local=df.local_authority.unique()
option=st.sidebar.selectbox('',local)
"you're selected :" ,option
ntp=df[df['local_authority']==option]
ntp=ntp[['latitude','longitude']]
st.map(ntp)