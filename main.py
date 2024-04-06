import streamlit as st
from dotenv import load_dotenv

# import components
from src.index import display_chat_interface
from src.server import setup_gemini_model, start_chat_session, send_message_to_gemini


# Load environment variables
load_dotenv()

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)


# Function to initialize chat session in Streamlit
def initialize_chat_session():
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = start_chat_session(setup_gemini_model())


# Display chat interface
initialize_chat_session()
user_prompt = display_chat_interface(st.session_state.chat_session)

# Process user input and display Gemini-Pro's response
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = send_message_to_gemini(user_prompt, st.session_state.chat_session)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

print(">>> App is running...")
