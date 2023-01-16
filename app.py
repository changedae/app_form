from datetime import datetime

import streamlit as st
import datetime


with st.form("my_form", clear_on_submit=True):
   st.info('다음 양식을 모두 작성후 제출합니다.')
   uid=st.text_input('아이디',max_chars=12)
   uName = st.text_input('성명',max_chars=10)
   uPw = st.text_input('비밀번호', type='password')
   uPwChk = st.text_input('비밀번호확인', type='password')
   uBirth = st.date_input('생년월일', min_value=datetime.date(1971,1,1))
   submitted = st.form_submit_button('제출')

   if submitted:
      if len(uid) < 6:
           st.warning('input least 6 characters')
           st.stop()
      if uPw != uPwChk:
           st.warning('password inconsisted')

      st.success('제출됨')