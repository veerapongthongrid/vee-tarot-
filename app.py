import random
import time
import streamlit as st

st.set_page_config(
    page_title="เปิดไพ่ทำนายดวง โดยพี่หมอวีร์",
    page_icon="🔮",
    initial_sidebar_state="collapsed",
)

# ลิงก์ไฟล์เสียงมาตรฐาน
SOUND_SHUFFLE = "https://assets.mixkit.co/active_storage/sfx/2070/2070-preview.mp3"
SOUND_REVEAL = (
    "https://assets.mixkit.co/active_storage/sfx/2019/2019-preview.mp3"
)


# ฟังก์ชันสำหรับเล่นเสียงอัตโนมัติ
def play_sound(sound_url):
    sound_html = f'<audio autoplay style="display:none;"><source src="{sound_url}" type="audio/mp3"></audio>'
    st.markdown(sound_html, unsafe_allow_html=True)


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

    .card-box {
        background: rgba(44, 12, 62, 0.6);
        border: 1px solid #8A2BE2;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(138, 43, 226, 0.25);
    }

    .card-title {
        font-size: 18px;
        font-weight: bold;
        color: #F3E5F5;
        margin-bottom: 4px;
    }

    .card-sub {
        font-size: 15px;
        color: #BA68C8;
        margin-bottom: 12px;
    }

    h3 {
        color: #E1BEE7 !important;
        text-align: center;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# ฐานข้อมูลรูปภาพไพ่ยิปซีมาตรฐาน ครบ 78 ใบ
BASE_URL = "https://sacred-texts.com/tarot/pkt/img/"

TAROT_IMAGES = {
    # Major Arcana (22 ใบ)
    "0. The Fool": BASE_URL + "ar00.jpg",
    "1. The Magician": BASE_URL + "ar01.jpg",
    "2. The High Priestess": BASE_URL + "ar02.jpg",
    "3. The Empress": BASE_URL + "ar03.jpg",
    "4. The Emperor": BASE_URL + "ar04.jpg",
    "5. The Hierophant": BASE_URL + "ar05.jpg",
    "6. The Lovers": BASE_URL + "ar06.jpg",
    "7. The Chariot": BASE_URL + "ar07.jpg",
    "8. Strength": BASE_URL + "ar08.jpg",
    "9. The Hermit": BASE_URL + "ar09.jpg",
    "10. Wheel of Fortune": BASE_URL + "ar10.jpg",
    "11. Justice": BASE_URL + "ar11.jpg",
    "12. The Hanged Man": BASE_URL + "ar12.jpg",
    "13. Death": BASE_URL + "ar13.jpg",
    "14. Temperance": BASE_URL + "ar14.jpg",
    "15. The Devil": BASE_URL + "ar15.jpg",
    "16. The Tower": BASE_URL + "ar16.jpg",
    "17. The Star": BASE_URL + "ar17.jpg",
    "18. The Moon": BASE_URL + "ar18.jpg",
    "19. The Sun": BASE_URL + "ar19.jpg",
    "20. Judgement": BASE_URL + "ar20.jpg",
    "21. The World": BASE_URL + "ar21.jpg",
    # Wands - ไม้เท้า (14 ใบ)
    "Ace of Wands": BASE_URL + "waac.jpg",
    "Two of Wands": BASE_URL + "wa02.jpg",
    "Three of Wands": BASE_URL + "wa03.jpg",
    "Four of Wands": BASE_URL + "wa04.jpg",
    "Five of Wands": BASE_URL + "wa05.jpg",
    "Six of Wands": BASE_URL + "wa06.jpg",
    "Seven of Wands": BASE_URL + "wa07.jpg",
    "Eight of Wands": BASE_URL + "wa08.jpg",
    "Nine of Wands": BASE_URL + "wa09.jpg",
    "Ten of Wands": BASE_URL + "wa10.jpg",
    "Page of Wands": BASE_URL + "wapa.jpg",
    "Knight of Wands": BASE_URL + "wakn.jpg",
    "Queen of Wands": BASE_URL + "waqu.jpg",
    "King of Wands": BASE_URL + "waki.jpg",
    # Cups - ถ้วย (14 ใบ)
    "Ace of Cups": BASE_URL + "cuac.jpg",
    "Two of Cups": BASE_URL + "cu02.jpg",
    "Three of Cups": BASE_URL + "cu03.jpg",
    "Four of Cups": BASE_URL + "cu04.jpg",
    "Five of Cups": BASE_URL + "cu05.jpg",
    "Six of Cups": BASE_URL + "cu06.jpg",
    "Seven of Cups": BASE_URL + "cu07.jpg",
    "Eight of Cups": BASE_URL + "cu08.jpg",
    "Nine of Cups": BASE_URL + "cu09.jpg",
    "Ten of Cups": BASE_URL + "cu10.jpg",
    "Page of Cups": BASE_URL + "cupa.jpg",
    "Knight of Cups": BASE_URL + "cukn.jpg",
    "Queen of Cups": BASE_URL + "cuqu.jpg",
    "King of Cups": BASE_URL + "cuki.jpg",
    # Swords - ดาบ (14 ใบ)
    "Ace of Swords": BASE_URL + "swac.jpg",
    "Two of Swords": BASE_URL + "sw02.jpg",
    "Three of Swords": BASE_URL + "sw03.jpg",
    "Four of Swords": BASE_URL + "sw04.jpg",
    "Five of Swords": BASE_URL + "sw05.jpg",
    "Six of Swords": BASE_URL + "sw06.jpg",
    "Seven of Swords": BASE_URL + "sw07.jpg",
    "Eight of Swords": BASE_URL + "sw08.jpg",
    "Nine of Swords": BASE_URL + "sw09.jpg",
    "Ten of Swords": BASE_URL + "sw10.jpg",
    "Page of Swords": BASE_URL + "swpa.jpg",
    "Knight of Swords": BASE_URL + "swkn.jpg",
    "Queen of Swords": BASE_URL + "swqu.jpg",
    "King of Swords": BASE_URL + "swki.jpg",
    # Pentacles - เหรียญ (14 ใบ)
    "Ace of Pentacles": BASE_URL + "peac.jpg",
    "Two of Pentacles": BASE_URL + "pe02.jpg",
    "Three of Pentacles": BASE_URL + "pe03.jpg",
    "Four of Pentacles": BASE_URL + "pe04.jpg",
    "Five of Pentacles": BASE_URL + "pe05.jpg",
    "Six of Pentacles": BASE_URL + "pe06.jpg",
    "Seven of Pentacles": BASE_URL + "pe07.jpg",
    "Eight of Pentacles": BASE_URL + "pe08.jpg",
    "Nine of Pentacles": BASE_URL + "pe09.jpg",
    "Ten of Pentacles": BASE_URL + "pe10.jpg",
    "Page of Pentacles": BASE_URL + "pepa.jpg",
    "Knight of Pentacles": BASE_URL + "pekn.jpg",
    "Queen of Pentacles": BASE_URL + "pequ.jpg",
    "King of Pentacles": BASE_URL + "peki.jpg",
}

full_deck = list(TAROT_IMAGES.keys())

# สร้าง Session State เก็บสถานะการสุ่มไพ่
if "drawn_3" not in st.session_state:
    st.session_state.drawn_3 = None
if "drawn_2" not in st.session_state:
    st.session_state.drawn_2 = None
if "play_reveal_sound" not in st.session_state:
    st.session_state.play_reveal_sound = False

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
    play_sound(SOUND_SHUFFLE)
    with st.spinner("✨ กำลังสับไพ่และตั้งจิตอธิษฐานสื่อสารกับดวงดาว..."):
        time.sleep(1.8)
        st.session_state.drawn_3 = random.sample(full_deck, 3)
        st.session_state.drawn_2 = None
        st.session_state.play_reveal_sound = True

# แสดงผลไพ่ 3 ใบ
if st.session_state.drawn_3:
    if st.session_state.play_reveal_sound:
        play_sound(SOUND_REVEAL)
        st.session_state.play_reveal_sound = False

    st.markdown("### 🎴 ผลการเปิดไพ่ของคุณ (3 ใบ)")
    st.write("---")

    for i, card in enumerate(st.session_state.drawn_3):
        img_url = TAROT_IMAGES.get(card)
        st.markdown(
            f'<div class="card-box"><div class="card-title">ใบที่ {i+1}</div><div class="card-sub">{card}</div><img src="{img_url}" style="width:140px; border-radius:10px; border:1px solid #BA68C8; box-shadow:0 0 15px rgba(138,43,226,0.6);"></div>',
            unsafe_allow_html=True,
        )

    # ปุ่มเปิดไพ่เพิ่ม 2 ใบ
    st.write("---")
    if st.button("✨ เปิดไพ่ทำนายเพิ่ม 2 ใบ", use_container_width=True):
        play_sound(SOUND_SHUFFLE)
        with st.spinner("🌟 กำลังเปิดไพ่ทำนายเพิ่มเติม..."):
            time.sleep(1.5)
            remaining_deck = [
                c for c in full_deck if c not in st.session_state.drawn_3
            ]
            st.session_state.drawn_2 = random.sample(remaining_deck, 2)
            st.session_state.play_reveal_sound = True

# แสดงผลไพ่เพิ่ม 2 ใบที่ด้านล่างสุด
if st.session_state.drawn_2:
    if st.session_state.play_reveal_sound:
        play_sound(SOUND_REVEAL)
        st.session_state.play_reveal_sound = False

    st.markdown("### ✨ ผลการเปิดไพ่ทำนายเพิ่ม (2 ใบ)")
    st.write("---")

    for i, card in enumerate(st.session_state.drawn_2):
        img_url = TAROT_IMAGES.get(card)
        st.markdown(
            f'<div class="card-box"><div class="card-title">ใบเพิ่ม {i+1}</div><div class="card-sub">{card}</div><img src="{img_url}" style="width:140px; border-radius:10px; border:1px solid #BA68C8; box-shadow:0 0 15px rgba(138,43,226,0.6);"></div>',
            unsafe_allow_html=True,
        )
        
