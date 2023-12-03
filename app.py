import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('diabetes.sav', 'rb'))

st.title('Klasifikasi Penyakit Diabetes Menggunakan Algoritma Regresi')

col1, col2 = st.columns(2)

#membuat form inputan
with col1:  
    Pregnancies = st.number_input('Input Nilai Pregnancies', 0)
with col2:
    Glucose = st.number_input('Input Nilai Glucose', 0)
with col1:
    BloodPressure = st.number_input('Input Nilai Blood Pressure', 0)
with col2:
    SkinThickness = st.number_input('Input Nilai Skin Thickness', 0)
with col1:
    Insulin = st.number_input('Input Nilai Insulin', 0)
with col2:
    Bmi = st.number_input('Input Nilai BMI')
with col1:
    DiabetesPedigreeFunction = st.number_input('Input Nilai Diabetes Pedigree Function')
with col2:
    Age = st.number_input('Input Nilai Age', 0)

#coding prediksi
input_data = ''

#membuat button prediksi
if st.button('Prediksi?'):
    diab_prediction = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, Bmi, DiabetesPedigreeFunction, Age]])
    
    if(diab_prediction [0] == 1):
        input_data = 'Pasien terkena Diabetes'
    else :
        input_data = 'Pasien TIDAK terkena Diabetes'

    st.success(input_data)
