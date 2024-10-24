# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:01:23 2024

@author: PLedin
"""

# streamlit_app.py

import streamlit as st
import pandas as pd

conn = st.connection("snowflake")

@st.cache_data
def get_report_periods_fromDB():
    session = conn.session()
    return session.table("monthly_report.either.afl_table_1_bystate_202409").to_pandas()





report_periods = get_report_periods_fromDB()
st.write(report_periods)




