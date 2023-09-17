import streamlit as st

st.title('การทดสอบการเขียนเว็บด้วย Streamlit')
col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
   st.image("./pic/kairung02.jpg")
with col2:
   #st.header("Versicolor")
   st.header("ไก้รุ่ง เฮงพระพรหม")
   st.text('สาขาวิชาวิทยาการข้อมูล')
   st.write('คณะวิทยาศาสตร์และเทคโนโลยี')
   st.markdown('มหาวิทยาลัยราชภัฏนครปฐม')

st.header('ไก้รุ่ง เฮงพระพรหม')
st.subheader('My sub')
