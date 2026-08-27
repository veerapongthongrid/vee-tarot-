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
        font-size: 24px;
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
        font-size: 14px;
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
        margin-top: 10px;
        margin-bottom: 15px;
    }
    
    div.stButton > button:hover {
        background: linear-gradient(135deg, #6A1B9A 0%, #4A0E4E 100%);
        box-shadow: 0 0 20px rgba(186, 104, 200, 0.6);
        border-color: #BA68C8 !important;
    }

    /* กล่องการ์ดแต่ละใบ */
    .card-box {
        background: rgba(44, 12, 62, 0.6);
        border: 1px solid #8A2BE2;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(138, 43, 226, 0.25);
    }

    .card-img {
        width: 140px;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(138, 43, 226, 0.6);
        border: 1px solid #BA68C8;
        margin-top: 10px;
    }

    .card-title {
        font-size: 18px;
        font-weight: bold;
        color: #F3E5F5;
        margin-bottom: 4px;
    }

    .card-sub {
        font-size: 14px;
        color: #BA68C8;
        margin-bottom: 10px;
    }

    h3 {
        color: #E1BEE7 !important;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ฐานข้อมูลรูปภาพไพ่ยิปซีมาตรฐาน ครบ 78 ใบ (Major 22 + Minor 56)
TAROT_IMAGES = {
    # Major Arcana (22 ใบ)
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
    # Wands - ไม้เท้า (14 ใบ)
    "Ace of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/1/11/Wands01.jpg"
    ),
    "Two of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/0/0f/Wands02.jpg"
    ),
    "Three of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/ff/ff/Wands03.jpg"
    ),
    "Four of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/a/a4/Wands04.jpg"
    ),
    "Five of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/9/9d/Wands05.jpg"
    ),
    "Six of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/3/3b/Wands06.jpg"
    ),
    "Seven of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/e/e4/Wands07.jpg"
    ),
    "Eight of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/6/6b/Wands08.jpg"
    ),
    "Nine of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/4/4d/Wands09.jpg"
    ),
    "Ten of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/0/0b/Wands10.jpg"
    ),
    "Page of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/6/6a/Wands11.jpg"
    ),
    "Knight of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/1/16/Wands12.jpg"
    ),
    "Queen of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/0/0d/Wands13.jpg"
    ),
    "King of Wands": (
        "https://upload.wikimedia.org/wikipedia/commons/c/ce/Wands14.jpg"
    ),
    # Cups - ถ้วย (14 ใบ)
    "Ace of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/3/36/Cups01.jpg"
    ),
    "Two of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/f/f8/Cups02.jpg"
    ),
    "Three of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/7/7a/Cups03.jpg"
    ),
    "Four of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/3/35/Cups04.jpg"
    ),
    "Five of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/d/d7/Cups05.jpg"
    ),
    "Six of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/1/17/Cups06.jpg"
    ),
    "Seven of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/a/ae/Cups07.jpg"
    ),
    "Eight of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/6/60/Cups08.jpg"
    ),
    "Nine of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/2/24/Cups09.jpg"
    ),
    "Ten of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/8/84/Cups10.jpg"
    ),
    "Page of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/a/ad/Cups11.jpg"
    ),
    "Knight of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/f/fa/Cups12.jpg"
    ),
    "Queen of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/6/62/Cups13.jpg"
    ),
    "King of Cups": (
        "https://upload.wikimedia.org/wikipedia/commons/0/04/Cups14.jpg"
    ),
    # Swords - ดาบ (14 ใบ)
    "Ace of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/1/1a/Swords01.jpg"
    ),
    "Two of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/9/9e/Swords02.jpg"
    ),
    "Three of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/0/02/Swords03.jpg"
    ),
    "Four of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/b/bf/Swords04.jpg"
    ),
    "Five of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/2/23/Swords05.jpg"
    ),
    "Six of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/2/29/Swords06.jpg"
    ),
    "Seven of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/3/34/Swords07.jpg"
    ),
    "Eight of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/a/a7/Swords08.jpg"
    ),
    "Nine of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/2/2f/Swords09.jpg"
    ),
    "Ten of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/d/d4/Swords10.jpg"
    ),
    "Page of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/4/4c/Swords11.jpg"
    ),
    "Knight of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/b/b0/Swords12.jpg"
    ),
    "Queen of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/d/d4/Swords13.jpg"
    ),
    "King of Swords": (
        "https://upload.wikimedia.org/wikipedia/commons/3/33/Swords14.jpg"
    ),
    # Pentacles - เหรียญ (14 ใบ)
    "Ace of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/f/fd/Pentalces01.jpg"
    ),
    "Two of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/9/9f/Pentalces02.jpg"
    ),
    "Three of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/4/42/Pentalces03.jpg"
    ),
    "Four of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/3/35/Pentalces04.jpg"
    ),
    "Five of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/9/96/Pentalces05.jpg"
    ),
    "Six of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/a/a6/Pentalces06.jpg"
    ),
    "Seven of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/6/6a/Pentalces07.jpg"
    ),
    "Eight of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/4/49/Pentalces08.jpg"
    ),
    "Nine of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/f/f0/Pentalces09.jpg"
    ),
    "Ten of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/4/42/Pentalces10.jpg"
    ),
    "Page of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/e/ec/Pentalces11.jpg"
    ),
    "Knight of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/d/d5/Pentalces12.jpg"
    ),
    "Queen of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/8/88/Pentalces13.jpg"
    ),
    "King of Pentacles": (
        "https://upload.wikimedia.org/wikipedia/commons/1/1c/Pentalces14.jpg"
    ),
}

