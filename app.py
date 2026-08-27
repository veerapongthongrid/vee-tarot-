import random
import streamlit as st

st.set_page_config(
    page_title="เปิดไพ่ทำนายดวง โดยพี่หมอวีร์",
    page_icon="🔮",
    initial_sidebar_state="collapsed",
)

# สไตล์แต่งปุ่มและจัดหัวข้อให้อยู่กึ่งกลาง
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        font-size: 18px;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
    }
    .main-title {
        text-align: center;
        font-size: 26px;
        font-weight: bold;
        color: #31333F;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    .sub-text {
        text-align: center;
        color: #555555;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อจัดกึ่งกลาง ขนาดเท่ากัน มีไอคอนหน้า-หลัง
st.markdown(
    '<div class="main-title">🔮 เปิดไพ่ทำนายดวง โดยพี่หมอวีร์ 🔮</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-text">ตั้งจิตอธิษฐานนึกถึงเรื่องที่ต้องการถาม แล้วกดปุ่มเปิดไพ่ได้เลยครับ</div>',
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

st.write("---")

col1, col2 = st.columns(2)

with col1:
    btn_3_cards = st.button("🔮 เปิดไพ่ 3 ใบ", use_container_width=True)

with col2:
    btn_2_cards = st.button("✨ เปิดไพ่ทำนายเพิ่ม 2 ใบ", use_container_width=True)

if btn_3_cards:
    drawn = random.sample(full_deck, 3)
    st.success("🎴 ผลการเปิดไพ่ของคุณ (3 ใบ)")
    st.write("---")
    for i, card in enumerate(drawn, 1):
        st.markdown(f"### ใบที่ {i}: **{card}**")
        st.image("https://picsum.photos/id/1025/300/450", caption=card, width=200)
        st.write("---")

if btn_2_cards:
    drawn = random.sample(full_deck, 2)
    st.info("✨ ผลการเปิดไพ่ทำนายเพิ่ม (2 ใบ)")
    st.write("---")
    for i, card in enumerate(drawn, 1):
        st.markdown(f"### ใบที่ขยายความเพิ่มเติม {i}: **{card}**")
        st.image("https://picsum.photos/id/1025/300/450", caption=card, width=200)
        st.write("---")
