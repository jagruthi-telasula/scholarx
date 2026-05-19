# chatbot.py

import streamlit as st

# Chatbot responses
def chatbot_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hello! How can I help you?"

    elif "your name" in user_input:
        return "I am an AI Chatbot."

    elif "ai" in user_input:
        return "Artificial Intelligence is the simulation of human intelligence by machines."

    elif "machine learning" in user_input:
        return "Machine Learning is a branch of AI that allows systems to learn from data."

    elif "bye" in user_input:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."

# Streamlit UI
st.title("AI Chatbot")

st.write("Simple AI Chatbot for Internship Task")

# User Input
user_input = st.text_input("Enter your message")

# Button
if st.button("Send"):

    response = chatbot_response(user_input)

    st.success(response)