import streamlit as st
import os

from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_community.llms import Tongyi


# os.environ["DASHSCOPE_API_KEY"] = "sk-4b9ed51bea374986b9521dd8682d642e"

st.title("聊天问答模型")

with st.sidebar:
    if st.button("清除聊天",type="primary"):
        st.session_state['history'] = ConversationBufferMemory()

if 'history' not in st.session_state:
    st.session_state['history'] = ConversationBufferMemory()

if key_ty:=st.sidebar.text_input("请输入通义千问的API密钥：", type="password"):
    model_ty = Tongyi(api_key=key_ty)
    conversation = ConversationChain(llm=model_ty,
                                 memory=st.session_state['history'])
    for i in conversation.memory.chat_memory.messages:
        st.chat_message(i.type).write(i.content)

    if a:=st.chat_input():
        st.chat_message("user").write(a)
        with st.spinner("AI正在思考中，请稍等..."):
            res = conversation.invoke(a)
            st.chat_message("ai").write(res['response'])
else:
    st.info("请输入通义千问的API密钥")