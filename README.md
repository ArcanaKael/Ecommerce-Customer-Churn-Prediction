# 🛒 Customer Churn Prediction for E-Commerce

## 🔗 Project Access

- 📂 **Dataset Source**: [Kaggle – E-Commerce Customer Churn Data](https://www.kaggle.com/datasets/upam22/ecommerce-customer-churn-data/data)  
- 🚀 **Live App Deployment**: [Hugging Face Space – E-Commerce Churn Analysis](https://huggingface.co/spaces/canakael/ecommerce-churn-analysis)

---

## 📁 Repository Structure

```
1. README.md                          : Dokumentasi utama proyek
2. ml_pipeline.ipynb                  : Notebook berisi proses EDA hingga model siap deploy
3. model_inference.ipynb              : Notebook inference model
4. conceptual_qna.txt                 : Jawaban conceptual problem
5. deployment folder                  : Folder berisi file deployment untuk menjalankan aplikasi Streamlit di Hugging Face Spaces
```


---

## 🌿 Problem Background

Menjaga loyalitas pelanggan adalah tantangan utama dalam industri e-commerce. Sering kali, identifikasi pelanggan yang akan berhenti (churn) dilakukan secara manual atau berdasarkan intuisi yang tidak akurat.

Proyek ini bertujuan untuk membangun **model machine learning prediktif** yang mampu mengidentifikasi pelanggan yang berisiko churn secara cepat, akurat, dan objektif. Dengan pendekatan ini, perusahaan dapat:
- Mengambil tindakan preventif tepat waktu
- Mengurangi tingkat kehilangan pelanggan
- Meningkatkan efisiensi dan profitabilitas bisnis secara keseluruhan

---

## 🎯 Project Output

- Model klasifikasi terbaik menggunakan **Random Forest**
- Notebook inference untuk deployment
- Aplikasi visual interaktif dengan **Streamlit**, di-*deploy* melalui **Hugging Face Spaces**

---

## 📦 Dataset

- **Jumlah data**: 5.630 baris, 20 kolom
- **Tipe data**:
  - Numerik kontinu (`float64`) : 7 kolom  
  - Numerik diskret (`int64`)   : 8 kolom  
  - Kategorikal (`object`)      : 5 kolom
- **Catatan**:
  - Terdapat beberapa missing values
  - Distribusi target cukup tidak seimbang

---

## 🔧 Methodology

Model klasifikasi yang diuji:

- Logistic Regression  
- K-Nearest Neighbors  
- Support Vector Machine  
- Decision Tree  
- **Random Forest** ✅ *(model terbaik)*  
- Gradient Boosting

📌 **Model terbaik dipilih berdasarkan:**
- Cross-validation
- Evaluation metrics: accuracy, classification report, confusion matrix

---

## 🛠️ Tech Stack

- **Bahasa & IDE**: Python (Jupyter Notebook)  
- **EDA & Visualisasi**: `pandas`, `numpy`, `seaborn`, `matplotlib`, `scipy`
- **Preprocessing & Feature Engineering**:  
  - `scikit-learn`: `StandardScaler`, `OneHotEncoder`, `ColumnTransformer`  
  - `feature_engine`: untuk penanganan outlier  
  - `imblearn`: untuk penanganan data imbalance (SMOTE)
- **Statistik & Multikolinearitas**: `statsmodels` (`VIF`)
- **Modeling & Tuning**: `sklearn` (`RandomForest`, `GridSearchCV`)
- **Deployment**:  
  - Model disimpan dengan `pickle`  
  - App dibangun dengan `Streamlit`, dan di-*deploy* melalui **Hugging Face Spaces**
