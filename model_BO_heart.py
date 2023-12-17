import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import h5py
import Dataset

raw_data = pd.read_csv('Dataset\heart2.csv')
X_save = raw_data.drop(columns=['target'])

columns_to_get_dummies = ['sex', 'cp', 'restecg', 'exang', 'slope']
data = pd.get_dummies(raw_data, columns=columns_to_get_dummies)
standardScaler         = StandardScaler()
columns_to_scale       = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
data[columns_to_scale] = standardScaler.fit_transform(data[columns_to_scale])
X = data.drop(columns='target', axis=1)
Y = data['target']
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

def load_model(filepath):
    with h5py.File(filepath, 'r') as file:
        w = file['w'][:]
        b = file['b'][()]
        gamma = file['gamma'][()]
    return w, b, gamma

w, b, gamma = load_model('heart_model.h5')

#Dịch vụ chính của model

def predict_by_model(X_test, X_train, w, b, gamma=0.1):
    n_test = X_test.shape[0]
    y_pred = np.zeros(n_test)

    for i in range(n_test):
        prediction = 0
        for j in range(X_train.shape[0]):
            squared_distance = np.sum((X_train[j] - X_test[i]) ** 2)
            prediction += w[j] * np.exp(-gamma * squared_distance)

        prediction += b
        y_pred[i] = prediction

    y_pred = 1 / (1 + np.exp(-y_pred))
    y_pred_class = np.where(y_pred >= 0.5, 1, 0)
    return y_pred_class

def predict_proba(X_test, X_train, w, b, gamma=0.1):
    n_test = X_test.shape[0]
    y_pred_proba = np.zeros(n_test)

    for i in range(n_test):
        prediction = 0
        for j in range(X_train.shape[0]):
            squared_distance = np.sum((X_train[j] - X_test[i]) ** 2)
            prediction += w[j] * np.exp(-gamma * squared_distance)

        prediction += b
        y_pred_proba[i] = 1 / (1 + np.exp(-prediction))

    return y_pred_proba


#Xử lý dữ liệu

def XuLyMau(sample_input):
    df_sample = pd.DataFrame([sample_input],
                        columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope'])
    X_mix_data = pd.concat([X_save, df_sample], ignore_index=True)
    # One-hot encoding và chuẩn hóa
    columns_to_get_dummies = ['sex', 'cp', 'restecg', 'exang', 'slope']
    X_mix_data_encoded = pd.get_dummies(X_mix_data, columns=columns_to_get_dummies)

    standardScaler = StandardScaler()
    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    X_mix_data_encoded[columns_to_scale] = standardScaler.fit_transform(X_mix_data_encoded[columns_to_scale])

    return X_mix_data_encoded

def predict(sample_input):
    X_mix_data_encoded = XuLyMau(sample_input)
    label_output = predict_proba(X_mix_data_encoded.values, X_train.values, w, b, gamma=0.1)[-1]
    return label_output

sample_input = [40, 'M', 'ATA', 140, 289, 0, 'Normal', 172, 'N', 0.0, 'Up']
print(predict(sample_input))
