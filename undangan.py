import streamlit as st
from datetime import datetime
import base64

st.set_page_config(layout="centered", page_title="Undangan Ara & Pasangan")

# Fungsi untuk encode gambar jadi base64 (untuk background)
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64("assets/background.png")

# Tambahkan CSS untuk background & tombol tengah
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_img}");
        background-size: contain;
        background-attachment: fixed;
        background-position: center;
    }}
    .centered {{ 
        text-align: center; 
        margin-top: 75vh;
        }}
    .btn {{
        background-color: #E91E63;
        color: white;
        padding: 6px 15px;
        border-radius: 8px;
        font-size: 18px;
        border: none;
        cursor: pointer;
    }}
    .btn:hover {{
        background-color: #FFFFE0;
        transform: scale(1.03);
        transition: all 0.3s ease;
    }}

    </style>
""", unsafe_allow_html=True)

# Isi konten undangan
st.markdown(f"""
    <div class="centered">
        <form action="">
            <button class="btn">Buka Undangan</button>
        </form>
    </div>
""", unsafe_allow_html=True)