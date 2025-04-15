import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.account import get_roles
import time


# If the user reloads or refreshes the page while still logged in,
# go to the account page to restore the login status. Note reloading
# the page changes the session id and previous state values are lost.
# What we are doing is only to relogin the user.
if 'authentication_status' not in ss:
    st.switch_page('./pages/account.py')


MenuButtons(get_roles())
st.header('Home page')


# Protected content in home page.
if ss.authentication_status:
    st.write('This content is only accessible for logged in users.')
    
    # Title and intro
    st.title("🎶 Raga Identification System")
    st.subheader("Discover the Soul of Indian Classical Music")
    
    st.write("""
    Welcome to the **Raga Identification System**, an AI-powered tool designed to recognize Indian classical ragas from audio clips.  
    Indian classical music features rich melodies, emotions, and centuries of tradition — now made accessible with machine learning.
    
    🎵 Upload your recording, or record live to identify the raga in moments!
    """)
    
    # Add a nice music-related image or GIF link if you have one
    st.image("https://media.giphy.com/media/3ohs4BSacFKI7A717y/giphy.gif", caption="Feel the melody!")
    
    # Call to action buttons
    st.markdown("### What would you like to do?")
    
    # Session state to track what the user wants to do
    # App title with emoji
    st.title("🎶 Welcome to RaagaSense 🎶")
    st.subheader("Discover the soul of Indian classical music")
    
    # A brief animated intro using a status message
    with st.spinner("Tuning the tanpura... 🎶"):
        time.sleep(2)
    
    # Markdown for styled text and description
    st.markdown("""
    <div style="text-align: justify; font-size: 17px;">
    Indian classical music is a universe of melodies called <b>Ragas</b>.  
    Each Raga evokes unique emotions, moods, and spiritual experiences.  
    🎧 Our AI-powered system listens, understands, and tells you the Raaga hidden in your music clip.  
    Just record or upload your tune and let RaagaSense decode the melody magic!
    </div>
    """, unsafe_allow_html=True)
    
    # Fun music-themed horizontal divider
    st.markdown("--- 🎼 ---")
    
    # A music emoji button (looks interactive)
    if st.button("🎙️ Start Identifying Raaga"):
        st.success("Head over to the prediction page to begin!")
    
    # Some inspirational music quote
    st.markdown("""
    > *"The music in the soul can be heard by the universe."*  
    > — Lao Tzu
    """)
    
    # Footer with credit
    st.markdown("""
    <div style="text-align: center; color: gray; font-size: 14px;">
    Made with ❤️ for music lovers by RaagaSense Team 🎵
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ for Indian Classical Music Enthusiasts")
else:
    st.write('Please log in on login page.')
