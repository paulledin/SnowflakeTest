# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:01:23 2024

@author: PLedin
"""

# streamlit_app.py

import streamlit as st
import pandas as pd

conn = st.connection("pets")

def get_report_periods_fromDB():
    session = conn.session()
    return session.table("mytable").to_pandas()

@st.cache_data
def load_table():
    session = conn.session()
    return session.table("mytable").to_pandas()

df = load_table()

for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")

report_periods = get_report_periods_fromDB()
st.write(report_periods)




