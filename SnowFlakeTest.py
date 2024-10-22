# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:01:23 2024

@author: PLedin
"""

# streamlit_app.py

import streamlit as st

# Initialize connection.
conn = st.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from mytable;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.NAME} has a :{row.PET}:")
