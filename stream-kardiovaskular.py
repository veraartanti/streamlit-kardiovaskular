import pickle
import numpy as np
import streamlit as st

# load saved model
model = pickle.load(open('kardiovaskular.sav', 'rb'))

# judul web
st.title('Klasifikasi Penyakit Kardiovaskular')

# Sidebar untuk input data
st.sidebar.header('Dashboard Edukasi Pencegahan')

# Konten sidebar
st.sidebar.markdown('Pencegahan Penyakit Kardiovaskular:')
st.sidebar.markdown('- Hindari merokok')
st.sidebar.markdown('- Tetap aktif secara fisik')
st.sidebar.markdown('- Konsumsi makanan sehat dan seimbang')
st.sidebar.markdown('- Pantau tekanan darah secara teratur')
st.sidebar.markdown('- Batasi konsumsi alkohol')
st.sidebar.markdown('- Kelola stres dengan baik')

# Input data
col1, col2, col3 = st.columns(3)
with col1:
    time = st.number_input('Time')
    age = st.number_input('Age')
    serum_sodium = st.number_input('Serum Sodium')
with col2:
    serum_creatinine = st.number_input('Serum Creatine')
    creatinine_phosphokinase = st.number_input('Creatine Phosphokinase')
with col3:
    ejection_fraction = st.number_input('Ejection Fraction')
    platelets = st.number_input('Platelets')

# code for prediction
heart_diagnosis =''

# membuat tombol prediksi
if st.button('Klasifikasi Penyakit Kardiovaskular'):
    heart_prediction = model.predict([[time, serum_creatinine, ejection_fraction, age, serum_sodium, creatinine_phosphokinase, platelets]])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'Pasien Meninggal'
    else:
        heart_diagnosis = 'Pasien Tidak Meninggal'
st.success(heart_diagnosis)
