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

    .wheel-container { text-align: center; padding: 15px; }
    .magic-wheel { font-size: 60px; display: inline-block; animation: spin 0.8s linear infinite; }
    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    .wheel-text { color: #FFD700; font-size: 14px; margin-top: 10px; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

# 📍 ฐานข้อมูลไพ่ออราเคิลมงคลสไตล์ไทย-จีน (ภาพออกแบบพิเศษ ลิขสิทธิ์ 100%)
RAJA_CHOK_CARDS = {
    "มังกรทองบารมี (Golden Dragon)": {
        "image": "https://images.unsplash.com/photo-1578632767115-351597cf2477?w=400&q=80",
        "meaning": "อำนาจ วาสนา สูงส่งด้วยยศถาบรรดาศักดิ์ ผู้ใหญ่เมตตาอุปถัมภ์",
    },
    "ปี่เซียะคาบทรัพย์ (Pixiu Fortune)": {
        "image": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400&q=80",
        "meaning": "โชคลาภการเงินหมุนเวียนดี กักเก็บทรัพย์สิน เงินทองไม่รั่วไหล",
    },
    "เทพเจ้าไฉ่ซิ้งเอี๊ย (God of Wealth)": {
        "image": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=400&q=80",
        "meaning": "ลาภลอยส้มหล่น ได้รับเงินก้อนโต การค้าขายเจริญรุ่งเรืองมั่งคั่ง",
    },
    "ดอกบัวปัญญามงคล (Sacred Lotus)": {
        "image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?w=400&q=80",
        "meaning": "จิตใจสงบร่มเย็น เกิดปัญญาญาณ หลุดพ้นอุปสรรคปัญหาทั้งปวง",
    },
    "พญานาคโชคโภคทรัพย์ (Naga Blessing)": {
        "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=400&q=80",
        "meaning": "สายญาณบารมีหนุนนำ โชคลาภจากสายน้ำและสิ่งศักดิ์สิทธิ์ให้พร",
    },
    "ดวงจันทร์กวักเสน่ห์ (Golden Moon)": {
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
            st.markdown(
                f"""
                <div style="text-align: center; background: rgba(42, 8, 92, 0.7); padding: 4px; border-radius: 8px; border: 1px solid #FFD700; margin-bottom: 5px;">
                    <div style="font-size: 11px; font-weight: bold; color: #FFD700;">ใบที่ {i+1}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            st.image(info["image"], use_container_width=True)

            st.markdown(
                f"""
                <div style="text-align: center; background: rgba(42, 8, 92, 0.7); padding: 4px; border-radius: 8px; border: 1px solid #FFD700; margin-top: 5px;">
                    <div style="font-size: 10px; font-weight: bold; color: #F3E5F5;">{name}</div>
                    <div style="font-size: 9px; color: #E1BEE7; margin-top: 3px; line-height: 1.2;">{info['meaning']}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

    st.write("---")
    
