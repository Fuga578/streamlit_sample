#!/usr/bin/env -S python -m streamlit run

import time
import streamlit as st

base = 'https://images.pexels.com/photos/'
images = [
    base + '612949/pexels-photo-612949.jpeg?auto=compress&w=1260&h=750',
    base + '3688579/pexels-photo-3688579.jpeg?auto=compress&w=1260&h=750',
    base + '4449867/pexels-photo-4449867.jpeg?&auto=compress&w=1260&h=750',
    base + '3757140/pexels-photo-3757140.jpeg?auto=compress&w=1260&h=750'
]

album = st.empty()
for img in images:
    album.image(img)
    time.sleep(1)

album.markdown('Completed')
