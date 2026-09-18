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


# ฟังก์ชันเล่นเสียงผ่าน JavaScript ทะลวงการบล็อกบน Android
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
        text-align: center; font-size: 24px; font-weight: bold; color: #FFD700;
        text-shadow: 0 0 10px #FFD700, 0 0 20px #8A2BE2; margin-top: 15px; margin-bottom: 10px;
    }
    .sub-text { text-align: center; color: #E1BEE7; margin-bottom: 25px; font-size: 14px; }
    
    div.stButton > button {
        width: 100%; font-size: 18px; font-weight: bold; border-radius: 12px; padding: 12px;
        background: linear-gradient(135deg, #4A0E4E 0%, #1A0033 100%);
        color: #FFD700 !important; border: 1px solid #FFD700 !important;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.2);
    }
    
    .wheel-container { text-align: center; padding: 20px; }
    .magic-wheel { font-size: 70px; display: inline-block; animation: spin 0.8s linear infinite; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    .wheel-text { color: #FFD700; font-size: 16px; margin-top: 10px; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

# 📍 ฐานข้อมูลไพ่ราชาโชค (12 มหาโชค)
RAJA_CHOK_CARDS = {
    "ราชาโชคโภคทรัพย์": {
        "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400",
        "meaning": "การเงินหมุนเวียนดีเยี่ยม มีทรัพย์สินเงินทองไหลมาเทมา",
    },
    "ราชาโชคเสน่หา": {
        "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400",
        "meaning": "ผู้คนรักใคร่เอ็นดู มีเมตตามหานิยม ติดต่อสิ่งใดก็สำเร็จง่าย",
    },
    "ราชาโชคยศถา": {
        "image": "https://images.unsplash.com/photo-1534447677768-be436bb09401?w=400",
        "meaning": "ได้รับการเลื่อนขั้น ปรับตำแหน่ง มีเกียรติยศและบารมีสูงขึ้น",
    },
    "ราชาโชคปัญญา": {
        "image": "https://images.unsplash.com/photo-1507652313519-d4e9174996dd?w=400",
        "meaning": "รอบรู้ ฉลาดหลักแหลม แก้ไขปัญหาและหาทางออกได้อย่างอัศจรรย์",
    },
    "ราชาโชคชนะศึก": {
        "image": "https://images.unsplash.com/photo-1518709779341-56cf4535e94b?w=400",
        "meaning": "ชนะอุปสรรคและคู่แข่ง สิ่งเลวร้ายแพ้พ่าย หลุดพ้นจากปัญหา",
    },
    "ราชาโชคฟลุก": {
        "image": "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=400",
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
    '<div class="sub-text">🌌 ตั้งจิตอธิษฐาน สุ่มเปิดไพ่รับพลังมหาโชค 3 ใบ 🌌</div>',
    unsafe_allow_html=True,
)

st.write("---")

wheel_placeholder = st.empty()

if st.button("👑 เปิดไพ่ราชาโชค 3 ใบ", use_container_width=True):
    play_sound(SOUND_SHUFFLE)

    wheel_placeholder.markdown(
        """
        <div class="wheel-container">
            <div class="magic-wheel">☸️</div>
            <div class="wheel-text">👑 กงล้อราชาโชคมหาลาภกำลังหมุน... 👑</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    time.sleep(2.0)
    wheel_placeholder.empty()

    st.session_state.drawn_raja = random.sample(card_names, 3)
    play_sound(SOUND_REVEAL)

# แสดงผลเรียง 3 ใบขนานกันบนหน้าจอเดียว
if st.session_state.drawn_raja:
    st.markdown("### 🎴 ผลการเปิดไพ่ราชาโชคของคุณ")
    st.write("---")

    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]

    for i, name in enumerate(st.session_state.drawn_raja):
        info = RAJA_CHOK_CARDS[name]

        with cols[i]:
            st.markdown(
                f"""
                <div style="text-align: center; background: rgba(42, 8, 92, 0.6); padding: 10px; border-radius: 12px; border: 1px solid #FFD700; box-shadow: 0 4px 12px rgba(255,215,0,0.3);">
                    <div style="font-size: 13px; font-weight: bold; color: #FFD700; margin-bottom: 6px;">ใบที่ {i+1}</div>
                    <img src="{info['image']}" style="width: 100%; max-width: 130px; border-radius: 8px; border: 1px solid #FFD700;">
                    <div style="font-size: 12px; font-weight: bold; color: #F3E5F5; margin-top: 8px;">{name}</div>
                    <div style="font-size: 11px; color: #E1BEE7; margin-top: 4px; line-height: 1.3;">{info['meaning']}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

    st.write("---")
    
