import streamlit as st
from langchain.llms import HuggingFaceHub
import os
HUGGINGFACEHUB_API_TOKEN='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'
# Replace with your actual Hugging Face token
#HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

# Initialize the HuggingFace model
repo_id = "gpt2"  # Make sure this is the correct repository ID
llm = HuggingFaceHub(repo_id=repo_id, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN, model_kwargs={"max_length": 128, "temperature": 0.7})

# Streamlit interface
st.title("Chat with GPT-2")
st.write("This chatbot is powered by a GPT-2 model hosted on Hugging Face.")

user_input = st.text_input("You:", "Type your message here...")

if st.button("Send"):
    if user_input:
        try:
            response = llm(user_input)
            st.write(f"Bot: {response}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.write("Please enter a message.")
