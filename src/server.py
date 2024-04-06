import os
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()


# Set up Google Gemini-Pro AI model
def setup_gemini_model():
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    gen_ai.configure(api_key=GOOGLE_API_KEY)
    return gen_ai.GenerativeModel("gemini-1.0-pro")


# Function to start chat session
def start_chat_session(model):
    return model.start_chat(history=[])


# Function to send user's message to Gemini-Pro and get the response
def send_message_to_gemini(user_prompt, chat_session):
    return chat_session.send_message(user_prompt)
