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
    /* พื้นหลังทั้งแอปเป็นโทนอวกาศ ลึกลับ */
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
    
    /* แต่งหัวข้อหลักเรืองแสง */
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

    /* ปรับแต่งปุ่มกดสไตล์เวทมนตร์ */
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

    /* ปรับแต่งการแสดงผลรูปภาพให้มีออร่า */
    [data-testid="stImage"] img {
        border-radius: 12px;
        box-shadow: 0 0 15px rgba(138, 43, 226, 0.5);
        border: 1px solid #6A1B9A;
    }
    
    /* ปรับสีฟอนต์ส่วนอื่นๆ */
    h3 {
        color: #E1BEE7 !important;
    }
    p, span {
        color: #E0D5F5;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อหลัก
st.markdown(
    '<div class="main-title">✨ 🔮 เปิดไพ่ทำนายดวง โดยพี่หมอวีร์ 🔮 ✨</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-text">🌌 ตั้งจิตอธิษฐานนึกถึงเรื่องที่ต้องการถาม แล้วกดปุ่มเปิดไพ่ได้เลยครับ 🌌</div>',
    unsafe_allow_html=True,
)

# รายชื่อไพ่ 78 ใบ
major_arcana = [
    "0. The Fool",
    "1. The Magician",
    "2. The High Priestess",
    "3. The Empress",
    "4. The Emperor",
    "5. The Hierophant",
    "6. The Lovers",
    "7. The Chariot",
    "8. Strength",
    "9. The Hermit",
    "10. Wheel of Fortune",
    "11. Justice",
    "12. The Hanged Man",
    "13. Death",
    "14. Temperance",
    "15. The Devil",
    "16. The Tower",
    "17. The Star",
    "18. The Moon",
    "19. The Sun",
    "20. Judgement",
    "21. The World",
]

suits = ["Wands", "Cups", "Swords", "Pentacles"]
ranks = [
    "Ace",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "Page",
    "Knight",
    "Queen",
    "King",
]
minor_arcana = [f"{rank} of {suit}" for suit in suits for rank in ranks]
full_deck = major_arcana + minor_arcana

# ลิงก์รูปภาพไพ่/เวทมนตร์จาก Unsplash CDN ที่ไม่มีวันโดนบล็อกและโหลดเร็ว
TAROT_CARD_URL = (
    "https://images.unsplash.com/photo-1635863138275-d9b33299680b?w=400&q=80"
)

st.write("---")

col1, col2 = st.columns(2)

with col1:
    btn_3_cards = st.button("🔮 เปิดไพ่ 3 ใบ", use_container_width=True)

with col2:
    btn_2_cards = st.button("✨ เปิดไพ่ทำนายเพิ่ม 2 ใบ", use_container_width=True)

if btn_3_cards:
    drawn = random.sample(full_deck, 3)
    st.markdown("### 🎴 ผลการเปิดไพ่ของคุณ (3 ใบ)")
    st.write("---")
    for i, card in enumerate(drawn, 1):
        st.markdown(f"### ใบที่ {i}: **{card}**")
        st.image(TAROT_CARD_URL, caption=card, width=220)
        st.write("---")

if btn_2_cards:
    drawn = random.sample(full_deck, 2)
    st.markdown("### ✨ ผลการเปิดไพ่ทำนายเพิ่ม (2 ใบ)")
    st.write("---")
    for i, card in enumerate(drawn, 1):
        st.markdown(f"### ใบที่ขยายความเพิ่มเติม {i}: **{card}**")
        st.image(TAROT_CARD_URL, caption=card, width=220)
        st.write("---")
        
