# import libraries
import pickle
import pandas as pd
import numpy as np
import joblib
import streamlit as st

# load model
best_model = joblib.load('./src/final_model.pkl')

def run():
    # Pembuatan form
    with st.form(key='form_churn_prediction'):
        tenure = st.number_input('Tenure', min_value=0.0, max_value=50.0, value=10.0, step=0.5)
        jumlah_device = st.selectbox('Number of Devices Registered', [1, 2, 3, 4, 5, 6], index=0)
        skor_kepuasan = st.selectbox('Satisfaction Score', [1, 2, 3, 4, 5], index=2)
        ada_keluhan = st.radio('Complain', options=[0, 1], format_func=lambda x: 'Tidak' if x == 0 else 'Ya', index=0)
        st.markdown('---')

        hari_sejak_order_terakhir = st.number_input('Days Since Last Order', min_value=0.0, max_value=30.0, value=5.0, step=0.5)
        jumlah_cashback = st.slider('Cashback Amount', 0, 150, 300)
        kategori_order = st.selectbox('Preferred Order Category', ['Laptop & Accessory', 'Mobile Phone', 'Others', 'Fashion', 'Grocery'], index=0)
        status_pernikahan = st.selectbox('Marital Status', ['Single', 'Divorced', 'Married'], index=0)

        submitted = st.form_submit_button('Predict')

    # create new data
    data_inf = {
    'Tenure': tenure,
    'NumberOfDeviceRegistered': jumlah_device,
    'SatisfactionScore': skor_kepuasan,
    'Complain': ada_keluhan,
    'DaySinceLastOrder': hari_sejak_order_terakhir,
    'CashbackAmount': jumlah_cashback,
    'PreferedOrderCat': kategori_order,
    'MaritalStatus': status_pernikahan
    }

    data_inf = pd.DataFrame([data_inf])
    data_inf

    if submitted:

        # Prediksi menggunakan model
        y_pred_inf = best_model.predict(data_inf)

        # Tampilkan hasil prediksi
        st.write('## Hasil Prediksi Churn:')
        st.write('###', 'Churn' if y_pred_inf[0] == 1 else 'Tidak Churn')


if __name__ == '__main__':
  run()