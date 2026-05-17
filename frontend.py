import streamlit as st
import requests


st.markdown("""
<style>

/* Main app width */
.block-container {
    max-width: 95%;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main title */
h1 {
    font-size: 4rem !important;
    font-weight: 800 !important;
}

/* Subtitle */
p {
    font-size: 1.3rem !important;
}

/* Chat messages */
.stChatMessage {
    font-size: 1.2rem !important;
    padding: 1rem !important;
}

/* User input box */
textarea {
    font-size: 1.2rem !important;
}

/* Input area */
.stChatInputContainer {
    padding-top: 1rem;
    padding-bottom: 1rem;
}

/* Blue info container */
.custom-box {
    background-color: #17304d;
    padding: 30px;
    border-radius: 18px;
    font-size: 1.2rem;
    line-height: 2;
    margin-bottom: 25px;
}

</style>
""", unsafe_allow_html=True)


st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AI Research Assistant")

st.markdown(
    "Ask questions about AI research papers."
)

st.info(
    """
    📚 Powered by 5 foundational AI research papers:
    
    • Attention Is All You Need  
    • Retrieval-Augmented Generation (RAG)  
    • Chain-of-Thought Prompting  
    • Llama 2  
    • ReAct
    """
)

if "messages" not in st.session_state:
    st.session_state.messages = []



for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


user_input = st.chat_input(
    "Ask your question..."
)


if user_input:

   

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):

        st.markdown(user_input)

  

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={
                        "question": user_input
                    }
                )

                data = response.json()

                answer = data["answer"]

            except Exception as e:

                answer = f"Error: {e}"

            st.markdown(answer)



    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )