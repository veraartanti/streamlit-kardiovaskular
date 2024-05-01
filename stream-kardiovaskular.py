import pickle
import numpy as np
import streamlit as st

# Judul
st.title('Klasifikasi Penyakit Kardiovaskular')

# Deskripsi
st.markdown("""
Aplikasi ini melakukan klasifikasi pasien berdasarkan beberapa fitur untuk memprediksi apakah pasien menderita penyakit kardiovaskular atau tidak.
""")

# Sidebar
st.sidebar.header('Pencegahan Penyakit Kardiovaskular')
st.sidebar.markdown("""
1. Makanlah makanan sehat seperti buah-buahan, sayuran, dan biji-bijian.
2. Lakukan olahraga secara teratur.
3. Hindari merokok dan konsumsi alkohol berlebihan.
4. Pertahankan berat badan yang sehat.
5. Atur tekanan darah dan kolesterol Anda.
6. Cek kesehatan secara rutin.
""")

# Input fitur
st.header('Masukkan Fitur Pasien')
time = st.number_input('Time')
serum_creatinine = st.number_input('Serum Creatine')
ejection_fraction = st.number_input('Ejection Fraction')
age = st.number_input('Age')
serum_sodium = st.number_input('Serum Sodium')
creatinine_phosphokinase = st.number_input('Creatine Phosphokinase')
platelets = st.number_input('Platelets')

# Prediksi
if st.button('Klasifikasi Penyakit Kardiovaskular'):
    # Lakukan prediksi di sini
    prediction = "Pasien Meninggal"  # Ganti ini dengan hasil prediksi sesungguhnya
    st.success(f'Hasil Prediksi: {prediction}')
