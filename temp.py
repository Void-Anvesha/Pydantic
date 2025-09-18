import streamlit as st
import requests

# Streamlit page config
st.set_page_config(page_title="Gemma Chat with Ollama", page_icon="💬")
st.title("💬 Chat with Gemma (via Ollama)")

# Store chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_prompt = st.chat_input("Ask something...")

if user_prompt:
    # Display user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Send prompt to Ollama's local server
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gemma",
            "messages": [
                {"role": "user", "content": user_prompt}
            ]
        }
    )

    # Stream the response content
    response_text = ""
    for chunk in response.iter_lines():
        if chunk:
            data = chunk.decode("utf-8").strip()
            if data.startswith("data:"):
                data = data.replace("data:", "")
                try:
                    import json
                    content = json.loads(data)
                    if "message" in content and "content" in content["message"]:
                        response_text += content["message"]["content"]
                        with st.chat_message("assistant"):
                            st.markdown(response_text)
                except Exception:
                    pass

    st.session_state.messages.append({"role": "assistant", "content": response_text})
