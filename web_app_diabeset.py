import streamlit as st
import pandas as pd

col1, col2, col3 = st.columns(3)

gender = col1.selectbox("Enter your gender",["Male", "Female"])

age = col2.number_input("Enter your age")

Insulin = col3.number_input("Enter Your Insulin")

Glucose = col1.number_input("Enter Your Glucose")

BMI = col2.number_input("Enter your BMI")

Pregnancies = col3.number_input("Enter Your Pregnancies")

# lấy dữ liệu từ form

data = [(age, Insulin, Glucose, BMI, Pregnancies)]

print(data)

df_give_from_form = pd.DataFrame(data, columns=["Age", "Insulin", "Glucose", "BMI", "Pregnancies"])

# tạo button predict để dự đoán

# vd là có model rồi Tín đưa model vào nhé

def model(df_give_from_form):
    #model này trả về kết quả 0 hoặc 1
    return 0


prediction = model(df_give_from_form)

haha = 0

button = st.button('Predict')

if button:

    if(haha==0):
        st.write('<p class="big-font">You likely will not develop heart disease in 10 years.</p>',unsafe_allow_html=True)

    else:
        st.write('<p class="big-font">You are likely to develop heart disease in 10 years.</p>',unsafe_allow_html=True)