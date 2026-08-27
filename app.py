import random
import streamlit as st

st.set_page_config(
    page_title="เปิดไพ่ทำนายดวง โดยพี่หมอวีร์",
    page_icon="🔮",
    initial_sidebar_state="collapsed",
)

# แต่งพื้นหลังธีมหมอดู ลึกลับ อวกาศ ดวงดาว
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0D0814;
        background-image: 
            radial-gradient(white, rgba(255,255,255,.2) 2px, transparent 40px),
            radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 30px),
            radial-gradient(white, rgba(255,255,255,.1) 2px, transparent 40px),
            radial-gradient(ellipse at bottom, #1B003A 0%, #0D0814 100%);
        background-size: 550px 550px, 350px 350px, 250px 250px, 100% 100%;
        background-position: 0 0, 40px 60px, 130px 270px, 0 0;
        color: #E0D5F5;
    }
    
    .main-title {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #F3E5F5;
        text-shadow: 0 0 10px #8A2BE2, 0 0 20px #8A2BE2;
        margin-top: 15px;
        margin-bottom: 10px;
    }
    
    .sub-text {
        text-align: center;
        color: #C8B6E2;
        margin-bottom: 25px;
        font-size: 15px;
    }

    div.stButton > button {
        width: 100%;
        font-size: 18px;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px;
        background: linear-gradient(135deg, #4A0E4E 0%, #2C0C3E 100%);
        color: #F3E5F5 !important;
        border: 1px solid #8A2BE2 !important;
        box-shadow: 0 4px 15px rgba(138, 43, 226, 0.3);
        margin-bottom: 10px;
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #6A1B9A 0%, #4A0E4E 100%);
        box-shadow: 0 0 20px rgba(186, 104, 200, 0.6);
        border-color: #BA68C8 !important;
    }

    [data-testid="stImage"] img {
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(138, 43, 226, 0.5);
        border: 1px solid #6A1B9A;
    }

    h3, h4 {
        color: #E1BEE7 !important;
        text-align: center;
    }
    p, span {
        color: #E0D5F5;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ฐานข้อมูลรูปภาพไพ่ยิปซี (Wikimedia)
TAROT_IMAGES = {
    "0. The Fool": (
        "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg"
    ),
    "1. The Magician": (
        "https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg"
    ),
    "2. The High Priestess": (
        "https://upload.wikimedia.org/wikipedia/commons/8/88/RWS_Tarot_02_High_Priestess.jpg"
    ),
    "3. The Empress": (
        "https://upload.wikimedia.org/wikipedia/commons/d/d2/RWS_Tarot_03_Empress.jpg"
    ),
    "4. The Emperor": (
        "https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg"
    ),
    "5. The Hierophant": (
        "https://upload.wikimedia.org/wikipedia/commons/8/8d/RWS_Tarot_05_Hierophant.jpg"
    ),
    "6. The Lovers": (
        "https://upload.wikimedia.org/wikipedia/commons/3/3a/TheLovers.jpg"
    ),
    "7. The Chariot": (
        "https://upload.wikimedia.org/wikipedia/commons/9/9b/RWS_Tarot_07_Chariot.jpg"
    ),
    "8. Strength": (
        "https://upload.wikimedia.org/wikipedia/commons/f/f5/RWS_Tarot_08_Strength.jpg"
    ),
    "9. The Hermit": (
        "https://upload.wikimedia.org/wikipedia/commons/4/4d/RWS_Tarot_09_Hermit.jpg"
    ),
    "10. Wheel of Fortune": (
        "https://upload.wikimedia.org/wikipedia/commons/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg"
    ),
    "11. Justice": (
        "https://upload.wikimedia.org/wikipedia/commons/e/e0/RWS_Tarot_11_Justice.jpg"
    ),
    "12. The Hanged Man": (
        "https://upload.wikimedia.org/wikipedia/commons/2/2b/RWS_Tarot_12_Hanged_Man.jpg"
    ),
    "13. Death": (
        "https://upload.wikimedia.org/wikipedia/commons/d/d7/RWS_Tarot_13_Death.jpg"
    ),
    "14. Temperance": (
        "https://upload.wikimedia.org/wikipedia/commons/f/f8/RWS_Tarot_14_Temperance.jpg"
    ),
    "15. The Devil": (
        "https://upload.wikimedia.org/wikipedia/commons/5/55/RWS_Tarot_15_Devil.jpg"
    ),
    "16. The Tower": (
        "https://upload.wikimedia.org/wikipedia/commons/5/53/RWS_Tarot_16_Tower.jpg"
    ),
    "17. The Star": (
        "https://upload.wikimedia.org/wikipedia/commons/d/db/RWS_Tarot_17_Star.jpg"
    ),
    "18. The Moon": (
        "https://upload.wikimedia.org/wikipedia/commons/7/7f/RWS_Tarot_18_Moon.jpg"
    ),
    "19. The Sun": (
        "https://upload.wikimedia.org/wikipedia/commons/1/17/RWS_Tarot_19_Sun.jpg"
    ),
    "20. Judgement": (
        "https://upload.wikimedia.org/wikipedia/commons/d/dd/RWS_Tarot_20_Judgement.jpg"
    ),
    "21. The World": (
        "https://upload.wikimedia.org/wikipedia/commons/ff/ff/RWS_Tarot_21_World.jpg"
    ),
    "DEFAULT": (
        "https://upload.wikimedia.org/wikipedia/commons/5/54/Card_back_06.svg"
    ),
}

full_deck = list(TAROT_IMAGES.keys())
full_deck.remove("DEFAULT")

# หัวข้อหลัก
st.markdown(
    '<div class="main-title">✨ 🔮 เปิดไพ่ทำนายดวง โดยพี่หมอวีร์ 🔮 ✨</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-text">🌌 ตั้งจิตอธิษฐานนึกถึงเรื่องที่ต้องการถาม แล้วกดปุ่มเปิดไพ่ได้เลยครับ 🌌</div>',
    unsafe_allow_html=True,
)

st.write("---")

col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    btn_3_cards = st.button("🔮 เปิดไพ่ 3 ใบ", use_container_width=True)

with col_btn2:
    btn_2_cards = st.button("✨ เปิดไพ่ทำนายเพิ่ม 2 ใบ", use_container_width=True)

if btn_3_cards:
    drawn = random.sample(full_deck, 3)
    st.markdown("### 🎴 ผลการเปิดไพ่ของคุณ (3 ใบ)")
    st.write("---")

    # สร้าง 3 คอลัมน์เรียงแถวเดียวกัน
    cols = st.columns(3)
    for i, card in enumerate(drawn):
        with cols[i]:
            st.markdown(f"**ใบที่ {i+1}**")
            st.markdown(f"*{card}*")
            img_url = TAROT_IMAGES.get(card, TAROT_IMAGES["DEFAULT"])
            st.image(img_url, use_column_width=True)

if btn_2_cards:
    drawn = random.sample(full_deck, 2)
    st.markdown("### ✨ ผลการเปิดไพ่ทำนายเพิ่ม (2 ใบ)")
    st.write("---")

    # สร้าง 2 คอลัมน์เรียงแถวเดียวกัน
    cols = st.columns(2)
    for i, card in enumerate(drawn):
        with cols[i]:
            st.markdown(f"**ใบที่เพิ่ม {i+1}**")
            st.markdown(f"*{card}*")
            img_url = TAROT_IMAGES.get(card, TAROT_IMAGES["DEFAULT"])
            st.image(img_url, use_column_width=True)
            
