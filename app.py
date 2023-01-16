import streamlit as st

with st.form("my_form", clear_on_submit=True):
   st.info('다음 양식을 모두 작성후 제출합니다.')
   uid=st.text_input('아이디',max_chars=12)