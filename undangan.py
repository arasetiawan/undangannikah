import streamlit as st
import base64

st.set_page_config(layout="centered", page_title="Undangan Ara & Pasangan")

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64("background.png")

st.markdown(f"""
    <style>
    html, body {{
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important;
        height: 100vh;
        width: 100vw;
    }}

    .main .block-container {{
        margin: 0 !important;
        padding: 0 !important;
        max-width: 100vw !important;
        height: 100vh !important;
    }}

    .fullscreen-img {{
        width: 100vw;
        height: 100vh;
        object-fit: cover;
        display: block;
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

    <div style="position: relative; width: 100vw; height: 100vh;">
        <img src="data:image/png;base64,{bg_img}" class="fullscreen-img" />
        <div style="position: absolute; top: 75%; left: 50%; transform: translate(-50%, -50%);">
            <form action="">
                <button class="btn">Buka Undangan</button>
            </form>
        </div>
    </div>
""", unsafe_allow_html=True)


