from datetime import datetime

import streamlit as st
import sqlite3
import datetime
import pandas as pd
import os.path
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


file_path = os.path.dirname(__file__)
db_file = os.path.join(file_path, 'database.db')
con = sqlite3.connect(db_file)
cur = con.cursor()
tNm = 'users'
st.subheader('회원가입 폼')
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

st.subheader('회원목록')

df = pd.read_sql('select * from users',con)
# st.dataframe(df)

gb=GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(editable=True, groupable=True)
#Add pagiation
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_side_bar()
gb.configure_selection(selection_mode='multiple',
                       use_checkbox=True,
                       groupSelectsChildren="Group checkbox select children")
gridOptions = gb.build()

grid_response = AgGrid(data=df,
                       gridOptions=gridOptions,
                       data_return_mode='AS_INPUT',
                       update_mode='MODEL_CHANGED',
                       fit_columns_on_grid_load=False,
                       enable_enterprise_modules=True,
                       height=350,
                       reload_data=False)
data = grid_response['data']
selected = grid_response['selected_rows']

if selected:
    updateBtn = st.button('수정')

    if updateBtn:
        for row in selected:
            cur.execute(f"update users set uname='{row['uname']}' where no={row['no']}")
        con.commit()
        st.success('성명을 수정하였습니다')
