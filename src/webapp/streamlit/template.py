import streamlit as st
import streamlit.components.v1 as components
import torch
from dalle_pytorch import DiscreteVAE, DALLE
from giphypop import upload
import os

st.title('This Plant Does Not Exist')
st.markdown('### App by David, Dylan, Karen')

description = st.text_input(label='Enter your description of plant')


if st.button('Submit'):
    st.write('### Plant Photo:')
    #
    f = """
             <img src="../outputs/hi_five/0.jpg" alt="Plant Result"></img>
    """

    components.html(f)