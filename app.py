import streamlit as st
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
a = st.number_input('Tham số a')
b = st.number_input('Tham số b')
if st.button('Giải'):
    if a != 0:
        result = -b/a
        st.success(f'Phương trình có một nghiệm {result}')
    else:
        st.success(f'Phương trình vô nghiệm {result}')
