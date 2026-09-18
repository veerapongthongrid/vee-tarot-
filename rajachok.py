import random
import time
import streamlit as st

st.set_page_config(
    page_title="เปิดไพ่ออราเคิลราชาโชค โดยพี่หมอวีร์",
    page_icon="👑",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <head>
        <meta property="og:title" content="เปิดไพ่ออราเคิลราชาโชค โดยพี่หมอวีร์ 👑✨">
        <meta property="og:description" content="สุ่มเปิดไพ่ออราเคิลมงคล รับพลังมหาโชค มหาลาภ และบารมี">
    </head>
""",
    unsafe_allow_html=True,
)

SOUND_SHUFFLE = "https://assets.mixkit.co/active_storage/sfx/2070/2070-preview.mp3"
SOUND_REVEAL = (
    "https://assets.mixkit.co/active_storage/sfx/2019/2019-preview.mp3"
)


def play_sound(sound_url):
    sound_html = f"""
        <script>
            var audio = new Audio('{sound_url}');
            audio.play().catch(function(error) {{
                console.log("Autoplay blocked:", error);
            }});
        </script>
    """
    st.markdown(sound_html, unsafe_allow_html=True)


st.markdown(
    """
    <style>
    .stApp {
        background-color: #0F0A1C;
        background-image: 
            radial-gradient(gold, rgba(255,215,0,.15) 1px, transparent 30px),
            radial-gradient(ellipse at bottom, #2A085C 0%, #0F0A1C 100%);
        background-size: 400px 400px, 100% 100%;
        color: #F3E5F5;
    }
    .main-title {
        text-align: center; font-size: 22px; font-weight: bold; color: #FFD700;
        text-shadow: 0 0 10px #FFD700, 0 0 20px #8A2BE2; margin-top: 10px; margin-bottom: 5px;
    }
    .sub-text { text-align: center; color: #E1BEE7; margin-bottom: 15px; font-size: 13px; }
    
    div.stButton > button {
        width: 100%; font-size: 15px; font-weight: bold; border-radius: 10px; padding: 10px;
        background: linear-gradient(135deg, #4A0E4E 0%, #1A0033 100%);
        color: #FFD700 !important; border: 1px solid #FFD700 !important;
        box-shadow: 0 4px 12px rgba(255, 215, 0, 0.2);
        margin-bottom: 5px;
    }
    
    [data-testid="column"] {
        flex: 1 1 0% !important;
        min-width: 0 !important;
        padding: 0 2px !important;
    }

    .card-top {
        background: #1F0833;
        border: 2px solid #FFD700;
        border-bottom: none;
        border-radius: 10px 10px 0 0;
        padding: 4px;
        text-align: center;
        font-size: 11px;
        font-weight: bold;
        color: #FFD700;
    }
    
    .card-bottom {
        background: #1F0833;
        border: 2px solid #FFD700;
        border-top: none;
        border-radius: 0 0 10px 10px;
        padding: 6px 4px;
        text-align: center;
        margin-bottom: 10px;
    }
    
    .card-title {
        font-size: 10px;
        font-weight: bold;
        color: #FFFFFF;
    }
    
    .card-meaning {
        font-size: 8px;
        color: #E1BEE7;
        margin-top: 2px;
        line-height: 1.1;
    }

    .wheel-container { text-align: center; padding: 15px; }
    .magic-wheel { font-size: 60px; display: inline-block; animation: spin 0.8s linear infinite; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    .wheel-text { color: #FFD700; font-size: 14px; margin-top: 10px; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

# 📍 ฐานข้อมูลรูปภาพที่ใช้ CDN เสถียรสูง ดึงภาพขึ้นแน่นอน 100%
RAJA_CHOK_CARDS = {
    "มังกรทองบารมี": {
        "image": "https://picsum.photos/id/1059/300/450",
        "meaning": "อำนาจ วาสนา สูงส่งด้วยยศถาบรรดาศักดิ์ ผู้ใหญ่เมตตาอุปถัมภ์",
    },
    "ปี่เซียะคาบทรัพย์": {
        "image": "https://picsum.photos/id/1062/300/450",
        "meaning": "โชคลาภการเงินหมุนเวียนดี กักเก็บทรัพย์สิน เงินทองไม่รั่วไหล",
    },
    "เทพไฉ่ซิ้งเอี๊ย": {
        "image": "https://picsum.photos/id/1069/300/450",
        "meaning": "ลาภลอยส้มหล่น ได้รับเงินก้อนโต การค้าขายเจริญรุ่งเรืองมั่งคั่ง",
    },
    "ดอกบัวปัญญามงคล": {
        "image": "https://picsum.photos/id/1074/300/450",
        "meaning": "จิตใจสงบร่มเย็น เกิดปัญญาญาณ หลุดพ้นอุปสรรคปัญหาทั้งปวง",
    },
    "พญานาคโภคทรัพย์": {
        "image": "https://picsum.photos/id/1084/300/450",
        "meaning": "สายญาณบารมีหนุนนำ โชคลาภจากสายน้ำและสิ่งศักดิ์สิทธิ์ให้พร",
    },
    "ดวงจันทร์กวักเสน่ห์": {
        "image": "https://images.unsplash.com/photo-1532693322450-2cb5c511067d?w=400&q=80",
        "meaning": "เมตตามหานิยม คนรักใคร่เอ็นดู ติดต่อเจรจาสิ่งใดก็สำเร็จสมปรารถนา",
    },
}

card_names = list(RAJA_CHOK_CARDS.keys())

if "drawn_raja" not in st.session_state:
    st.session_state.drawn_raja = None

st.markdown(
    '<div class="main-title">👑 ✨ เปิดไพ่ออราเคิลราชาโชค โดยพี่หมอวีร์ ✨ 👑</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-text">🌌 ตั้งจิตอธิษฐาน เลือกเปิดไพ่ออราเคิลรับพลังมหาโชค 🌌</div>',
    unsafe_allow_html=True,
)

st.write("---")

wheel_placeholder = st.empty()

col_b1, col_b2, col_b3 = st.columns(3)

num_to_draw = 0
with col_b1:
    if st.button("🔮 เปิด 1 ใบ", use_container_width=True):
        num_to_draw = 1
with col_b2:
    if st.button("✨ เปิด 2 ใบ", use_container_width=True):
        num_to_draw = 2
with col_b3:
    if st.button("👑 เปิด 3 ใบ", use_container_width=True):
        num_to_draw = 3

if num_to_draw > 0:
    play_sound(SOUND_SHUFFLE)

    wheel_placeholder.markdown(
        """
        <div class="wheel-container">
            <div class="magic-wheel">☸️</div>
            <div class="wheel-text">👑 กำลังสุ่มเปิดไพ่ออราเคิลมงคล... 👑</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    time.sleep(1.8)
    wheel_placeholder.empty()

    st.session_state.drawn_raja = random.sample(card_names, num_to_draw)
    play_sound(SOUND_REVEAL)

if st.session_state.drawn_raja:
    st.markdown("##### 🎴 ผลการเปิดไพ่ออราเคิลของคุณ")

    card_count = len(st.session_state.drawn_raja)
    cols = st.columns(card_count)

    for i, name in enumerate(st.session_state.drawn_raja):
        info = RAJA_CHOK_CARDS[name]

        with cols[i]:
            # ส่วนหัวการ์ด
            st.markdown(
                f'<div class="card-top">ใบที่ {i+1}</div>',
                unsafe_allow_html=True,
            )

            # แสดงผลรูปภาพผ่าน st.image ของ Streamlit โดยตรง
            st.image(info["image"], use_container_width=True)

            # ส่วนท้ายการ์ดพร้อมคำทำนาย
            st.markdown(
                f"""
                <div class="card-bottom">
                    <div class="card-title">{name}</div>
                    <div class="card-meaning">{info['meaning']}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

    st.write("---")
    
