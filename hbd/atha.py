import streamlit as st
from PIL import Image

# Judul aplikasi
st.title("🎉 Happy Milad! 🎉")

# Ucapan ulang tahun
st.subheader("Selamat Ulang Tahun Atha Fajri Putri! 🎂🎁")
st.write("Semoga panjang umur dan sehat selaluuu, wish u all the best Jri!!!")

# Memainkan musik Happy Birthday
audio_file = open('Happy Birthday.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/mp3')

# Menampilkan gambar
st.image("kelan.jpg", use_column_width=True)
st.image("bedugul.jpg", use_column_width=True)
st.image("kint.jpg", use_column_width=True)
st.image("peninsula.jpg", use_column_width=True)
st.image("gradu.jpg", use_column_width=True)
st.image("bedugul.jpg", use_column_width=True)
st.image("peninsula2.jpg", use_column_width=True)
st.image("tsm.jpg", use_column_width=True)
st.image("upz.jpg", use_column_width=True)

# Efek balon
st.balloons()


