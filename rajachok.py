import random
import time
import streamlit as st

st.set_page_config(
    page_title="เปิดไพ่ราชาโชค โดยพี่หมอวีร์",
    page_icon="👑",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <head>
        <meta property="og:title" content="เปิดไพ่ราชาโชค โดยพี่หมอวีร์ 👑✨">
        <meta property="og:description" content="สุ่มเปิดไพ่ราชาโชค รับพลังมหาลาภ วาสนา และบารมี">
        <meta property="og:image" content="https://images.unsplash.com/photo-1518709268805-4e9042af9f23">
    </head>
""",
    unsafe_allow_html=True,
)

SOUND_SHUFFLE = "https://assets.mixkit.co/active_storage/sfx/2070/2070-preview.mp3"
SOUND_REVEAL = (
    "https://assets.mixkit.co/active_storage/sfx/2019/2019-preview.mp3"
)


# ฟังก์ชันเล่นเสียงที่รองรับ Android Chrome
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

    .wheel-container { text-align: center; padding: 15px; }
    .magic-wheel { font-size: 60px; display: inline-block; animation: spin 0.8s linear infinite; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    .wheel-text { color: #FFD700; font-size: 14px; margin-top: 10px; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

# 📍 ฐานข้อมูลไพ่ราชาโชค
RAJA_CHOK_CARDS = {
    "ราชาโชคโภคทรัพย์": {
        "image": "https://picsum.photos/id/1059/300/480",
        "meaning": "การเงินหมุนเวียนดี มีทรัพย์สินเงินทองไหลมาเทมา",
    },
    "ราชาโชคเสน่หา": {
        "image": "https://picsum.photos/id/1062/300/480",
        "meaning": "ผู้คนรักใคร่เอ็นดู มีเมตตามหานิยม ติดต่อสิ่งใดก็สำเร็จ",
    },
    "ราชาโชคยศถา": {
        "image": "https://picsum.photos/id/1069/300/480",
        "meaning": "ได้รับการเลื่อนขั้น ปรับตำแหน่ง มีเกียรติยศและบารมีสูงขึ้น",
    },
    "ราชาโชคปัญญา": {
        "image": "https://picsum.photos/id/1074/300/480",
        "meaning": "รอบรู้ ฉลาดหลักแหลม แก้ไขปัญหาหาทางออกได้อย่างอัศจรรย์",
    },
    "ราชาโชคชนะศึก": {
        "image": "https://picsum.photos/id/1084/300/480",
        "meaning": "ชนะอุปสรรคและคู่แข่ง สิ่งเลวร้ายแพ้พ่าย หลุดพ้นจากปัญหา",
    },
    "ราชาโชคฟลุก": {
        "image": "https://picsum.photos/id/1080/300/480",
        "meaning": "ได้โชคลาภแบบไม่คาดฝัน ส้มหล่น ได้รับของขวัญหรือเงินก้อนโต",
    },
}

card_names = list(RAJA_CHOK_CARDS.keys())

if "drawn_raja" not in st.session_state:
    st.session_state.drawn_raja = None

st.markdown(
    '<div class="main-title">👑 ✨ เปิดไพ่ราชาโชค โดยพี่หมอวีร์ ✨ 👑</div>',
    unsafe_allow_html=True,
)
st.markdown(
    '<div class="sub-text">🌌 ตั้งจิตอธิษฐาน เลือกเปิดไพ่รับพลังมหาโชค 🌌</div>',
    unsafe_allow_html=True,
)

st.write("---")

wheel_placeholder = st.empty()

# 📍 ปุ่มกดเปิดไพ่ 3 ตัวเลือก (1 ใบ, 2 ใบ, 3 ใบ)
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
            <div class="wheel-text">👑 กำลังสุ่มเปิดไพ่ราชาโชค... 👑</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    time.sleep(1.8)
    wheel_placeholder.empty()

    st.session_state.drawn_raja = random.sample(card_names, num_to_draw)
    play_sound(SOUND_REVEAL)

# แสดงผลเรียงขนานกันบนหน้าจอมือถือตามจำนวนไพ่ที่สุ่มได้
if st.session_state.drawn_raja:
    st.markdown("##### 🎴 ผลการเปิดไพ่ราชาโชค")

    card_count = len(st.session_state.drawn_raja)
    cols = st.columns(card_count)

    for i, name in enumerate(st.session_state.drawn_raja):
        info = RAJA_CHOK_CARDS[name]

        with cols[i]:
            st.markdown(
                f"""
                <div style="text-align: center; background: rgba(42, 8, 92, 0.7); padding: 6px; border-radius: 8px; border: 1px solid #FFD700;">
                    <div style="font-size: 11px; font-weight: bold; color: #FFD700; margin-bottom: 3px;">ใบที่ {i+1}</div>
                    <img src="{info['image']}" style="width: 100%; border-radius: 6px; border: 1px solid #FFD700;">
                    <div style="font-size: 11px; font-weight: bold; color: #F3E5F5; margin-top: 5px;">{name}</div>
                    <div style="font-size: 9px; color: #E1BEE7; margin-top: 3px; line-height: 1.2;">{info['meaning']}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

    st.write("---")
    
