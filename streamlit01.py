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

html_1 = """
<div style="background-color:#FFBF00;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

