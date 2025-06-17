import streamlit as st
import base64

st.set_page_config(layout="centered", page_title="Undangan Ara & Pasangan")

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64("background.png")

st.markdown(f"""
    <style>
    /* Reset seluruh halaman agar tidak bisa discroll */
    html, body {{
        margin: 0 !important;
        padding: 0 !important;
        height: 100vh;
        width: 100vw;
        overflow: hidden !important;
    }}

    .main .block-container {{
        margin: 0 !important;
        padding: 0 !important;
        height: 100vh !important;
        width: 100vw !important;
        max-width: 100vw !important;
        overflow: hidden !important;
    }}

    /* Gambar fullscreen & terkunci */
    .fullscreen-img {{
        position: absolute;
        top: 0; left: 0;
        width: 100vw;
        height: 100vh;
        object-fit: cover;
        z-index: -1;
    }}

    /* Tombol mengambang dengan animasi floating */
    @keyframes floating {{
        0% {{ transform: translate(-50%, -50%) translateY(0); }}
        50% {{ transform: translate(-50%, -50%) translateY(-10px); }}
        100% {{ transform: translate(-50%, -50%) translateY(0); }}
    }}

    .floating-btn {{
        position: absolute;
        top: 75%;
        left: 50%;
        transform: translate(-50%, -50%);
        animation: floating 2s ease-in-out infinite;
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

    <!-- Struktur konten -->
    <img src="data:image/png;base64,{bg_img}" class="fullscreen-img" />
    <div class="floating-btn">
        <form action="">
            <button class="btn">Buka Undangan</button>
        </form>
    </div>
""", unsafe_allow_html=True)



