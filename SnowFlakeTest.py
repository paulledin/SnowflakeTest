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

    #retVal = session.table("monthly_report.information_schema.tables").to_pandas()
    retVal = session.sql("select * from monthly_report.information_schema.tables").to_pandas()
    
    return retVal

#SELECT TABLE_NAME, length(TABLE_NAME), substr(TABLE_NAME, 21, 26) 
#FROM monthly_report.information_schema.tables 
#WHERE table_schema = 'BOTH' and TABLE_NAME like 'AFL_TABLE_1_BYSTATE_%';

report_periods = get_report_periods_fromDB()
st.write(report_periods)




