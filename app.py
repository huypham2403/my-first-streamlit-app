import streamlit as st
import plotly
import sklearn
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
    if a == 0:
        if b==0:
            st.success(f'Phương trình vô nghiệm')
        st.success(f'Phương trình vô nghiệm')
    else: 
        result = -b/a
        st.warning(f'Phương trình có một nghiệm {result}')
