import pickle
import numpy as np
import streamlit as st

# load saved model
model = pickle.load(open('kardiovaskular.sav', 'rb'))

# judul web
st.title('Klasifikasi Penyakit Kardiovaskular')

# Sidebar untuk input data
st.sidebar.image('heart_icon.png', width=100)
st.sidebar.header('Pencegahan Penyakit Kardiovaskular')
st.sidebar.markdown('### **Langkah-langkah Pencegahan:**')
st.sidebar.markdown('- **Hindari Merokok**')
st.sidebar.markdown('- **Tetap Aktif Secara Fisik**')
st.sidebar.markdown('- **Konsumsi Makanan Sehat**')
st.sidebar.markdown('- **Pantau Tekanan Darah**')
st.sidebar.markdown('- **Batasi Konsumsi Alkohol**')
st.sidebar.markdown('- **Kelola Stres**')

# Input data
st.header('Masukkan Data Pasien')
col1, col2 = st.columns(2)
with col1:
    time = st.number_input('Waktu (Time)')
    age = st.number_input('Usia (Age)')
    serum_sodium = st.number_input('Natrium Serum (Serum Sodium)')
    serum_creatinine = st.number_input('Kreatinin Serum (Serum Creatine)')
with col2:
    creatinine_phosphokinase = st.number_input('Fosfokinase Kreatinin (Creatine Phosphokinase)')
    ejection_fraction = st.number_input('Fraksi Eject (Ejection Fraction)')
    platelets = st.number_input('Trombosit (Platelets)')

# code for prediction
heart_diagnosis = ''

# membuat tombol prediksi
if st.button('Cek Klasifikasi'):
    heart_prediction = model.predict([[time, serum_creatinine, ejection_fraction, age, serum_sodium, creatinine_phosphokinase, platelets]])

    if heart_prediction[0] == 1:
        heart_diagnosis = '**Pasien Meninggal**'
    else:
        heart_diagnosis = '**Pasien Tidak Meninggal**'

# Hasil Prediksi
st.header('Hasil Klasifikasi')
st.markdown(f'Hasil klasifikasi: {heart_diagnosis}')
