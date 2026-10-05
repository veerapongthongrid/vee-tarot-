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


# ฟังก์ชันดึงรูปภาพและแปลงเป็น Base64
@st.cache_data(show_spinner=False)
def get_image_base64(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        res = requests.get(url, headers=headers, timeout=5)
        if res.status_code == 200:
            b64 = base64.b64encode(res.content).decode("utf-8")
            return f"data:image/jpeg;base64,{b64}"
    except Exception:
        pass
    return url


# 2. CSS ตกแต่งหน้าเว็บและกรอบเซียมซีพื้นหลังเทพเจ้า
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

    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        background-color: #ffffff !important;
        border: 2px solid #fde047 !important;
        border-radius: 12px !important;
        padding: 12px 15px !important;
        margin-bottom: 10px !important;
        box-shadow: 0px 3px 8px rgba(168, 85, 247, 0.12) !important;
        font-size: 1.05rem !important;
        font-weight: bold !important;
        cursor: pointer !important;
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

    .siamsi-bg-box {
        background: linear-gradient(rgba(255, 255, 255, 0.92), rgba(254, 243, 199, 0.92)), 
                    url('https://images.unsplash.com/photo-1544717305-2782549b5136?w=800&auto=format&fit=crop&q=80');
        background-size: cover;
        background-position: center;
        border: 2.5px solid #ca8a04;
        border-radius: 15px;
        padding: 18px;
        box-shadow: 0px 8px 25px rgba(168, 85, 247, 0.25);
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .result-box {
        background-color: rgba(255, 255, 255, 0.95);
        border: 2px solid #facc15;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0px 6px 18px rgba(168, 85, 247, 0.15);
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .result-box-small {
        background-color: rgba(255, 255, 255, 0.95);
        border: 1.5px solid #facc15;
        border-radius: 8px;
        padding: 8px;
        box-shadow: 0px 3px 8px rgba(168, 85, 247, 0.12);
        margin-top: 6px;
        font-size: 0.8rem;
        line-height: 1.3;
        text-align: center;
    }

    .pred-header {
        color: #7e22ce;
        font-weight: bold;
        margin-top: 10px;
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

# 3. แถบเมนูด้านข้าง
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

    TAROT_CARDS = {
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

    st.info(
        "💡 ตั้งจิตอธิษฐานนึกถึงเรื่องที่ต้องการถาม แล้วกดปุ่มสุ่มเปิดไพ่ยิปซี"
    )

    if st.button("✨ กดเพื่อสุ่มเปิดไพ่ยิปซี (3 ใบ)"):
        with st.spinner("🔮 กำลังสุ่มจับไพ่ยิปซี 3 ใบ..."):
            time.sleep(0.5)
            st.session_state["tarot_main_cards"] = random.sample(
                list(TAROT_CARDS.keys()), 3
            )
            if "tarot_extra_cards" in st.session_state:
                del st.session_state["tarot_extra_cards"]

    if "tarot_main_cards" in st.session_state:
        st.markdown(
            "<h4 style='text-align: center; color: #6b21a8; margin-top: 10px;'>🔮 ไพ่ยิปซีหลัก 3 ใบของคุณ</h4>",
            unsafe_allow_html=True,
        )

        main_list = st.session_state["tarot_main_cards"]
        col1, col2, col3 = st.columns(3)
        cols = [col1, col2, col3]

        for idx, card_id in enumerate(main_list):
            card = TAROT_CARDS[card_id]
            img_b64 = get_image_base64(card["url"])
            with cols[idx]:
                st.image(
                    img_b64, caption=f"ใบที่ {idx+1}", use_container_width=True
                )
                st.markdown(
                    f'<div class="result-box-small"><b>{card["name"]}</b><br><span style="color:#3b0764;">{card["meaning"]}</span></div>',
                    unsafe_allow_html=True,
                )

        st.write("")

        if st.button("➕ กดสุ่มไพ่เพิ่ม (2 ใบ)"):
            with st.spinner("🔮 กำลังสุ่มจับไพ่ยิปซีเพิ่ม 2 ใบ..."):
                time.sleep(0.5)
                available_cards = [
                    c
                    for c in TAROT_CARDS.keys()
                    if c not in st.session_state["tarot_main_cards"]
                ]
                st.session_state["tarot_extra_cards"] = random.sample(
                    available_cards, 2
                )

    if "tarot_extra_cards" in st.session_state:
        st.markdown(
            "<h4 style='text-align: center; color: #d946ef; margin-top: 15px;'>✨ ไพ่ทำนายเพิ่มเติม 2 ใบ</h4>",
            unsafe_allow_html=True,
        )

        extra_list = st.session_state["tarot_extra_cards"]
        col_ex1, col_ex2 = st.columns(2)
        extra_cols = [col_ex1, col_ex2]

        for idx, card_id in enumerate(extra_list):
            card = TAROT_CARDS[card_id]
            img_b64 = get_image_base64(card["url"])
            with extra_cols[idx]:
                st.image(
                    img_b64,
                    caption=f"ใบเพิ่มที่ {idx+1}",
                    use_container_width=True,
                )
                st.markdown(
                    f'<div class="result-box-small" style="border-color:#d946ef;"><b>{card["name"]}</b><br><span style="color:#3b0764;">{card["meaning"]}</span></div>',
                    unsafe_allow_html=True,
                )


# ==========================================
# 🟣 เมนูที่ 2: เซียมซีเทพเซียนห้องสิน 49 ใบ (ระบุรูปภาพตัวละครตามใบเซียมซี)
# ==========================================
elif selected_menu == "☯️ เซียมซีเทพเซียนห้องสิน 49 ใบ":

    # สามารถเปลี่ยนลิงก์รูปภาพในคีย์ "img_url" ของแต่ละใบให้ตรงกับตัวละครห้องสินที่ต้องการได้เลยครับ
    SIAMSI_49 = {
        1: {
            "title": "อากงเทพสามตาเอ้อหลางเสิน (ปราบมารประทานพร)",
            "summary": "ดวงตามหาเทพส่องสว่าง อุปสรรคพ่ายแพ้ภัย",
            "img_url": "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg",  # รูปตัวอย่าง (เปลี่ยนเป็นรูปเอ้อหลางเสินได้)
            "work_money": "การงานโดดเด่น มีสติปัญญาแก้ปัญหาได้ทุกรูปแบบ ผู้ใหญ่เมตตาเอ็นดูสนับสนุน การเงินคล่องตัวดี มีลาภจากการงานและโชคลาภ",
            "love": "คนโสดพบคนดีที่ถูกใจ เป็นคู่แท้สนับสนุนกัน คนมีคู่ความสัมพันธ์แน่นแฟ้น เข้าใจกันลึกซึ้ง",
            "advice": "จงเชื่อมั่นในสติปัญญาและสัญชาตญาณของตัวเอง มารไม่มี บารมีไม่เกิด ความเพียรจะนำมาซึ่งความสำเร็จ",
        },
        2: {
            "title": "นาจาเหยียบกงล้อเพลิง (ชัยชนะอันว่องไว)",
            "summary": "ความสำเร็จรวดเร็วปานกามนิต ชนะอุปสรรคเด็ดขาด",
            "img_url": "https://upload.wikimedia.org/wikipedia/commons/d/de/RWS_Tarot_01_Magician.jpg",  # รูปตัวอย่าง (เปลี่ยนเป็นรูปนาจาได้)
            "work_money": "การงานก้าวหน้ารวดเร็ว มีโปรเจกต์ใหม่เข้ามาตลอด การตัดสินใจเด็ดขาดนำผลงานดีเยี่ยม การเงินไหลเวียนดี มีลาภฟลุ๊กๆ",
            "love": "ความรักสดใส มีเสน่ห์แรง คนโสดมีคนเข้ามาจีบมากมาย คนมีคู่ราบรื่น เกณฑ์เดินทางร่วมกัน",
            "advice": "อย่ากลัวการเปลี่ยนแปลง จงกล้าคิดกล้าทำ ความมุ่งมั่นเด็ดเดี่ยวจะนำพาท่านสู่ชัยชนะ",
        },
        3: {
            "title": "มหาเทพเจียงจื่อหยาบัญชาทัพ (ความสำเร็จแห่งปัญญา)",
            "summary": "สติปัญญาชนะงานใหญ่ ได้รับเกียรติยศชื่อเสียง",
            "img_url": "https://upload.wikimedia.org/wikipedia/commons/8/88/RWS_Tarot_02_High_Priestess.jpg",  # รูปตัวอย่าง (เปลี่ยนเป็นรูปเจียงจื่อหยาได้)
            "work_money": "การงานก้าวหน้า ได้รับความไว้วางใจให้คุมงานใหญ่ มีวิสัยทัศน์กว้างไกล การเงินมั่นคง มีเกณฑ์ได้เงินก้อนใหญ่",
            "love": "คนโสดพบคนมีความรู้ความสามารถ เป็นคู่คิดคู่ชีวิต คนมีคู่มั่นคง สนับสนุนกัน",
            "advice": "จงใช้สติปัญญาและวิสัยทัศน์ในการดำเนินชีวิต ความเพียรพยายามจะนำพาความสำเร็จที่ยั่งยืน",
        },
        4: {
            "title": "เจ้าแม่หนี่วาประทานพร (เยียวยาและฟื้นฟู)",
            "summary": "สุขภาพแข็งแรง ฟื้นฟูจิตใจ ความสัมพันธ์สดใส",
            "img_url": "https://upload.wikimedia.org/wikipedia/commons/d/d2/RWS_Tarot_03_Empress.jpg",
            "work_money": "การงานเริ่มราบรื่น ปัญหาเก่าได้รับการแก้ไข ได้รับความช่วยเหลือจากเพื่อนร่วมงาน การเงินฟื้นตัวดีขึ้นเรื่อยๆ",
            "love": "ความรักสมหวัง คนโสดพบคนเมตตาจิตใจดี คนมีคู่กลับมาเข้าใจกันลึกซึ้งผูกพันกว่าเดิม",
            "advice": "จงรักษาจิตใจให้ผ่องใสและมีเมตตา พลังงานบวกจะดึงดูดสิ่งดีๆ เข้ามาในชีวิต",
        },
        5: {
            "title": "ศาลามหาเทพแต่งตั้งเซียน (เกียรติยศชื่อเสียง)",
            "summary": "ผลงานได้รับการยอมรับ เลื่อนขั้นยศตำแหน่ง",
            "img_url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/RWS_Tarot_04_Emperor.jpg",
            "work_money": "การงานโดดเด่น ผลงานประจักษ์ ได้โปรโมตหรือรับหน้าที่สำคัญ การเงินดีเยี่ยม รายได้เพิ่มตามความสามารถ",
            "love": "คนโสดมีคนโปรไฟล์ดีเข้ามาจีบ คนมีคู่สนับสนุนกันและกันจนก้าวหน้าในสังคม",
            "advice": "จงมุ่งมั่นสร้างผลงานด้วยความซื่อสัตย์ ความสำเร็จและเกียรติยศจะเป็นของท่านอย่างแน่นอน",
        },
    }

    # เติมฐานข้อมูลใบที่ 6 ถึง 49 พร้อมรูปภาพตัวละครสำรอง
    for i in range(6, 50):
        SIAMSI_49[i] = {
            "title": f"สาส์นสวรรค์มงคลห้องสิน ใบที่ {i}",
            "summary": "สิ่งศักดิ์สิทธิ์อำนวยพร ความเจริญรุ่งเรืองบังเกิดในชีวิต",
            "img_url": "https://upload.wikimedia.org/wikipedia/commons/9/90/RWS_Tarot_00_Fool.jpg",  # สามารถระบุรูปเฉพาะใบได้ที่นี่
            "work_money": f"การงานก้าวหน้า ใบที่ {i} ทายว่ามีเกณฑ์ได้รับความสำเร็จ สมหวังในสิ่งที่ลงทุนลงแรงไว้ การเงินคล่องตัวดี",
            "love": "ความรักอบอุ่นเข้าใจกัน คนโสดมีเกณฑ์พบมิตรสหายหรือกัลยาณมิตรนำพาความสุขมาให้",
            "advice": "หมั่นทำความดีและสร้างกุศล ความเพียรพยายามจะนำพาความสำเร็จที่ยั่งยืนมาสู่ท่าน",
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
        # ดึงรูปประจำตัวละครตามใบเซียมซีที่สุ่มได้
        img_b64 = get_image_base64(card_info["img_url"])

        col1, col2 = st.columns([1, 1.2])

        with col1:
            st.image(
                img_b64,
                caption=f"ใบที่ {result_num}: {card_info['title']}",
                use_container_width=True,
            )

        with col2:
            st.markdown(
                f"""
            <div class="siamsi-bg-box">
                <h4 style="color: #7e22ce; margin-bottom: 2px; text-shadow: 0px 1px 2px rgba(255,255,255,0.8);">ใบที่ {result_num} / 49</h4>
                <h3 style="color: #6b21a8; margin-top: 0; font-size: 1.15rem; text-shadow: 0px 1px 2px rgba(255,255,255,0.8);">{card_info['title']}</h3>
                <p style="font-size: 0.95rem; font-weight: bold; color: #b45309; margin-top: 5px; text-align: center; text-shadow: 0px 1px 2px rgba(255,255,255,0.8);">
                    ✨ {card_info['summary']} ✨
                </p>
                <hr style="border-top: 1px dashed #ca8a04;">
                <p class="pred-header">💼 การงาน & การเงิน:</p>
                <p style="color: #3b0764; font-size: 0.9rem; font-weight: 500;">{card_info['work_money']}</p>
                <p class="pred-header">❤️ ความรัก:</p>
                <p style="color: #3b0764; font-size: 0.9rem; font-weight: 500;">{card_info['love']}</p>
                <p class="pred-header">💡 ข้อคิดสติปัญญา:</p>
                <p style="color: #3b0764; font-size: 0.9rem; font-style: italic; font-weight: 500;">{card_info['advice']}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
            
