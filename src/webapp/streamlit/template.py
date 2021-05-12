import streamlit as st
import streamlit.components.v1 as components
# import torch
# from dalle_pytorch import DiscreteVAE, DALLE

import os

st.title('This Plant Does Not Exist')
st.markdown('### App by David, Dylan, Karen')

description = st.text_input(label='Description')

#dalle = torch.load("dalle.pt",map_location=torch.device('cpu'))

if st.button('Submit'):
    #send_request(color + ' ' + song)

    st.write('### Plant Photo:')

    #with open('streamlit/media.html', 'r') as f:
    f = """
        <iframe
                src="https://giphy.com/embed/E6jscXfv3AkWQ" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen>
        </iframe>
        <p>
            <a href="https://giphy.com/gifs/cat-typing-E6jscXfv3AkWQ">via GIPHY</a>
        </p>
        """
    components.html(f,height=800)#.replace('SONGPATHHERE', songs[song]).replace('MOTION_NAME_HERE', room), height=8000)