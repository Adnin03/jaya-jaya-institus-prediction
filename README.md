# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Tingginya kasus dropout berdampak pada reputasi institusi dan efisiensi pendidikan. Institusi membutuhkan cara untuk mendeteksi siswa yang berisiko dropout agar bisa ditangani lebih dini dan mendapat perhatian khusus.

### Cakupan Proyek
1. Mengidentifikasi faktor-faktor kunci yang berkorelasi dengan status dropout siswa.
2. Membuat model machine learning yang dapat meprediksi siswa yang kemungkinan akan melakukan dropout.
3. Memberikan insight kepada institusi melalui dashboard untuk membantu memonitori siswa

#### Data Understanding
Dataset yang digunakan berasal dari "Students' Performance" yang mencakup data demografi, ekonomi, dan performa akademik mahasiswa.

##### Temuan Utama (EDA):
- **Faktor Demografi:** Siswa laki-laki memiliki kecenderungan dropout yang jauh lebih tinggi dibandingkan siswa perempuan (rasio dropout melampaui 50% pada kelompok laki-laki).
- **Status Pernikahan:** Siswa yang sudah menikah (married) memiliki risiko dropout yang lebih besar dibandingkan siswa dengan status single.
- **Faktor Ekonomi:** Terdapat korelasi kuat antara kendala finansial dan dropout. Siswa yang memiliki tunggakan biaya sekolah (debtor) memiliki risiko dropout 3 kali lipat lebih besar. Sebaliknya, penerima beasiswa memiliki tingkat kelulusan yang sangat stabil.
- **Performa Akademik:** Jumlah mata kuliah yang lulus (approved) dan nilai rata-rata (grade) pada semester 2 merupakan indikator terkuat dalam menentukan apakah siswa akan lulus atau tidak.

#### Data Preparation
Beberapa langkah pembersihan data yang telah dilakukan:
- Memfilter status siswa dengan menghapus kategori 'Enrolled' untuk fokus pada klasifikasi biner (Graduate vs Dropout).
- Melakukan encoding pada label target: Dropout (1) dan Graduate (0).
- Melakukan seleksi fitur berdasarkan heatmap korelasi (mengambil fitur dengan koefisien > 0.1).
- Melakukan pembagian data (splitting) dengan rasio 80:20 dan teknik stratifikasi untuk menjaga keseimbangan label.

#### Modeling
Model yang digunakan dalam proyek ini adalah **Random Forest Classifier**. Proses pengembangan model meliputi:
- Hyperparameter tuning menggunakan GridSearchCV untuk mencari kombinasi optimal (n_estimators, max_depth, dll).
- Evaluasi menggunakan Confusion Matrix dan Classification Report.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
Setup environment:
Untuk menjalankan proyek ini, sangat disarankan menggunakan *virtual environment* agar dependensi tetap terisolasi dengan baik.
**Opsi 1: Menggunakan Anaconda**
Buka terminal/Anaconda Prompt lalu jalankan perintah berikut:
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

**Opsi 2: Menggunakan Pipenv (Shell/Terminal)**
Buka terminal lalu jalankan perintah berikut:
```bash
pip install pipenv
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Business Dashboard
Dashboard dibuat menggunakan Looker Studio untuk memantau kesehatan akademik mahasiswa secara real-time. Dashboard ini menyoroti korelasi antara status pembayaran SPP, jumlah mata kuliah yang lulus di semester awal, dan status akhir mahasiswa.

Link Dashboard: https://datastudio.google.com/reporting/18c93fa7-e679-4634-a219-3d73d71c073a

## Menjalankan Sistem Machine Learning
Aplikasi prototype dibuat menggunakan Streamlit. User dapat memasukkan data akademik dan finansial mahasiswa untuk mendapatkan prediksi instan.
**Cara Menajalankan Skrip / Web App (Streamlit):**
```bash
streamlit run app.py
```

Link streamlit: https://jaya-jaya-institus-prediction-adnin.streamlit.app/

## Conclusion
Berdasarkan analisis Exploratory Data Analysis (EDA) dan Business Dashboard yang telah dibangun, berikut adalah temuan mendalam terkait masalah dropout di Jaya Jaya Institut:

**1. Faktor Finansial sebagai Prediktor Utama:**
Karakteristik paling mencolok dari mahasiswa yang melakukan dropout adalah kendala finansial. Mahasiswa yang memiliki status menunggak SPP (Tuition fees up to date = No) memiliki risiko dropout yang sangat ekstrem. Secara visual, hampir seluruh mahasiswa dalam kategori penunggak gagal menyelesaikan studinya, terlepas dari seberapa baik performa akademik mereka di awal semester.

**2. Titik Kritis Akademik di Semester Awal:**
Terdapat hubungan linear yang kuat antara jumlah mata kuliah yang lulus di semester 1 dengan keberlanjutan studi. Mahasiswa yang lulus kurang dari 3 mata kuliah di semester pertama berada dalam "zona merah". Sebaliknya, mahasiswa yang berhasil mengamankan kelulusan di atas 5 mata kuliah memiliki probabilitas Graduate yang jauh lebih stabil. Hal ini menunjukkan bahwa beban perkuliahan di semester awal menjadi fase adaptasi yang menentukan.

**3. Pengaruh Dukungan Beasiswa:**
Dukungan finansial berupa beasiswa terbukti menjadi "jaring pengaman" yang efektif. Rasio dropout pada kelompok bukan penerima beasiswa (Scholarship holder = No) jauh lebih tinggi. Hal ini memperkuat temuan bahwa stabilitas ekonomi berbanding lurus dengan ketenangan mahasiswa dalam menempuh pendidikan hingga lulus.

### Rekomendasi Action Items
Untuk menekan angka dropout di Jaya Jaya Institut, berikut adalah langkah strategis yang direkomendasikan bagi manajemen kampus:

**1. Restrukturisasi Kebijakan Keuangan (Skema Cicilan):**
Mengingat tunggakan SPP adalah pemicu utama dropout, institusi disarankan untuk mengimplementasikan kebijakan cicilan SPP yang lebih fleksibel bagi mahasiswa yang masuk dalam kategori Debtor. Pemberian keringanan atau penundaan pembayaran sementara bagi mahasiswa dengan IPK di atas 3.0 namun terkendala biaya, dapat menyelamatkan potensi kelulusan mahasiswa tersebut.

**2. Program Mentoring Akademik Intensif:**
Kampus perlu mengaktifkan sistem pendampingan khusus bagi mahasiswa yang lulus di bawah 3 mata kuliah pada semester pertama. Evaluasi tidak boleh menunggu hingga akhir tahun; intervensi berupa tambahan jam pelajaran atau konseling akademik harus dilakukan segera setelah nilai semester satu keluar untuk mencegah akumulasi kegagalan di semester berikutnya.

**3. Optimalisasi Model ML sebagai Early Warning System:**
Tim administrasi akademik harus mulai mengoperasionalisasikan model prediksi Machine Learning yang telah dibangun. Mahasiswa yang masuk dalam radar risiko tinggi (probabilitas dropout > 0.7) harus secara otomatis masuk ke dalam daftar prioritas untuk dipanggil oleh Dosen Wali. Sesi consultation proaktif harus dijadwalkan maksimal 14 hari setelah sistem memberikan peringatan untuk mengidentifikasi akar masalah sebelum mahasiswa memutuskan untuk berhenti.