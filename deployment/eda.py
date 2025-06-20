import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt

def run():
    # membuat title
    st.title('E-Commerce Customer Churn Prediction App')

    # membuat sub header
    st.subheader('Halaman ini menampilkan hasil eksplorasi data dari dataset')

    # menambahkan gambar
    image = Image.open('./src/image.png')
    st.image(image, caption='EDA Customer Churn for E-commerce')

    # menampilkan DataFrame
    df = pd.read_csv('src/ecom_data.csv')
    st.dataframe(df)

    # membuat bar chart PrefferedLoginDevice
    st.write('### Bar Chart Preffered Login Device')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='PreferredLoginDevice', data=df)
    st.pyplot(fig)
    st.write('Dari bar chart di atas terlihat bahwa mayoritas user lebih ' \
    'memilih untuk login menggunakan perangkat tipe Mobile Phone dibandingkan dengan perangkat tipe Computer. ' \
    'Hal ini menunjukkan preferensi user yang cenderung lebih nyaman atau lebih sering mengakses layanan ' \
    'melalui perangkat mobile.')

    # membuat histogram of HourSpendOnApp
    st.write('### Persebaran Durasi Harian Pengguna dalam Menggunakan Aplikasi')
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df['HourSpendOnApp'], bins=30, kde=True)
    st.pyplot(fig)
    st.write('Dari bar chart di atas terlihat bahwa mayoritas pengguna menghabiskan waktu sekitar 2 ' \
    'hingga 3 jam per hari dalam menggunakan aplikasi. Sangat sedikit pengguna yang menghabiskan waktu hanya 1 jam ' \
    'maupun lebih dari 4 jam. Hal ini menunjukkan bahwa durasi penggunaan aplikasi secara ' \
    'harian cenderung berada pada rentang sedang.')

    # membuat bar chart CityTier
    st.write('### Bar Chart CityTier')
    fig = plt.figure(figsize=(15, 5))
    sns.countplot(x='CityTier', data=df)
    st.pyplot(fig)
    st.write('Berdasarkan visualisasi bar chart di atas dapat dilihat bahwa mayoritas pengguna berasal dari kota ' \
    'dengan tier 1, yang menunjukkan bahwa aplikasi ini paling banyak digunakan di kota ' \
    'besar atau metropolitan')

    # membuat histogram of CashbackAmount
    st.write('### Distribusi jumlah cashback bulanan yang diterima pengguna')
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df['CashbackAmount'], bins=30, kde=True)
    st.pyplot(fig)
    st.write('Berdasarkan histogram di atas terlihat bahwa sebagian besar pengguna menerima cashback bulanan dalam ' \
    'rentang 100 hingga 300, dengan puncak tertinggi berada sekitar nilai 150. ' \
    'Sementara itu, jumlah pengguna yang tidak menerima cashback (nilai 0) sangat sedikit, ' \
    'hampir tidak terlihat pada distribusi, menandakan sebagian besar pengguna memang ' \
    'mendapatkan cashback secara rutin')

    # membuat plot menggunakan plotly
    st.write('### Scatter Plot Tenure dan HourSpendOnApp ')
    fig = px.scatter(df, x='Tenure', y='HourSpendOnApp', color='Churn', 
                    hover_data=['PreferredLoginDevice', 'CityTier'])
    st.plotly_chart(fig)

    # membuat histogram berdasarkan input user
    st.write('### Histogram berdasarkan input user')
    option = st.selectbox('Pilih Column : ', ('Gender', 'PreferredPaymentMode', 'MaritalStatus'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df[option], bins=30, kde=True)
    st.pyplot(fig)


if __name__ == '__main__':
    run()