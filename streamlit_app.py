import streamlit as st
from streamlit import session_state as ss
from modules.nav import MenuButtons
from pages.account import get_roles
import time
from datetime import datetime
import random

# If the user reloads or refreshes the page while still logged in,
# go to the account page to restore the login status. Note reloading
# the page changes the session id and previous state values are lost.
# What we are doing is only to relogin the user.
if 'authentication_status' not in ss:
    st.switch_page('./pages/account.py')


MenuButtons(get_roles())

# Protected content in home page.
if ss.authentication_status:
    # st.write('This content is only accessible for logged in users.')
    
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
    # Session state to track what the user wants to d
    # A brief animated intro using a status message
    with st.spinner("Tuning the tanpura... 🎶"):
        time.sleep(2)
    
    # Markdown for styled text and description
    st.markdown("""
    <div style="text-align: justify; font-size: 17px;">
    Indian classical music is a universe of melodies called <b>Ragas</b>.  
    Each Raga evokes unique emotions, moods, and spiritual experiences.  
    🎧 Our AI-powered system listens, understands, and tells you the Raaga hidden in your music clip.  
    Just record or upload your tune and let us decode the melody magic!
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
    Made with ❤️ for music lovers by KK Wagh Team 🎵
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ for Indian Classical Music Enthusiasts")
else:
    # st.header('Home page')
    # Title section with style
    st.markdown("""
    <div style="text-align: center; font-size: 48px; font-weight: bold; color: #8E44AD;">
    🎶 Welcome to KK Wagh 🎶
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; font-size: 20px; color: #555;">
    Discover the magic of Indian Classical Music — Identify ragas from your own recordings!
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Date and time
    now = datetime.now().strftime("%A, %d %B %Y | %I:%M %p")
    st.markdown(f"<p style='text-align: center; color: gray;'>🗓️ {now}</p>", unsafe_allow_html=True)
    
    # Animated Emoji Line
    st.markdown("<h3 style='text-align: center;'>🎧 🎶 🎼 🎵 🥁 🎻 🎤</h3>", unsafe_allow_html=True)
    
    # Fun Random Fact Button
    if st.button("🎙️ Give me a Raaga Fun Fact!"):
        facts = [
            "🎶 Raga Yaman is often played in the evening and conveys a mood of devotion and tranquility.",
            "🎵 There are more than 500 ragas in Indian Classical Music!",
            "🎧 Raga Bhairavi is one of the most versatile ragas — it’s often used to conclude a concert.",
            "🎶 The earliest treatise on Indian music, the 'Natya Shastra', was written over 2000 years ago.",
            "🎼 Raga Desh is known to evoke feelings of patriotism and joy.",
        ]
        st.success(random.choice(facts))
    
    # Audio Teasers (optional - replace these URLs with your own audio samples)
    st.subheader("🎶 Listen to some Iconic Ragas")
    ragas = {
        "Yaman": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        "Yaman": "https://ia803204.us.archive.org/0/items/RaagYaman_201707/Invocation%20%28Raag%20Yaman%20Kalyan%29%20-%20Divinity%202%20-%20Flute%20-%20Sitar.mp3", 
        "Bhairavi": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        "Bhairavi": "https://ia801700.us.archive.org/31/items/RagaBhairavi/Raag%20Bhairavi%20-%20Pt.Keshav%20Ginde%20-%20Flute.mp3", 
        #"Desh": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3", 
        "Darbari": "https://ia600603.us.archive.org/13/items/RaagDarbari_201707/MERU%20Concert%20live%20-%20Lenneke%20van%20Staalen%20-%20Violin%20-%20Raga%20Darbari%20Kanada.mp3"
    }
    
    for raga, url in ragas.items():
        st.markdown(f"**🎵 {raga}**")
        st.audio(url)
    
    # Quote of the day
    st.markdown("""
    <div style="text-align: center; font-size: 20px; color: #333; margin-top: 20px; padding: 10px; border-left: 4px solid #8E44AD;">
    🎶 "Music is the divine way to tell beautiful, poetic things to the heart." – Pablo Casals
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Navigation hints (could connect these to pages later)
    st.markdown("""
    ### 🎛️ Explore:
    - 🎙️ [Record your Raaga](#)
    - 📚 [Learn about Raagas](#)
    - 🎶 [Your Audio Predictions](#)
    """)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; font-size: 14px; color: gray; margin-top: 40px;">
    Made with ❤️ for Indian Classical Music 🎶 | © 2025 KK Wagh
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.warning('Please log in on login page.')
