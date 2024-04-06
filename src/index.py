import streamlit as st


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# Function to display the chat interface
def display_chat_interface(chat_session):
    # Display the chatbot's title on the page
    st.title("🤖 Gemini Pro - AI")

    # Display the chat history
    for message in chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input field for user's message
    user_prompt = st.chat_input("Ask Gemini-Pro...")
    return user_prompt