full_deck = list(TAROT_IMAGES.keys())

# สร้าง Session State เก็บสถานะการสุ่มไพ่
if "drawn_3" not in st.session_state:
    st.session_state.drawn_3 = None
if "drawn_2" not in st.session_state:
    st.session_state.drawn_2 = None

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

# ปุ่มหลักสำหรับเปิดไพ่ 3 ใบ
if st.button("🔮 เปิดไพ่ 3 ใบ", use_container_width=True):
    st.session_state.drawn_3 = random.sample(full_deck, 3)
    st.session_state.drawn_2 = None  # ล้างค่าทำนายเพิ่มเก่าเมื่อสุ่ม 3 ใบใหม่

# แสดงผลไพ่ 3 ใบ
if st.session_state.drawn_3:
    st.markdown("### 🎴 ผลการเปิดไพ่ของคุณ (3 ใบ)")
    st.write("---")

    for i, card in enumerate(st.session_state.drawn_3):
        img_url = TAROT_IMAGES.get(card)
        st.markdown(
            f'<div class="card-box">'
            f'<div class="card-title">ใบที่ {i+1}</div>'
            f'<div class="card-sub">{card}</div>'
            f'<img src="{img_url}" class="card-img">'
            f"</div>",
            unsafe_allow_html=True,
        )

    # ปุ่มเปิดไพ่เพิ่ม 2 ใบ จะแสดงต่อเมื่อเปิดไพ่ 3 ใบเรียบร้อยแล้วเท่านั้น
    st.write("---")
    if st.button("✨ เปิดไพ่ทำนายเพิ่ม 2 ใบ", use_container_width=True):
        # สุ่มไพ่เพิ่ม 2 ใบโดยไม่ซ้ำกับ 3 ใบแรก
        remaining_deck = [
            c for c in full_deck if c not in st.session_state.drawn_3
        ]
        st.session_state.drawn_2 = random.sample(remaining_deck, 2)

# แสดงผลไพ่เพิ่ม 2 ใบที่ด้านล่างสุด
if st.session_state.drawn_2:
    st.markdown("### ✨ ผลการเปิดไพ่ทำนายเพิ่ม (2 ใบ)")
    st.write("---")

    for i, card in enumerate(st.session_state.drawn_2):
        img_url = TAROT_IMAGES.get(card)
        st.markdown(
            f'<div class="card-box">'
            f'<div class="card-title">ใบเพิ่ม {i+1}</div>'
            f'<div class="card-sub">{card}</div>'
            f'<img src="{img_url}" class="card-img">'
            f"</div>",
            unsafe_allow_html=True,
        )
        
