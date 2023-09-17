import streamlit as st

st.title('การทดสอบการเขียนเว็บด้วย Streamlit')
col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
   st.header("ไก้รุ่ง เฮงพระพรหม")
with col1:
   st.header("Versicolor")
   st.image("./pic/kairung01.jpg")

st.header('ไก้รุ่ง เฮงพระพรหม')
st.subheader('My sub')
