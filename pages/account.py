koutimport streamlit as st
from streamlit import session_state as ss
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from modules.nav import MenuButtons
from datetime import datetime



CONFIG_FILENAME = 'config.yaml'


with open(CONFIG_FILENAME) as file:
    config = yaml.load(file, Loader=SafeLoader)


def get_roles():
    """Gets user roles based on config file."""
    with open(CONFIG_FILENAME) as file:
        config = yaml.load(file, Loader=SafeLoader)

    if config is not None:
        cred = config['credentials']
    else:
        cred = {}

    return {username: user_info['role'] for username, user_info in cred['usernames'].items() if 'role' in user_info}


st.header('Account page')


authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    # config['pre-authorized']
)

login_tab, register_tab = st.tabs(['Login', 'Register'])

with login_tab:
    authenticator.login(location='main')

    if ss["authentication_status"]:
        authenticator.logout(location='main')    
        # st.write(f'Welcome *{ss["name"]}*')

        name = ss["name"]
        join_date = "2024-12-10"
        
        # 🎉 Welcome Message
        st.title(f"👋 Welcome back, {ss["name"]}!")
        st.markdown("You are logged in to **RaagaSense** – your personalized Indian classical music companion.")
        
        # Show account info in a nice container
  
        st.success("✨ You have now access to the Raga Identification System.")
        
        # Add a music-themed call to action
        st.markdown("---")
        st.markdown("### 🎶 What would you like to do next?")
        
        action = st.radio("Choose an action:", ["🎙️ Identify a Raaga", "📊 View Past Predictions", "⚙️ Manage Account Settings"])
        
        if action == "🎙️ Identify a Raaga":
            st.info("Go to the Prediction Page and upload or record your Raaga.")
        elif action == "📊 View Past Predictions":
            st.warning("🔍 This feature is coming soon! Stay tuned.")
        elif action == "⚙️ Manage Account Settings":
            st.warning("⚙️ Settings are not editable in this demo.")
        
        # Optional: Add logout button
        st.markdown("--- 🎶 ---")
        
        # Simple interactive "fun fact" button
        if st.button("🎤 Give me a music fact!"):
            st.info("🎧 Did you know? The ancient Vedic chants are considered one of the earliest forms of Indian classical music!")
        
        # Option to navigate (or placeholder for future links)
        st.markdown("""
        ### 🌟 Checkout below features!
        - 🎙️ [Make a new Raaga Prediction](#)
        - 🎶 [Explore Popular Ragas](#)
        - 🎨 [Customize Your Profile](#)
        """)
        
        # Footer
        st.markdown("""
        <div><p></p></div>
        <div style="text-align: center; font-size: 14px; color: gray;">
        Keep the music alive, {name}! 🎵  
        Made with ❤️ by KK Wagh Team
        </div>
        """.replace("{name}", name.capitalize()), unsafe_allow_html=True)
            

    elif ss["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif ss["authentication_status"] is None:
        st.warning('Please enter your username and password')

with register_tab:
    if not ss["authentication_status"]:
        try:
            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorized=config['pre-authorized']['emails'])
            # email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user()

            if email_of_registered_user:
                st.success('User registered successfully')
        except Exception as e:
            st.error(e)

# We call below code in case of registration, reset password, etc.
with open(CONFIG_FILENAME, 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

# Call this late because we show the page navigator depending on who logged in.
MenuButtons(get_roles())
