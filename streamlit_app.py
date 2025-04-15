import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.account import get_roles

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
    
    # Page Configuration
    st.set_page_config(page_title="Raga Identification System 🎶", page_icon="🎵")
    
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
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🎙️ Record Live Audio"):
            st.switch_page("pages/page2.py")  # Change path to your recorder page
    
    with col2:
        if st.button("📂 Upload Audio File"):
            st.switch_page("pages/upload_page.py")  # Add a dedicated upload page or section
    
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ for Indian Classical Music Enthusiasts")
else:
    st.write('Please log in on login page.')
