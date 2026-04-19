import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title='Student Dropout Predictor', layout='wide')

@st.cache_resource
def load_model():
    model_path = os.path.join('model', 'model_rf.joblib')
    return joblib.load(model_path)

model = load_model()

st.title("🎓 Student Dropout Prediction Dashboard")
st.markdown("""Dashboard ini digunakan untuk memprediksi potensi keberlanjutan studi mahasiswa berdasarkan faktor ekonomi, demografi, dan performa akademik semester awal.""")
st.divider()

st.sidebar.header('Input Data Mahasisiswa')

def user_input_features():
    app_mode_map = {
        1: "1st phase - general quota",
        2: "2nd phase - general quota",
        5: "Over 23 years old",
        7: "Holders of other higher courses",
        17: "Transfer",
        18: "Change of course",
        43: "International student",
        44: "Short cycle diploma holders"
    }
    
    app_mode_selection = st.sidebar.selectbox(
        "Jalur Pendaftaran (Application Mode)", 
        options=list(app_mode_map.keys()),
        format_func=lambda x: app_mode_map[x]
    )
    
    st.sidebar.subheader("Faktor Ekonomi & Demografi")
    gender = st.sidebar.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 1 else "Female")
    debtor = st.sidebar.selectbox("Punya Hutang SPP (Debtor)?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    tuition = st.sidebar.selectbox("Biaya SPP Terbayar?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    scholarship = st.sidebar.selectbox("Penerima Beasiswa?", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    age = st.sidebar.slider("Usia saat Pendaftaran", 17, 60, 20)

    st.sidebar.subheader("Performa Akademik")
    sem1_app = st.sidebar.number_input("Mata Kuliah Lulus Sem 1", min_value=0, max_value=20, value=5)
    sem1_grade = st.sidebar.slider("Nilai Rata-rata Sem 1", 0.0, 20.0, 12.0)
    sem2_app = st.sidebar.number_input("Mata Kuliah Lulus Sem 2", min_value=0, max_value=20, value=5)
    sem2_grade = st.sidebar.slider("Nilai Rata-rata Sem 2", 0.0, 20.0, 12.0)
    
    data = {
        'Application_mode': app_mode_selection,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age,
        'Curricular_units_1st_sem_approved': sem1_app,
        'Curricular_units_1st_sem_grade': sem1_grade,
        'Curricular_units_2nd_sem_approved': sem2_app,
        'Curricular_units_2nd_sem_grade': sem2_grade
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("Data Input")
    st.write(input_df.T)
    
with col2:
    st.subheader("Hasil Prediksi")
    if st.button("Lakukan Prediksi"):
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        if prediction[0] == 1:
            st.error("⚠️ Potensi: **DROPOUT**")
        else:
            st.success("✅ Potensi: **GRADUATE**")
            
        st.write(f"Probabilitas Dropout: {prediction_proba[0][1]:.2%}")
        st.write(f"Probabilitas Graduate: {prediction_proba[0][0]:.2%}")
        
st.divider()
st.info("Catatan: Gunakan hasil ini sebagai referensi awal bimbingan akademik.")