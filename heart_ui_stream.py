import streamlit as st
import model_BO_heart

# Tiêu đề của ứng dụng
st.subheader("Kiểm tra, phát hiện bệnh tim mạch")

# Thêm một số widget cơ bản
username = st.text_input("Tên của bạn là:", "Nhập tên của bạn")

gender = st.radio("Giới tính:", ["Nam", "Nữ"]) #--- M F

age = st.number_input("Tuổi:", step=1)

cp = st.selectbox("Bạn có bị đau ngực không, hãy chọn loại đau ngực?",["ATA", "NAP", "TA", "ASY"])

col1, col2, col3, col4 = st.columns(4)

fbs_form = col1.selectbox("Đường huyết đói:",["<120 ml/dl", ">120 ml/dl"]) #---- 0 1

restecg = col2.selectbox("Kết quả điện tâm đồ nghỉ ngơi:",["Normal", "LVH", "ST"])

exang_form = col3.selectbox("Bạn có bị đau ngực sau khi tập thể dục không?",["Có", "Không"]) #----- Y N

slope = col4.selectbox("Góc nghiêng của đoạn ST đo bằng Điện tâm đồ:",["Up", "Down", "Flat"])

col1, col2, col3, col4 = st.columns(4)

trestbps = col1.number_input("Huyết áp nghỉ ngơi (mmHg):")
chol = col2.number_input("Cholesterol (mm/dl):")
thalach = col3.number_input("Nhịp tim tối đa (nhịp/phút):")
oldpeak = col4.number_input("Sự thay đổi độ cao của ST sau khi tập thể dục (mm):")

bt_submit = st.button('Predict')

if bt_submit:
    sex = 'F' if gender == "Nữ" else 'M' # Gán 1 cho Nữ và 0 cho Nam
    fbs = 1 if fbs_form == "<120 ml/dl" else 0
    exang = 'Y' if fbs_form == "Có" else 'N'
    input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope]
    predict_result = model_BO_heart.predict(input_data)
    
    predict_result_percentage = predict_result * 100

    if predict_result_percentage > 30:
        st.write(f'<p class="big-font">Khả năng bạn bị mắc bệnh tim là {predict_result_percentage:.2f}%</p>', unsafe_allow_html=True)
    else:
        st.write(f'<p class="big-font">Khả năng bạn bị mắc bệnh tim là {predict_result_percentage:.2f}%</p>', unsafe_allow_html=True)
        st.write('<p class="big-font">Bạn hoàn toàn khỏe mạnh.</p>',unsafe_allow_html=True)