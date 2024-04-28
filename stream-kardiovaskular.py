import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('kardiovaskular.sav','rb'))

# judul web
st.title('Klasifikasi Penyakit Kardiovaskular')

col1, col2, col3 = st.columns(3)

with col1:
    time = st.number_input('Time')
with col2:
    serum_creatinine = st.number_input('Serum Creatine')
with col3:
    ejection_fraction = st.number_input('Ejection Fraction')
with col1:
    age = st.number_input('Age')
with col2:
    serum_sodium = st.number_input('Serum Sodium')
with col3:
    creatinine_phosphokinase = st.number_input('Creatine Phosphokinase')
with col1:
    platelets = st.number_input('Platelets')

# code for prediction
heart_diagnosis =''

# membuat tombol prediksi
if st.button('Klasifikasi Penyakit Kardiovaskular'):
    heart_prediction = model.predict([[time, serum_creatinine, ejection_fraction, age, serum_sodium, creatinine_phosphokinase, platelets]])

    if (heart_prediction[0]==1):
        heart_diagnosis = 'Pasien Meninggal'
    else:
        heart_diagnosis = 'Pasien Tidak Meninggal'
st.success(heart_diagnosis)