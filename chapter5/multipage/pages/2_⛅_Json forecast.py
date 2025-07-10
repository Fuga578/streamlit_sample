#!/usr/bin/env python

from datetime import date
import requests
import streamlit as st

@st.cache_data
def get_json(today_dummy):
    url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json'
    headers = {'accept': 'application/json'}
    resp = requests.get(url, headers)
    return resp.text


st.header('天気予報（JSON）')
today = str(date.today())
st.json(get_json(today), expanded=False)
