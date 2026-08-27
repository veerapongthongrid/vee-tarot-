import random
import streamlit as st

st.set_page_config(
    page_title="เปิดไพ่ทำนายดวง โดยพี่หมอวีร์",
    page_icon="🔮",
    initial_sidebar_state="collapsed",
)

# สไตล์แต่งปุ่มให้สวยงามบนมือถือ
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
    .btn-main {
        background-color: #4B0082;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# หัวข้อใหม่ตามต้องการ
st.title("🔮 เปิดไพ่ทำนายดวง")
st.subheader("โดยพี่หมอวีร์")
st.write("ตั้งจิตอธิษฐานนึกถึงเรื่องที่ต้องการถาม แล้วกดปุ่มเปิดไพ่ได้เลยครับ")

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

# ปุ่มกดเลือกเปิดไพ่
col1, col2 = st.columns(2)

with col1:
    btn_3_cards = st.button("🔮 เปิดไพ่ 3 ใบ", use_container_width=True)

with col2:
    btn_2_cards = st.button("✨ เปิดไพ่ทำนายเพิ่ม 2 ใบ", use_container_width=True)

# การทำงานเมื่อกดปุ่มเปิดไพ่ 3 ใบ
if btn_3_cards:
    drawn = random.sample(full_deck, 3)
    st.success("🎴 ผลการเปิดไพ่ของคุณ (3 ใบ)")
    st.write("---")
    for i, card in enumerate(drawn, 1):
        st.markdown(f"### ใบที่ {i}: **{card}**")
        st.image(
            "https://raw.githubusercontent.com/effata/tarot-cards/main/cards/c01.jpg",
            caption=card,
            width=220,
        )
        st.write("---")

# การทำงานเมื่อกดปุ่มเปิดไพ่ทำนายเพิ่ม 2 ใบ
if btn_2_cards:
    drawn = random.sample(full_deck, 2)
    st.info("✨ ผลการเปิดไพ่ทำนายเพิ่ม (2 ใบ)")
    st.write("---")
    for i, card in enumerate(drawn, 1):
        st.markdown(f"### ใบที่ขยายความเพิ่มเติม {i}: **{card}**")
        st.image(
            "https://raw.githubusercontent.com/effata/tarot-cards/main/cards/c01.jpg",
            caption=card,
            width=220,
        )
        st.write("---")
