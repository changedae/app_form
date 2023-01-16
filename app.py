import streamlit as st
import datetime

with st.form("my_form", clear_on_submit=True):
   st.info('다음 양식을 모두 작성후 제출합니다.')
   uId=st.text_input('아이디',max_chars=12)
   uNm = st.text_input('성명', max_chars=10)
   uGender = st.radio('성별',options=['남','성'] horizontal=True)
   uPw = st.text_input('비밀번호', type='password')
   uPwChk= st.text_input('비밀번호 확인', type='password')
   uEmail = st.text_input('이메일', max_chars=50)
   uBirth=st.date_input('생년월일', min_value=datetime.date(1971, 1, 1))

   submitted = st.form_submit_button('제출')

   if submitted:
      st.success('제출됨')