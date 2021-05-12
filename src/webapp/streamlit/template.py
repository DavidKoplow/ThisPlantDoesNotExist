import streamlit as st
import streamlit.components.v1 as components

import os

st.title('This Plant Does Not Exist')
st.markdown('### App by David, Dylan, Karen')

color = st.text_input(label='Description')

if st.button('Submit'):
    #send_request(color + ' ' + song)

    st.write('### Plant Photo:')

    with open('media.html', 'r') as f:
        components.html(f.read(),height=800)#.replace('SONGPATHHERE', songs[song]).replace('MOTION_NAME_HERE', room), height=8000)