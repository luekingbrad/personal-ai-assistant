import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Streamlit UI
st.title("Personal AI Assistant")

# Load memory
MEMORY_FILE = "memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = []

# User input
user_input = st.text_input("What would you like help with?")

if st.button("Send") and user_input:

    # Save user message
    memory.append({"role": "user", "content": user_input})

    # Generate AI response
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=memory
    )

    ai_response = response.choices[0].message.content

    # Save AI response
    memory.append({"role": "assistant", "content": ai_response})

    # Save memory to file
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

    # Display response
    st.write(ai_response)
