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
    @keyframes scaleIn {{
        0%   {{ transform: translate(-50%, -50%) scale(0); opacity: 0; }}
        60%  {{ transform: translate(-50%, -50%) scale(1.05); opacity: 1; }}
        100% {{ transform: translate(-50%, -50%) scale(1); }}
    }}

    .scale-in {{
        animation: scaleIn 0.8s ease-out forwards;
    }}

    .btn {{
        background-color: #E91E63;
        color: white;
        padding: 10px 24px;
        border-radius: 8px;
        font-size: 18px;
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

    <div style="position: relative; text-align: center;">
        <img src="data:image/png;base64,{bg_img}" style="width: 100%; border-radius: 10px;" />
        <div style="position: absolute; top: 70%; left: 50%; transform: translate(-50%, -50%);" class="scale-in">
            <form action="">
                <button class="btn">Buka Undangan</button>
            </form>
        </div>
    </div>
""", unsafe_allow_html=True)

