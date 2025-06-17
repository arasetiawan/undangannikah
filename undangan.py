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
    <div style="position: relative; text-align: center;">
        <img src="data:image/png;base64,{bg_img}" style="width: 100%; border-radius: 10px;" />
        <div style="position: absolute; top: 70%; left: 50%; transform: translate(-50%, -50%);">
            <form action="">
                <button style="
                    background-color: #E91E63;
                    color: white;
                    padding: 8px 20px;
                    border-radius: 8px;
                    font-size: 18px;
                    border: none;
                    cursor: pointer;
                ">Buka Undangan</button>
            </form>
        </div>
    </div>
""", unsafe_allow_html=True)
