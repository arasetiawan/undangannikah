import streamlit as st
import base64

st.set_page_config(layout="centered", page_title="Undangan Ara & Pasangan")

# Fungsi base64
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64("background.png")

# Tampilkan gambar dengan tombol di atasnya
st.markdown(f"""
    <style>
    html, body {{
        margin: 0 !important;
        padding: 0 !important;
        height: 100vh;
        width: 100vw;
        overflow: hidden;
    }}

    .main .block-container {{
        margin: 0 !important;
        padding: 0 !important;
        height: 100vh !important;
        width: 100vw !important;
        max-width: 100vw !important;
        overflow: hidden;
    }}

    .fullscreen-img {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        object-fit: contain;
        display: block;
        z-index: -1;
    }}

    @keyframes floating {{
        0%   {{ transform: translate(-50%, -50%) translateY(0); }}
        50%  {{ transform: translate(-50%, -50%) translateY(-10px); }}
        100% {{ transform: translate(-50%, -50%) translateY(0); }}
    }}

    @keyframes fadeInTop {{
        0%   {{ opacity: 0; transform: translateY(-50px); }}
        100% {{ opacity: 1; transform: translateY(0); }}
    }}

    .animated-btn {{
        animation: floating 2.5s ease-in-out infinite;
    }}

    .bride-groom {{
        font-family: 'Georgia', serif;
        font-size: 28px;
        color: white;
        text-shadow: 1px 1px 4px black;
        animation: fadeInTop 1.5s ease-out forwards;
        position: absolute;
        top: 15%;
        left: 50%;
        transform: translateX(-50%);
    }}

    .btn {{
        background-color: #E91E63;
        color: white;
        padding: 10px 24px;
        border-radius: 8px;
        font-size: 12px;
        border: none;
        cursor: pointer;
        transition: 0.3s ease;
    }}

    .btn:hover {{
        background-color: #FFFFE0;
        color: #E91E63;
        transform: scale(1.05);
    }}
    </style>

    <!-- Gambar Latar -->
    <img src="data:image/png;base64,{bg_img}" class="fullscreen-img" />

    <!-- Nama Pengantin -->
    <div class="bride-groom">
        Ara & Pasangan
    </div>

    <!-- Tombol -->
    <div class="animated-btn" style="position: absolute; top: 75%; left: 50%; transform: translate(-50%, -50%);">
        <form action="">
            <button class="btn">Buka Undangan</button>
        </form>
    </div>
""", unsafe_allow_html=True)

