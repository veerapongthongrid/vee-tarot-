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

# ลิงก์รูปภาพเทพเอ้อหลางเสินของพี่หมอ
ERLANG_IMG_URL = "https://i.postimg.cc/gJr3zxtR/1791185422353.png"


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


# 2. CSS ตกแต่งหน้าเว็บ (ปรับพื้นหลังกล่องข้อความให้รองรับรูปภาพด้านหลังและอ่านง่ายขึ้น)
st.markdown(
    f"""
    <style>
    .stApp {{
        background: linear-gradient(135deg, #fefce8 0%, #fae8ff 40%, #fce7f3 70%, #ffffff 100%);
        color: #3b0764;
        font-family: 'Sarabun', sans-serif;
    }}
    
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #faf5ff 0%, #f3e8ff 100%);
        border-right: 2px solid #fde047;
    }}

    div[data-testid="stRadio"] div[role="radiogroup"] > label {{
        background-color: #ffffff !important;
        border: 2px solid #fde047 !important;
        border-radius: 12px !important;
        padding: 12px 15px !important;
        margin-bottom: 10px !important;
        box-shadow: 0px 3px 8px rgba(168, 85, 247, 0.12) !important;
        font-size: 1.05rem !important;
        font-weight: bold !important;
        cursor: pointer !important;
    }}

    .main-title {{
        text-align: center;
        color: #7e22ce;
        font-size: 1.8rem;
        font-weight: bold;
        text-shadow: 0px 2px 10px rgba(234, 179, 8, 0.4);
        margin-bottom: 2px;
    }}
    
    .sub-title {{
        text-align: center;
        color: #a855f7;
        font-size: 0.95rem;
        margin-bottom: 15px;
    }}

    .siamsi-bg-box {{
        background: linear-gradient(rgba(255, 255, 255, 0.88), rgba(254, 243, 199, 0.88)), 
                    url('{ERLANG_IMG_URL}');
        background-size: cover;
        background-position: center;
        border: 2.5px solid #ca8a04;
        border-radius: 15px;
        padding: 18px;
        box-shadow: 0px 8px 25px rgba(168, 85, 247, 0.25);
        margin-top: 10px;
        margin-bottom: 15px;
    }}

    .result-box-small {{
        background-color: rgba(255, 255, 255, 0.95);
        border: 1.5px solid #facc15;
        border-radius: 8px;
        padding: 8px;
        box-shadow: 0px 3px 8px rgba(168, 85, 247, 0.12);
        margin-top: 6px;
        font-size: 0.8rem;
        line-height: 1.3;
        text-align: center;
    }}

    .pred-header {{
        color: #7e22ce;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 3px;
        font-size: 0.95rem;
    }}

    div.stButton > button {{
        background: linear-gradient(90deg, #a855f7 0%, #d946ef 100%);
        color: white;
        font-size: 1.05rem;
        font-weight: bold;
        border-radius: 20px;
        border: 2px solid #fef08a;
        box-shadow: 0px 4px 12px rgba(168, 85, 247, 0.25);
        width: 100%;
        transition: all 0.3s ease;
    }}
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
# 🟣 เมนูที่ 2: เซียมซีเทพเซียนห้องสิน 49 ใบ
# ==========================================
elif selected_menu == "☯️ เซียมซีเทพเซียนห้องสิน 49 ใบ":

    SIAMSI_49 = {
        1: {
            "title": "อากงเทพสามตาเอ้อหลางเสิน (ปราบมารประทานพร)",
            "summary": "ดวงตามหาเทพส่องสว่าง อุปสรรคพ่ายแพ้ภัย",
            "work_money": "การงานโดดเด่น มีสติปัญญาแก้ปัญหาได้ทุกรูปแบบ ผู้ใหญ่เมตตาเอ็นดูสนับสนุน การเงินคล่องตัวดี มีลาภจากการงานและโชคลาภ",
            "love": "คนโสดพบคนดีที่ถูกใจ เป็นคู่แท้สนับสนุนกัน คนมีคู่ความสัมพันธ์แน่นแฟ้น เข้าใจกันลึกซึ้ง",
            "advice": "จงเชื่อมั่นในสติปัญญาและสัญชาตญาณตัวเอง มารไม่มี บารมีไม่เกิด ความเพียรจะนำมาซึ่งความสำเร็จ",
        },
        2: {
            "title": "นาจาเหยียบกงล้อเพลิง (ชัยชนะอันว่องไว)",
            "summary": "ความสำเร็จรวดเร็วปานกามนิต ชนะอุปสรรคเด็ดขาด",
            "work_money": "การงานก้าวหน้ารวดเร็ว มีโปรเจกต์ใหม่เข้ามาตลอด การตัดสินใจเด็ดขาดนำผลงานดีเยี่ยม การเงินไหลเวียนดี มีลาภฟลุ๊กๆ",
            "love": "ความรักสดใส มีเสน่ห์แรง คนโสดมีคนเข้ามาจีบมากมาย คนมีคู่ราบรื่น เกณฑ์เดินทางร่วมกัน",
            "advice": "อย่ากลัวการเปลี่ยนแปลง จงกล้าคิดกล้าทำ ความมุ่งมั่นเด็ดเดี่ยวจะนำพาท่านสู่ชัยชนะ",
        },
        3: {
            "title": "มหาเทพเจียงจื่อหยาบัญชาทัพ (ความสำเร็จแห่งปัญญา)",
            "summary": "สติปัญญาชนะงานใหญ่ ได้รับเกียรติยศชื่อเสียง",
            "work_money": "การงานก้าวหน้า ได้รับความไว้วางใจให้คุมงานใหญ่ มีวิสัยทัศน์กว้างไกล การเงินมั่นคง มีเกณฑ์ได้เงินก้อนใหญ่",
            "love": "คนโสดพบคนมีความรู้ความสามารถ เป็นคู่คิดคู่ชีวิต คนมีคู่มั่นคง สนับสนุนกัน",
            "advice": "จงใช้สติปัญญาและวิสัยทัศน์ในการดำเนินชีวิต ความเพียรพยายามจะนำพาความสำเร็จที่ยั่งยืน",
        },
        4: {
            "title": "เจ้าแม่หนี่วาประทานพร (เยียวยาและฟื้นฟู)",
            "summary": "สุขภาพแข็งแรง ฟื้นฟูจิตใจ ความสัมพันธ์สดใส",
            "work_money": "การงานเริ่มราบรื่น ปัญหาเก่าได้รับการแก้ไข ได้รับความช่วยเหลือจากเพื่อนร่วมงาน การเงินฟื้นตัวดีขึ้นเรื่อยๆ",
            "love": "ความรักสมหวัง คนโสดพบคนเมตตาจิตใจดี คนมีคู่กลับมาเข้าใจกันลึกซึ้งผูกพันกว่าเดิม",
            "advice": "จงรักษาจิตใจให้ผ่องใสและมีเมตตา พลังงานบวกจะดึงดูดสิ่งดีๆ เข้ามาในชีวิต",
        },
        5: {
            "title": "ศาลามหาเทพแต่งตั้งเซียน (เกียรติยศชื่อเสียง)",
            "summary": "ผลงานได้รับการยอมรับ เลื่อนขั้นยศตำแหน่ง",
            "work_money": "การงานโดดเด่น ผลงานประจักษ์ ได้โปรโมตหรือรับหน้าที่สำคัญ การเงินดีเยี่ยม รายได้เพิ่มตามความสามารถ",
            "love": "คนโสดมีคนโปรไฟล์ดีเข้ามาจีบ คนมีคู่สนับสนุนกันและกันจนก้าวหน้าในสังคม",
            "advice": "จงมุ่งมั่นสร้างผลงานด้วยความซื่อสัตย์ ความสำเร็จและเกียรติยศจะเป็นของท่านอย่างแน่นอน",
        },
        6: {
            "title": "เทพเจ้าโชคลาภปีกาน (โชคลาภมั่งคั่ง)",
            "summary": "เงินทองไหลมาเทมา ขจัดหนี้สินพบความมั่งคั่ง",
            "work_money": "การค้าขายดีเยี่ยม ยอดขายทะลุเป้า เงินทองไหลเข้าไม่ขาดสาย มีเกณฑ์ได้รับโชคลาภก้อนใหญ่จากการลงทุน",
            "love": "คนโสดพบคู่สายเปย์หรือชวนกันตั้งตัว คนมีคู่เกณฑ์สร้างฐานะซื้อทรัพย์สินชิ้นใหญ่ร่วมกัน",
            "advice": "หมั่นทำบุญแบ่งปันและสร้างกุศล ยิ่งให้ออกไปจะยิ่งได้กลับคืนมาเป็นเท่าทวีคูณ",
        },
        7: {
            "title": "เล้งเอี๊ยงกุนทหารเทพมังกร (พลังอำนาจและความกล้า)",
            "summary": "ขจัดภยันตรายทั้งปวง มีชัยชนะเหนือศัตรูคู่แข่ง",
            "work_money": "การงานชนะคู่แข่ง ชนะการประมูลหรือแข่งขัน มีอำนาจบารมีคุมบริวารได้ดี การเงินรับทรัพย์มั่นคง",
            "love": "ความรักมีความปกป้องดูแลกันดี คนโสดพบคนบุคลิกเป็นผู้นำ มีความจริงใจสูง",
            "advice": "จงกล้าเผชิญหน้ากับความจริง ความซื่อสัตย์และความกล้าหาญจะปกป้องท่านจากสิ่งไม่ดี",
        },
        8: {
            "title": "เทพกระบี่สวรรค์หลี่จิ้ง (ความระเบียบและมั่นคง)",
            "summary": "ครอบครัวร่มเย็นเป็นสุข วางรากฐานชีวิตมั่นคง",
            "work_money": "การงานมีความเป็นระบบระเบียบ บริหารจัดการงานใหญ่ได้อย่างมีประสิทธิภาพ การเงินเสถียรภาพดี ปลอดภัย",
            "love": "ครอบครัวมีความสุข ปรับความเข้าใจกันได้ คนโสดเกณฑ์พบคนผู้ใหญ่แนะนำให้รู้จัก",
            "advice": "ความมีวินัยและการวางแผนที่ดี คือรากฐานสำคัญที่จะทำให้ชีวิตประสบความสำเร็จยั่งยืน",
        },
        9: {
            "title": "เทพเซียนกิมจ๊า (ขุมทรัพย์ทองคำ)",
            "summary": "ได้รับทรัพย์สินมรดก มีเกณฑ์ขยับขยายธุรกิจ",
            "work_money": "ได้รับโอกาสทำธุรกิจใหม่ๆ หรือได้มรดกโชคลาภจากผู้ใหญ่ การเงินอุดมสมบูรณ์ คล่องตัวสูง",
            "love": "คนโสดพบคนฐานะดีเข้ามาดูแล คนมีคู่ราบรื่น ช่วยกันเก็บหอมรอมริบได้เงินก้อน",
            "advice": "เมื่อมีโชคลาภเข้ามา จงบริหารจัดการอย่างชาญฉลาด อย่าประมาทในการใช้จ่าย",
        },
        10: {
            "title": "เทพเซียนมูจ๊า (เงียบสงบชนะความวุ่นวาย)",
            "summary": "จิตใจสงบพบทางสว่าง ปัญหาหนักเบาลงทันที",
            "work_money": "การงานที่เคยคลุมเครือจะเริ่มชัดเจน ปัญหาที่ยุ่งยากคลายตัวลงด้วยความสงบ การเงินค่อยๆ ฟื้นตัว",
            "love": "คนโสดรักสงบ ไม่รีบร้อน จะพบคนใจเย็น คนมีคู่เข้าใจและเป็นที่พักใจให้แก่กัน",
            "advice": "ใช้ความสงบสยบความเคลื่อนไหว สติและความนิ่งจะช่วยขจัดความวุ่นวายรอบตัวได้ดีที่สุด",
        },
    }

    names_11_49 = [
        "มหาเทพไท่กงหนุนนำ",
        "กระบี่วิเศษปราบมาร",
        "ค่ายกลสุริยันจันทรา",
        "บัวสวรรค์แปดกลีบ",
        "คัมภีร์สวรรค์ห้องสิน",
        "อาคมวิเศษคุ้มดวง",
        "ค่ายกลเก้าสวรรค์",
        "พัดวิเศษแห่งความเย็น",
        "ไข่มุกราตรีสว่างไสว",
        "คฑามหาอำนาจเซียน",
        "สะพานสายรุ้งสวรรค์",
        "กลองศึกประกาศชัย",
        "น้ำทิพย์ชะล้างความเศร้า",
        "คลังสมบัติฮ่องเต้",
        "ธงประกาศิตสวรรค์",
        "เตาหลอมโอสถวิเศษ",
        "คัมภีร์ฟ้าดินลิขิต",
        "ระฆังทองคำกังวาน",
        "ศาลาเซียนแปดทิศ",
        "เสือติดปีกมหาอำนาจ",
        "มังกรทองผงาดฟ้า",
        "ดอกบัวขาวเหนือโคลนตม",
        "คัมภีร์ลับสวรรค์ชั้นฟ้า",
        "หินผาศักดิ์สิทธิ์มั่นคง",
        "คันฉ่องส่องความจริง",
        "เกวียนทองขนทรัพย์",
        "นกกระสาคาบเกี่ยวเงินทอง",
        "เต่ามังกรอายุยืนยาว",
        "ธนูเงินยิงตรงเป้าหมาย",
        "ศาลาชมจันทร์สราญใจ",
        "คัมภีร์หมอดูเทวดา",
        "ปราสาททองคำสวรรค์",
        "คทาหยกประทานพร",
        "กระบี่บินทะยานฟ้า",
        "ดอกโบตั๋นบานสะพรั่ง",
        "ป้ายทองคำประกาศิต",
        "เรือสำเภาทองคำ",
        "พระอาทิตย์สาดส่อง",
        "สวรรค์บันดาลโชค",
    ]

    for idx, name in enumerate(names_11_49, start=11):
        SIAMSI_49[idx] = {
            "title": f"สาส์นสวรรค์มงคลห้องสิน ใบที่ {idx} ({name})",
            "summary": f"ดวงชะตาฟ้าประทานพร เปิดทางสว่างแห่งความสำเร็จในใบที่ {idx}",
            "work_money": f"การงานและธุรกิจเจริญก้าวหน้า การเงินหมุนเวียนคล่องตัว มีโอกาสรับทรัพย์ก้อนโตจากความตั้งใจ",
            "love": f"ความรักราบรื่นและอบอุ่น คนโสดมีเกณฑ์พบกัลยาณมิตรที่ดีเข้ามาในชีวิต",
            "advice": "ตั้งจิตมั่นทำความดี หมั่นสร้างกุศล ความเพียรพยายามจะนำพาความสำเร็จที่ยั่งยืนมาสู่ท่าน",
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

        # แสดงกล่องข้อความคำทำนายที่มีรูปเทพเอ้อหลางเสินเป็นพื้นหลัง
        st.markdown(
            f"""
        <div class="siamsi-bg-box">
            <h4 style="color: #7e22ce; margin-bottom: 2px; text-shadow: 0px 1px 2px rgba(255,255,255,0.9);">ใบที่ {result_num} / 49</h4>
            <h3 style="color: #6b21a8; margin-top: 0; font-size: 1.15rem; text-shadow: 0px 1px 2px rgba(255,255,255,0.9);">{card_info['title']}</h3>
            <p style="font-size: 0.95rem; font-weight: bold; color: #b45309; margin-top: 5px; text-align: center; text-shadow: 0px 1px 2px rgba(255,255,255,0.9);">
                ✨ {card_info['summary']} ✨
            </p>
            <hr style="border-top: 1px dashed #ca8a04;">
            <p class="pred-header">💼 การงาน & การเงิน:</p>
            <p style="color: #3b0764; font-size: 0.9rem; font-weight: bold;">{card_info['work_money']}</p>
            <p class="pred-header">❤️ ความรัก:</p>
            <p style="color: #3b0764; font-size: 0.9rem; font-weight: bold;">{card_info['love']}</p>
            <p class="pred-header">💡 ข้อคิดสติปัญญา:</p>
            <p style="color: #3b0764; font-size: 0.9rem; font-style: italic; font-weight: bold;">{card_info['advice']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )
        
