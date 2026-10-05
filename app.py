import base64
import random
import time
import requests
import streamlit as st

# 1. ตั้งค่าหน้าเพจ Streamlit
st.set_page_config(
    page_title="ระบบดูดวงพี่หมอวี - ไพ่ยิปซี & เซียมซีห้องสิน",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded",
)


# ฟังก์ชันดึงรูปไพ่ยิปซีจริงและแปลงเป็น Base64
@st.cache_data(show_spinner=False)
def load_card_image_base64(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            encoded = base64.b64encode(response.content).decode("utf-8")
            return f"data:image/jpeg;base64,{encoded}"
    except Exception:
        pass
    return url


# ฟังก์ชันสร้างการ์ดรูปภาพเซียมซีเทพเซียนห้องสิน มงคลจีนเฉพาะใบ
def generate_siamsi_card_svg(title_th, number, symbol="☯️", bg_color1="#7e22ce", bg_color2="#3b0764"):
    svg_code = f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 380" width="100%" height="100%">
        <defs>
            <linearGradient id="siamsiBg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="{bg_color1}" />
                <stop offset="100%" stop-color="{bg_color2}" />
            </linearGradient>
            <linearGradient id="goldFrame" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#fef08a" />
                <stop offset="50%" stop-color="#eab308" />
                <stop offset="100%" stop-color="#ca8a04" />
            </linearGradient>
        </defs>
        <rect x="5" y="5" width="230" height="370" rx="12" fill="url(#siamsiBg)" stroke="url(#goldFrame)" stroke-width="4"/>
        <rect x="12" y="12" width="216" height="356" rx="8" fill="none" stroke="url(#goldFrame)" stroke-width="1.5" stroke-dasharray="4,3"/>
        
        <text x="120" y="42" font-family="'Sarabun', sans-serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#fef08a">เซียมซีห้องสิน ใบที่ {number}</text>
        
        <circle cx="120" cy="160" r="55" fill="rgba(255,255,255,0.08)" stroke="url(#goldFrame)" stroke-width="2"/>
        <circle cx="120" cy="160" r="46" fill="none" stroke="#fef08a" stroke-width="1" stroke-dasharray="3,2"/>
        <text x="120" y="178" font-family="'Sarabun', sans-serif" font-size="50" text-anchor="middle" fill="#fef08a">{symbol}</text>
        
        <rect x="20" y="250" width="200" height="90" rx="8" fill="rgba(15, 23, 42, 0.85)" stroke="url(#goldFrame)" stroke-width="1"/>
        <text x="120" y="280" font-family="'Sarabun', sans-serif" font-size="13" font-weight="bold" text-anchor="middle" fill="#ffffff">สาส์นสวรรค์มงคล</text>
        <text x="120" y="305" font-family="'Sarabun', sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#fef08a">{title_th[:22]}</text>
        <text x="120" y="325" font-family="'Sarabun', sans-serif" font-size="10" text-anchor="middle" fill="#cbd5e1">☯️ ตำนานเทพเซียนห้องสิน 49 ใบ</text>
    </svg>
    """
    b64 = base64.b64encode(svg_code.encode('utf-8')).decode('utf-8')
    return f"data:image/svg+xml;base64,{b64}"


# 2. ฐานข้อมูลไพ่ยิปซีคลาสสิก Rider-Waite จริง
TAROT_CARDS_RAW = {
    1: {
        "name": "The Fool (ผู้เริ่มต้น)",
        "meaning": "การเริ่มต้นใหม่ ความเป็นอิสระ มีโชคจากการกล้าเสี่ยง ให้ทำตามหัวใจ",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg",
    },
    2: {
        "name": "The Magician (นักมายากล)",
        "meaning": "ความสามารถรอบด้าน การติดต่อสื่อสารสำเร็จ เงินทองมาจากความสามารถ",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg",
    },
    3: {
        "name": "The High Priestess (นักบวชหญิง)",
        "meaning": "สัญชาตญาณแม่นยำ เสน่ห์ดึงดูด มีโชคด้านลางสังหรณ์ ให้เชื่อมั่นความคิดแรก",
        "url": "https://upload.wikimedia.org/wikipedia/commons/8/88/RWS_Tarot_02_High_Priestess.jpg",
    },
    4: {
        "name": "The Empress (จักรพรรดินี)",
        "meaning": "ความอุดมสมบูรณ์ ความรักอบอุ่น มั่งคั่ง มีเกณฑ์ได้รับข่าวดีเรื่องเงินทอง",
        "url": "https://upload.wikimedia.org/wikipedia/commons/d/d2/RWS_Tarot_03_Empress.jpg",
    },
    5: {
        "name": "The Emperor (จักรพรรดิ)",
        "meaning": "อำนาจบารมี ความมั่นคง การได้รับการสนับสนุนจากผู้ใหญ่ งานใหญ่สำเร็จ",
        "url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg",
    },
    6: {
        "name": "The Lovers (คนรัก)",
        "meaning": "ความรักสมหวัง การตัดสินใจครั้งสำคัญ พันธมิตรที่ดี ความสัมพันธ์ก้าวหน้า",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3a/TheLovers.jpg",
    },
    7: {
        "name": "The Sun (ดวงอาทิตย์)",
        "meaning": "ความสำเร็จสูงสุด ข่าวดี ชื่อเสียง ความสุขความสดใส ได้รับโชคลาภใหญ่",
        "url": "https://upload.wikimedia.org/wikipedia/commons/9/91/RWS_Tarot_19_Sun.jpg",
    },
    8: {
        "name": "Wheel of Fortune (กงล้อโชคชะตา)",
        "meaning": "โชคชะตาเปลี่ยนไปในทางที่ดี ได้รับโอกาสทอง โชคลาภฟลุ๊กๆ ไหลมา",
        "url": "https://upload.wikimedia.org/wikipedia/commons/3/3c/RWS_Tarot_10_Wheel_of_Fortune.jpg",
    },
}

# 3. CSS สไตล์เทพมงคลจีน
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fefce8 0%, #fae8ff 40%, #fce7f3 70%, #ffffff 100%);
        color: #3b0764;
        font-family: 'Sarabun', sans-serif;
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #faf5ff 0%, #f3e8ff 100%);
        border-right: 2px solid #fde047;
    }

    div[data-testid="stRadio"] > label {
        font-size: 1.1rem !important;
        font-weight: bold !important;
        color: #7e22ce !important;
        margin-bottom: 8px !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 2px solid #e9d5ff !important;
        border-radius: 12px !important;
        padding: 14px 16px !important;
        margin-bottom: 12px !important;
        box-shadow: 0px 3px 10px rgba(168, 85, 247, 0.1) !important;
        cursor: pointer !important;
        transition: all 0.2s ease-in-out !important;
        display: flex !important;
        align-items: center !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] > label p {
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        color: #3b0764 !important;
    }

    div[data-testid="stRadio"] div[role="radiogroup"] > label:has(input:checked) {
        border-color: #a855f7 !important;
        background: linear-gradient(135deg, #ffffff 0%, #f3e8ff 100%) !important;
        box-shadow: 0px 4px 12px rgba(168, 85, 247, 0.25) !important;
    }

    .main-title {
        text-align: center;
        color: #7e22ce;
        font-size: 1.8rem;
        font-weight: bold;
        text-shadow: 0px 2px 10px rgba(234, 179, 8, 0.4);
        margin-bottom: 2px;
    }
    
    .sub-title {
        text-align: center;
        color: #a855f7;
        font-size: 0.95rem;
        margin-bottom: 15px;
    }

    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 6px !important;
    }

    div[data-testid="column"] {
        flex: 1 1 33.33% !important;
        min-width: 0 !important;
    }

    div[data-testid="stImage"] {
        text-align: center;
    }

    div[data-testid="stImage"] > img {
        max-height: 135px !important;
        width: auto !important;
        margin: 0 auto !important;
        border-radius: 6px !important;
        box-shadow: 0px 3px 8px rgba(0,0,0,0.25) !important;
        border: 1px solid #facc15 !important;
    }

    .result-box-small {
        background-color: rgba(255, 255, 255, 0.95);
        border: 1px solid #facc15;
        border-radius: 6px;
        padding: 5px;
        box-shadow: 0px 2px 6px rgba(168, 85, 247, 0.1);
        margin-top: 4px;
        font-size: 0.7rem;
        line-height: 1.2;
        text-align: center;
        word-break: break-word;
    }

    .result-box {
        background-color: rgba(255, 255, 255, 0.95);
        border: 2px solid #facc15;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0px 6px 18px rgba(168, 85, 247, 0.15);
        margin-bottom: 15px;
    }

    .pred-header {
        color: #7e22ce;
        font-weight: bold;
        margin-top: 8px;
        margin-bottom: 3px;
        font-size: 0.95rem;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #a855f7 0%, #d946ef 100%);
        color: white;
        font-size: 1.05rem;
        font-weight: bold;
        border-radius: 20px;
        border: 2px solid #fef08a;
        box-shadow: 0px 4px 12px rgba(168, 85, 247, 0.25);
        width: 100%;
        transition: all 0.3s ease;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 4. แถบเมนูด้านข้าง
st.sidebar.title("☯️ เมนูดูดวงเทพมงคล")
selected_menu = st.sidebar.radio(
    "กรุณาเลือกประเภทการทำนาย:",
    ["🃏 เปิดไพ่ยิปซีทำนายดวง", "☯️ เซียมซีเทพเซียนห้องสิน 49 ใบ"],
)

# ==========================================
# 🟢 เมนูที่ 1: ระบบเปิดไพ่ยิปซีทำนายดวง
# ==========================================
if selected_menu == "🃏 เปิดไพ่ยิปซีทำนายดวง":
    st.markdown(
        '<div class="main-title">🔮 เปิดไพ่ยิปซีทำนายดวง โดยพี่หมอวี 🔮</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-title">✨ มงคลทายทาย ส่องดวงชะตาชี้ทางสว่าง ✨</div>',
        unsafe_allow_html=True,
    )

    st.info("💡 ตั้งจิตอธิษฐานนึกถึงเรื่องที่ต้องการถาม แล้วกดปุ่มสุ่มเปิดไพ่ยิปซี")

    if st.button("✨ กดเพื่อสุ่มเปิดไพ่ยิปซี (3 ใบ)"):
        with st.spinner("🔮 กำลังสุ่มจับไพ่ยิปซี 3 ใบ..."):
            time.sleep(0.5)
            st.session_state["tarot_main_cards"] = random.sample(
                list(TAROT_CARDS_RAW.keys()), 3
            )
            if "tarot_extra_cards" in st.session_state:
                del st.session_state["tarot_extra_cards"]

    if "tarot_main_cards" in st.session_state:
        st.markdown(
            "<h4 style='text-align: center; color: #6b21a8; margin-top: 10px; margin-bottom: 10px;'>🔮 ไพ่ยิปซีหลัก 3 ใบของคุณ</h4>",
            unsafe_allow_html=True,
        )

        main_list = st.session_state["tarot_main_cards"]
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]

        for idx, card_id in enumerate(main_list):
            card_info = TAROT_CARDS_RAW[card_id]
            img_data = load_card_image_base64(card_info["url"])

            with cols[idx]:
                st.image(
                    img_data,
                    caption=f"ใบที่ {idx+1}",
                    use_container_width=True,
                )
                st.markdown(
                    f'<div class="result-box-small"><b>{card_info["name"]}</b><br><span style="color:#3b0764;">{card_info["meaning"]}</span></div>',
                    unsafe_allow_html=True,
                )

        st.write("")

        if st.button("➕ กดสุ่มไพ่เพิ่ม (2 ใบ)"):
            with st.spinner("🔮 กำลังสุ่มจับไพ่ยิปซีเพิ่ม 2 ใบ..."):
                time.sleep(0.5)
                available_cards = [
                    c
                    for c in TAROT_CARDS_RAW.keys()
                    if c not in st.session_state["tarot_main_cards"]
                ]
                st.session_state["tarot_extra_cards"] = random.sample(
                    available_cards, 2
                )

    if "tarot_extra_cards" in st.session_state:
        st.markdown(
            "<h4 style='text-align: center; color: #d946ef; margin-top: 15px; margin-bottom: 10px;'>✨ ไพ่ทำนายเพิ่มเติม 2 ใบ</h4>",
            unsafe_allow_html=True,
        )

        extra_list = st.session_state["tarot_extra_cards"]
        col_ex1, col_ex2 = st.columns(2)
        extra_cols = [col_ex1, col_ex2]

        for idx, card_id in enumerate(extra_list):
            card_info = TAROT_CARDS_RAW[card_id]
            img_data = load_card_image_base64(card_info["url"])

            with extra_cols[idx]:
                st.image(
                    img_data,
                    caption=f"ใบเพิ่มที่ {idx+1}",
                    use_container_width=True,
                )
                st.markdown(
                    f'<div class="result-box-small" style="border-color:#d946ef;"><b>{card_info["name"]}</b><br><span style="color:#3b0764;">{card_info["meaning"]}</span></div>',
                    unsafe_allow_html=True,
                )


# ==========================================
# 🟣 เมนูที่ 2: เซียมซีเทพเซียนห้องสิน 49 ใบ (แยกคำทำนายและสัญลักษณ์รายใบ)
# ==========================================
elif selected_menu == "☯️ เซียมซีเทพเซียนห้องสิน 49 ใบ":

    SIAMSI_49 = {
        1: {
            "title": "อากงเทพสามตาเอ้อหลางเสิน (ปราบมารประทานพร)",
            "summary": "ดวงตามหาเทพส่องสว่าง อุปสรรคพ่ายแพ้ภัย",
            "symbol": "👁️",
            "color1": "#6b21a8",
            "color2": "#3b0764",
            "work_money": "การงานโดดเด่น มีสติปัญญาแก้ปัญหาได้ทุกรูปแบบ ผู้ใหญ่เมตตาเอ็นดูสนับสนุน การเงินคล่องตัวดี มีลาภจากการงานและโชคลาภ",
            "love": "คนโสดพบคนดีที่ถูกใจ เป็นคู่แท้สนับสนุนกัน คนมีคู่ความสัมพันธ์แน่นแฟ้น เข้าใจกันลึกซึ้ง",
            "advice": "จงเชื่อมั่นในสติปัญญาและสัญชาตญาณของตัวเอง มารไม่มี บารมีไม่เกิด ความเพียรจะนำมาซึ่งความสำเร็จ",
        },
        2: {
            "title": "นาจาเหยียบกงล้อเพลิง (ชัยชนะอันว่องไว)",
            "summary": "ความสำเร็จรวดเร็วปานกามนิต ชนะอุปสรรคเด็ดขาด",
            "symbol": "🔥",
            "color1": "#991b1b",
            "color2": "#450a0a",
            "work_money": "การงานก้าวหน้ารวดเร็ว มีโปรเจกต์ใหม่เข้ามาตลอด การตัดสินใจเด็ดขาดนำผลงานดีเยี่ยม การเงินไหลเวียนดี มีลาภฟลุ๊กๆ",
            "love": "ความรักสดใส มีเสน่ห์แรง คนโสดมีคนเข้ามาจีบมากมาย คนมีคู่ราบรื่น เกณฑ์เดินทางร่วมกัน",
            "advice": "อย่ากลัวการเปลี่ยนแปลง จงกล้าคิดกล้าทำ ความมุ่งมั่นเด็ดเดี่ยวจะนำพาท่านสู่ชัยชนะ",
        },
        3: {
            "title": "มหาเทพเจียงจื่อหยาบัญชาทัพ (ความสำเร็จแห่งปัญญา)",
            "summary": "สติปัญญาชนะงานใหญ่ ได้รับเกียรติยศชื่อเสียง",
            "symbol": "📜",
            "color1": "#1e3a8a",
            "color2": "#172554",
            "work_money": "การงานก้าวหน้า ได้รับความไว้วางใจให้คุมงานใหญ่ มีวิสัยทัศน์กว้างไกล การเงินมั่นคง มีเกณฑ์ได้เงินก้อนใหญ่",
            "love": "คนโสดพบคนมีความรู้ความสามารถ เป็นคู่คิดคู่ชีวิต คนมีคู่มั่นคง สนับสนุนกัน",
            "advice": "จงใช้สติปัญญาและวิสัยทัศน์ในการดำเนินชีวิต ความเพียรพยายามจะนำพาความสำเร็จที่ยั่งยืน",
        },
        4: {
            "title": "เจ้าแม่หนี่วาประทานพร (เยียวยาและฟื้นฟู)",
            "summary": "สุขภาพแข็งแรง ฟื้นฟูจิตใจ ความสัมพันธ์สดใส",
            "symbol": "🌸",
            "color1": "#831843",
            "color2": "#500724",
            "work_money": "การงานราบรื่น ปัญหาเก่าได้รับการแก้ไข ได้รับความช่วยเหลือจากเพื่อนร่วมงาน การเงินฟื้นตัวดีขึ้นเรื่อยๆ",
            "love": "ความรักสมหวัง คนโสดพบคนเมตตาจิตใจดี คนมีคู่กลับมาเข้าใจกันลึกซึ้งผูกพันกว่าเดิม",
            "advice": "จงรักษาจิตใจให้ผ่องใสและมีเมตตา พลังงานบวกจะดึงดูดสิ่งดีๆ เข้ามาในชีวิต",
        },
        5: {
            "title": "ศาลามหาเทพแต่งตั้งเซียน (เกียรติยศชื่อเสียง)",
            "summary": "ผลงานได้รับการยอมรับ เลื่อนขั้นยศตำแหน่ง",
            "symbol": "🏛️",
            "color1": "#854d0e",
            "color2": "#422006",
            "work_money": "การงานโดดเด่น ผลงานประจักษ์ ได้โปรโมตหรือรับหน้าที่สำคัญ การเงินดีเยี่ยม รายได้เพิ่มตามความสามารถ",
            "love": "คนโสดมีคนโปรไฟล์ดีเข้ามาจีบ คนมีคู่สนับสนุนกันและกันจนก้าวหน้าในสังคม",
            "advice": "จงมุ่งมั่นสร้างผลงานด้วยความซื่อสัตย์ ความสำเร็จและเกียรติยศจะเป็นของท่านอย่างแน่นอน",
        },
    }

    # เติมคำทำนายแยกต่างกันสำหรับใบที่ 6 ถึง 49
    symbols_list = ["☯️", "⚔️", "🐉", "🛡️", "🌟", "📜", "⚡", "🔮"]
    colors_list = [
        ("#6b21a8", "#3b0764"),
        ("#166534", "#052e16"),
        ("#9a3412", "#431407"),
        ("#1e40af", "#1e1b4b"),
    ]

    for i in range(6, 50):
        c1, c2 = colors_list[i % len(colors_list)]
        sym = symbols_list[i % len(symbols_list)]
        
        if i % 3 == 0:
            summary = "โชคลาภหลั่งไหล การงานสำเร็จก้าวหน้า"
            work = "การงานขยายตัว ได้รับโอกาสใหม่ๆ ที่ท้าทาย การเงินคล่องตัว มีเกณฑ์ได้ลาภลอยหรือเงินก้อนพิเศษ"
            love = "คนโสดมีเสน่ห์โดดเด่น พบคนเก่งเข้ามาคุย คนมีคู่เกณฑ์วางแผนอนาคตร่วมกันอย่างอบอุ่น"
            adv = "จงคว้าโอกาสที่เข้ามาอย่างมั่นใจ ความขยันและจริงใจจะพาไปสู่ความมั่งคั่ง"
        elif i % 3 == 1:
            summary = "เมตตาบารมี ผู้ใหญ่อุปถัมภ์ชี้ช่องทาง"
            work = "ได้รับการสนับสนุนจากผู้ใหญ่หรือผู้บังคับบัญชา ปัญหาได้รับการแก้ไข การเงินมั่นคงไม่ขาดมือ"
            love = "ความรักราบรื่น อบอุ่นเข้าใจกันดี คนโสดมีคนแนะนำมิตรสหายที่ดีมาให้รู้จัก"
            adv = "หมั่นอ่อนน้อมถ่อมตนและกตัญญู บารมีจะส่งผลให้ทำสิ่งใดก็เจริญรุ่งเรือง"
        else:
            summary = "สติปัญญาเฉียบแหลม ชนะอุปสรรคทั้งปวง"
            work = "ต้องใช้สติและความรอบคอบในการทำงาน แล้วจะผ่านพ้นทุกอุปสรรคได้ราบรื่น การเงินประหยัดเก็บออมได้ดี"
            love = "ความสัมพันธ์ค่อยเป็นค่อยไป ชะลอความใจร้อน คนโสดเน้นพัฒนาตัวเองแล้วความรักดีๆ จะตามมา"
            adv = "ความใจเย็นและความอดทนคือคีย์สำคัญ มุ่งมั่นทำหน้าที่ของตนให้ดีที่สุด"

        SIAMSI_49[i] = {
            "title": f"สาส์นสวรรค์มงคลห้องสิน ใบที่ {i}",
            "summary": summary,
            "symbol": sym,
            "color1": c1,
            "color2": c2,
            "work_money": work,
            "love": love,
            "advice": adv,
        }

    st.markdown(
        '<div class="main-title">☯️ เซียมซีเทพเซียนห้องสิน 49 ใบ ☯️</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-title">✨ สำรับวิจิตร 49 มหาโชค - ตั้งจิตอธิษฐานแล้วเขย่าติ้วเสี่ยงทาย ✨</div>',
        unsafe_allow_html=True,
    )

    if st.button("🎋 เขย่ากระบอกเซียมซีสวรรค์"):
        with st.spinner("⏳ กำลังเขย่ากระบอกเซียมซีมหาเทพห้องสิน..."):
            time.sleep(0.8)
            num = random.randint(1, 49)
            st.session_state["siamsi_result"] = num

    if "siamsi_result" in st.session_state:
        result_num = st.session_state["siamsi_result"]
        card_info = SIAMSI_49[result_num]

        st.markdown("---")
        img_url = generate_siamsi_card_svg(
            card_info["title"],
            result_num,
            card_info["symbol"],
            card_info["color1"],
            card_info["color2"],
        )

        col1, col2 = st.columns([1, 1.2])

        with col1:
            st.image(
                img_url,
                caption=f"ใบที่ {result_num}: {card_info['title']}",
                use_container_width=True,
            )

        with col2:
            st.markdown(
                f"""
            <div class="result-box">
                <h4 style="color: #9333ea; margin-bottom: 2px;">ใบที่ {result_num} / 49</h4>
                <h3 style="color: #6b21a8; margin-top: 0;">{card_info['title']}</h3>
                <p style="font-size: 1rem; font-weight: bold; color: #d946ef; margin-top: 5px; text-align: center;">
                    ✨ {card_info['summary']} ✨
                </p>
                <hr style="border-top: 1px dashed #facc15;">
                <p class="pred-header">💼 การงาน & การเงิน:</p>
                <p style="color: #3b0764; font-size: 0.95rem;">{card_info['work_money']}</p>
                <p class="pred-header">❤️ ความรัก:</p>
                <p style="color: #3b0764; font-size: 0.95rem;">{card_info['love']}</p>
                <p class="pred-header">💡 ข้อคิดสติปัญญา:</p>
                <p style="color: #3b0764; font-size: 0.95rem; font-style: italic;">{card_info['advice']}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
    
