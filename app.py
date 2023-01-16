from datetime import datetime

import streamlit as st
import sqlite3
import datetime

con = sqlite3.connect('database.db')
cur = con.cursor()
tNm = 'users'

with st.form("my_form", clear_on_submit=True):
   st.info('다음 양식을 모두 작성후 제출합니다.')
   uId=st.text_input('아이디',max_chars=12)
   uName = st.text_input('성명',max_chars=10)
   uPw = st.text_input('비밀번호', type='password')
   uPwChk = st.text_input('비밀번호확인', type='password')
   uBirth = st.date_input('생년월일', min_value=datetime.date(1971,1,1))
   uGender = st.radio('성별',options=['남','여'],horizontal=True)
   submitted = st.form_submit_button('제출')

   if submitted:
      if len(uId) < 6:
           st.warning('input least 6 characters')
           st.stop()
      if uPw != uPwChk:
           st.warning('password inconsisted')

      st.success(f'{uId} {uName} {uGender} '
                 f'{uPw} {uBirth}')

      cur.execute(f"insert into users(uid,uname,pswd,brth,gndr) "
                  f" values('{uId}','{uName}','{uPw}','{uBirth}','{uGender}')")
      con.commit()