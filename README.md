Đây là một phần của dự án Web đa bệnh (Dự đoán 1 trong 3 bệnh Parkinson, Tiểu đường, Tim)
Nhiệm vụ của tôi là làm (xây dựng, huấn luyện) mô hình dự đoán bệnh tim.
Mô hình có khả năng dự đoán 1 người có mắc bệnh tim hay không. Kết quả: xem file Heart_rbf_LR.ipynb

Cách làm: Xây dựng một thuật toán để học trên dữ liệu dạng bảng (dataframe).
Mô tả tập dữ liệu:
    Số mẫu: 918 (không có mẫu trùng)
    Số đặc trưng: 11
    age
    Sex
    Cp: Loại đau ngực (có 4 giá trị)
    trestbps: Huyết áp tâm thu (đo được khi nghỉ ngơi) 
    chol: Lượng cholesterol trong huyết thanh (đơn vị: mg/dl).
    fbs: Lượng đường trong máu khi đói
            0: ≤ 120 mg/dl (bình thường)
            1: > 120 mg/dl (cao)
    restecg: Kết quả điện tâm đồ khi nghỉ ngơi.
    thalach: Nhịp tim tối đa đạt được trong quá trình kiểm tra (đơn vị: nhịp/phút).
    exang: Đau ngực do gắng sức. 
              0: Không
              1: Có
    oldpeak: Mức độ giảm ST (trong điện tâm đồ) do gắng sức so với khi nghỉ ngơi (đơn vị: mm).
    Slope: Độ dốc của đoạn ST khi gắng sức.
            1: Độ dốc đi lên (upsloping)
            2: Độ dốc phẳng (flat)
            3: Độ dốc đi xuống (downsloping)
    Nhãn:
    1 – mắc bệnh tim
    0 – không mắc bệnh tim
    
THUẬT TOÁN:
Triển khai thuật toán Logistic Regression
(ban đầu là SVM nhưng do cài đặc sai lầm và không thu được kết quả nên đã đổi lại thành LR)
(cũng vì vậy mà trong file ipynp vẫn còn ghi là SVM)
Tuy nhiên Logistic Regression là thuật toán học có giám sát dùng cho dữ liệu tuyến tính,
Mà dữ liệu bệnh tim là Phi Tuyến tính, do đó tác giả đề xuất giải pháp sau:
- Sử dụng Kernel RBF để: Chuyển đổi dữ liệu từ Phi Tuyến tính sang một không gian khác gần như Tuyến tính
- Áp dụng thuật toán LR trên dữ liệu ở không gian mới (tuyến tính) này để học và tạo nên mô hình.
Vì vậy mô hình này gọi là Kernel Logistic Regression.
__________________________________________________________________

Về web, thật ra đây là một web local, sử dụng giao diện các streamlit và kết nối chắp vá với nhau bằng một khung web HTML.
Chỉ dùng để triển khai ứng dụng cho các mô hình học máy. Và còn thiếu 2 mô hình còn lại (dự đoán bệnh tiểu đường và parkinson)
