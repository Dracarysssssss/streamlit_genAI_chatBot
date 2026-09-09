from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(".env")
#streamlit  page setup

st.set_page_config(
    page_title="SpeedY ChatBot",
    page_icon="🤖",
    layout="centered"
)
st.title("🦸‍ Generative AI ChatBot")

#initiate chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]


# Show Chat History
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# llm initiation
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


user_prompt = st.chat_input("Ask ChatBot......")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user","content":user_prompt})

    response = llm.invoke(
        input = [{"role":"system", "content":"you are a helpfull assistant"}, *st.session_state.chat_history]
    )
    assistance_response = response.content[0]["text"]
    st.session_state.chat_history.append({"role":"assistant","content":assistance_response})
    with st.chat_message("assistant"):
        st.markdown(assistance_response)


