import random
import streamlit as st

st.set_page_config(
    page_title="ดูดวงไพ่ยิปซี", page_icon="🔮", initial_sidebar_state="collapsed"
)

# สไตล์แต่งหน้าจอให้ดูสวยงามบนมือถือ
st.markdown(
    """
    <style>
    .stButton>button {
        width: 100%;
        background-color: #4B0082;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🔮 เปิดไพ่ยิปซีทำนายดวง")
st.write("ตั้งจิตอธิษฐานนึกถึงเรื่องที่ต้องการถาม แล้วเลือกจำนวนไพ่ได้เลยครับ")

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

# ปุ่มเลือกจำนวนไพ่
num_cards = st.radio(
    "เลือกจำนวนไพ่ที่ต้องการจับ:",
    [1, 3, 4, 10],
    format_func=lambda x: f"สุ่มไพ่ {x} ใบ",
    horizontal=True,
)

if st.button("✨ ตั้งจิตอธิษฐาน แล้วเปิดไพ่"):
    drawn = random.sample(full_deck, num_cards)

    st.subheader(f"🎴 ผลการเปิดไพ่ของคุณ ({num_cards} ใบ)")
    st.write("---")

    for i, card in enumerate(drawn, 1):
        st.markdown(f"### ใบที่ {i}: **{card}**")
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/9/90/Rider-Waite-Tarot_00_Fool.jpg",
            caption=card,
            width=220,
        )
        st.write("---")
      
