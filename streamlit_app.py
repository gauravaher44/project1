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
    
    # Session state to track what the user wants to do
    if "action" not in st.session_state:
        st.session_state.action = None
    
    with col1:
        if st.button("🎙️ Record Live Audio"):
            st.session_state.action = "record"
    
    with col2:
        if st.button("📂 Upload Audio File"):
            st.session_state.action = "upload"
    
    # Show selected content dynamically
    if st.session_state.action == "record":
        st.markdown("## 🎙️ Record Your Audio")
        st.write("👉 [Add your recording functionality here!]")
    
    elif st.session_state.action == "upload":
        st.markdown("## 📂 Upload Audio File")
        uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])
        if uploaded_file:
            st.audio(uploaded_file, format="audio/wav")
            st.success("🎶 Audio uploaded successfully — ready for prediction!")
            st.write("👉 [Call your prediction function here!]")
    
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ for Indian Classical Music Enthusiasts")
else:
    st.write('Please log in on login page.')
