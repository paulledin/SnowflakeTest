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
    retVal = session.sql("SELECT substr(TABLE_NAME, 21, 26) as \"period\" FROM monthly_report.information_schema.tables WHERE table_schema = 'BOTH' and TABLE_NAME like 'AFL_TABLE_1_BYSTATE_%' ").to_pandas()
    
    return retVal

report_periods = get_report_periods_fromDB()
st.write(report_periods)




