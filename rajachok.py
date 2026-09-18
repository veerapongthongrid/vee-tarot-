import random
import time
import streamlit as st

st.set_page_config(
    page_title="ไพ่ออราเคิลสาส์นศักดิ์สิทธิ์ โดยพี่หมอวีร์",
    page_icon="🔮",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <head>
        <meta property="og:title" content="ไพ่ออราเคิลสาส์นศักดิ์สิทธิ์ โดยพี่หมอวีร์ 🔮✨">
        <meta property="og:description" content="สุ่มเปิดไพ่ออราเคิลรับสาส์นจากสิ่งศักดิ์สิทธิ์ เสริมพลังคำทำนายไพ่ทาโรต์">
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
        line-height: 1.2;
    }

    .wheel-container { text-align: center; padding: 15px; }
    .magic-wheel { font-size: 60px; display: inline-block; animation: spin 0.8s linear infinite; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    .wheel-text { color: #FFD700; font-size: 14px; margin-top: 10px; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

# 📍 ฐานข้อมูล 12 สาส์นศักดิ์สิทธิ์ (สุ่มเปิดเสริมคู่กับไพ่ทาโรต์)
DIVINE_ORACLE_CARDS = {
    "1. สาส์นแห่งการรอคอย": {
        "image": "https://picsum.photos/id/1059/300/450",
        "meaning": "ทุกอย่างมีเวลาของมัน ช้าหน่อยแต่ชัวร์ อย่าเพิ่งใจร้อน สิ่งดีๆ กำลังจัดสรร",
    },
    "2. สาส์นแห่งการปล่อยวาง": {
        "image": "https://picsum.photos/id/1062/300/450",
        "meaning": "ปล่อยความกังวลออกไป ถอยออกมาหนึ่งก้าว ยิ่งยึดติดยิ่งเหนื่อย ให้จักรวาลดูแล",
    },
    "3. สาส์นแห่งการปกป้อง": {
        "image": "https://picsum.photos/id/1069/300/450",
        "meaning": "สิ่งศักดิ์สิทธิ์กำลังคุ้มครองคุณ ปลอดภัยจากภยันตรายและคนคิดร้าย แน่นอน",
    },
    "4. สาส์นแห่งปัญญาญาณ": {
        "image": "https://picsum.photos/id/1074/300/450",
        "meaning": "เชื่อในสัญชาตญาณและเสียงข้างในจิตใจ คำตอบที่คุณตามหาอยู่ในตัวคุณเอง",
    },
    "5. สาส์นแห่งโชคอุปถัมภ์": {
        "image": "https://picsum.photos/id/1084/300/450",
        "meaning": "เทวดาพร้อมอวยพร เปิดรับโชคลาภและการช่วยเหลือจากผู้ใหญ่/สิ่งศักดิ์สิทธิ์",
    },
    "6. สาส์นแห่งการเยียวยา": {
        "image": "https://picsum.photos/id/1067/300/450",
        "meaning": "พักผ่อนใจและกาย บาดแผลในอดีตกำลังได้รับการฟื้นฟู ชาร์จพลังแล้วเริ่มใหม่",
    },
    "7. สาส์นแห่งทางสว่าง": {
        "image": "https://picsum.photos/id/1058/300/450",
        "meaning": "อุปสรรคหมอกควันกำลังจะหายไป ทางออกที่ชัดเจนกำลังเปิดให้คุณเดินต่อ",
    },
    "8. สาส์นแห่งผลบุญ": {
        "image": "https://picsum.photos/id/1039/300/450",
        "meaning": "ความดีและบุญกุศลที่เคยทำไว้นานแล้ว กำลังส่งผลเป็นโชคลาภและความสำเร็จ",
    },
    "9. สาส์นแห่งความกล้าหาญ": {
        "image": "https://picsum.photos/id/1043/300/450",
        "meaning": "อย่ากล้ว จงก้าวข้ามความขี้กลัว คุณมีความแข็งแกร่งและพลังชนะทุกอุปสรรค",
    },
    "10. สาส์นแห่งความสมดุล": {
        "image": "https://picsum.photos/id/1048/300/450",
        "meaning": "ปรับสมดุลชีวิต งาน ความรัก และการพักผ่อน ตึงไปก็ขาด หย่อนไปก็ไม่โต",
    },
    "11. สาส์นแห่งโอกาสใหม่": {
        "image": "https://picsum.photos/id/1050/300/450",
        "meaning": "ประตูบานเก่าปิด ประตูบานใหม่ใหญ่กว่ากำลังเปิด เตรียมพร้อมรับสิ่งใหม่",
    },
    "12. สาส์นแห่งความสงบสุข": {
        "image": "https://picsum.photos/id/1053/300/450",
        "meaning": "ความอุ่นใจ ชัยชนะที่นุ่มนวล ชีวิตกำลังเข้าสู่ช่วงแห่งความสงบและเปี่ยมสุข",
    },
}

card_names = list(DIVINE_ORACLE_CARDS.keys())

if "drawn_divine" not in st.session_state:
    st.session_state.drawn_divine = None

st.markdown(
    '<div class="main-title">🔮 ✨ สาส์นศักดิ์สิทธิ์ โดยพี่หมอวีร์ ✨ 🔮</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-text">🌌 สิ่งศักดิ์สิทธิ์อยากบอกอะไรกับคุณในวันนี้? 🌌</div>',
    unsafe_allow_html=True,
)

st.write("---")

wheel_placeholder = st.empty()

col_b1, col_b2, col_b3 = st.columns(3)

num_to_draw = 0
with col_b1:
    if st.button("🔮 รับ 1 สาส์น", use_container_width=True):
        num_to_draw = 1
with col_b2:
    if st.button("✨ รับ 2 สาส์น", use_container_width=True):
        num_to_draw = 2
with col_b3:
    if st.button("👑 รับ 3 สาส์น", use_container_width=True):
        num_to_draw = 3

if num_to_draw > 0:
    play_sound(SOUND_SHUFFLE)

    wheel_placeholder.markdown(
        """
        <div class="wheel-container">
            <div class="magic-wheel">☸️</div>
            <div class="wheel-text">🔮 กำลังเชื่อมต่อสาส์นศักดิ์สิทธิ์... 🔮</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    time.sleep(1.8)
    wheel_placeholder.empty()

    st.session_state.drawn_divine = random.sample(card_names, num_to_draw)
    play_sound(SOUND_REVEAL)

if st.session_state.drawn_divine:
    st.markdown("##### 🎴 สาส์นที่สิ่งศักดิ์สิทธิ์ประทานให้คุณ")

    card_count = len(st.session_state.drawn_divine)
    cols = st.columns(card_count)

    for i, name in enumerate(st.session_state.drawn_divine):
        info = DIVINE_ORACLE_CARDS[name]

        with cols[i]:
            st.markdown(
                f'<div class="card-top">ใบที่ {i+1}</div>',
                unsafe_allow_html=True,
            )

            st.image(info["image"], use_container_width=True)

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

    
