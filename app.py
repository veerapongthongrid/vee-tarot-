import random
import time
import streamlit as st

# 1. ตั้งค่าหน้าเพจ Streamlit
st.set_page_config(
    page_title="ระบบดูดวงพี่หมอวี - ไพ่ยิปซี & เซียมซีห้องสิน",
    page_icon="☯️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 2. ตกแต่ง CSS รวม โทนเทพมงคลจีน (ขาว-ทอง-ม่วงอ่อน-ชมพูดอกท้อ)
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

    .main-title {
        text-align: center;
        color: #7e22ce;
        font-size: 2rem;
        font-weight: bold;
        text-shadow: 0px 2px 10px rgba(234, 179, 8, 0.4);
        margin-bottom: 5px;
    }
    
    .sub-title {
        text-align: center;
        color: #a855f7;
        font-size: 1rem;
        margin-bottom: 20px;
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
        margin-top: 10px;
        margin-bottom: 3px;
        font-size: 1rem;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #a855f7 0%, #d946ef 100%);
        color: white;
        font-size: 1.15rem;
        font-weight: bold;
        border-radius: 25px;
        border: 2px solid #fef08a;
        box-shadow: 0px 4px 15px rgba(168, 85, 247, 0.3);
        width: 100%;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0px 6px 20px rgba(217, 70, 239, 0.5);
        color: #fef08a;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# 3. แถบเมนูด้านข้างสำหรับเลือกประเภทการทำนาย
st.sidebar.title("☯️ เมนูดูดวงเทพมงคล")
selected_menu = st.sidebar.radio(
    "กรุณาเลือกประเภทการทำนาย:",
    ["🃏 เปิดไพ่ยิปซีทำนายดวง", "☯️ เซียมซีเทพเซียนห้องสิน 49 ใบ"],
)

# ==========================================
# 🟢 เมนูที่ 1: ระบบเปิดไพ่ยิปซีทำนายดวง (เรียงแนวนอนแถวละ 2 ใบ)
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

    # เปลี่ยนลิงก์รูปภาพเป็น CDN ภาพคุณภาพสูงที่โหลดติดชัวร์
    TAROT_CARDS = {
        1: {
            "name": "The Fool (ผู้เริ่มต้น)",
            "meaning": "การเริ่มต้นใหม่ การเดินทางครั้งใหม่ ความเป็นอิสระ มีโชคจากการกล้าเสี่ยง ให้ทำตามหัวใจ",
            "img": "https://picsum.photos/id/1025/400/600",
        },
        2: {
            "name": "The Magician (นักมายากล)",
            "meaning": "ความสามารถรอบด้าน การติดต่อสื่อสารสำเร็จ ไอเดียสร้างสรรค์ เงินทองมาจากความสามารถ",
            "img": "https://picsum.photos/id/1062/400/600",
        },
        3: {
            "name": "The High Priestess (นักบวชหญิง)",
            "meaning": "สัญชาตญาณแม่นยำ เสน่ห์ดึงดูด ความลึกลับ มีโชคด้านลางสังหรณ์ ให้เชื่อมั่นในความคิดแรก",
            "img": "https://picsum.photos/id/1069/400/600",
        },
        4: {
            "name": "The Empress (จักรพรรดินี)",
            "meaning": "ความอุดมสมบูรณ์ ความรักอบอุ่น การเติบโต มั่งคั่ง มีเกณฑ์ได้รับข่าวดีเรื่องเงินทอง",
            "img": "https://picsum.photos/id/1080/400/600",
        },
        5: {
            "name": "The Emperor (จักรพรรดิ)",
            "meaning": "อำนาจบารมี ความมั่นคง การได้รับการสนับสนุนจากผู้ใหญ่ งานใหญ่ประสบความสำเร็จ",
            "img": "https://picsum.photos/id/1074/400/600",
        },
        6: {
            "name": "The Lovers (คนรัก)",
            "meaning": "ความรักสมหวัง การตัดสินใจครั้งสำคัญ พันธมิตรที่ดี ความสัมพันธ์ก้าวหน้าหวานชื่น",
            "img": "https://picsum.photos/id/1027/400/600",
        },
        7: {
            "name": "The Sun (ดวงอาทิตย์)",
            "meaning": "ความสำเร็จสูงสุด ข่าวดี ชื่อเสียง ความสุขความสดใส ปัญหาหมดไป ได้รับโชคลาภใหญ่",
            "img": "https://picsum.photos/id/1015/400/600",
        },
        8: {
            "name": "Wheel of Fortune (กงล้อแห่งโชคชะตา)",
            "meaning": "โชคชะตาเปลี่ยนไปในทางที่ดี จังหวะชีวิตเปิด ได้รับโอกาสทอง โชคลาภฟลุ๊กๆ ไหลมา",
            "img": "https://picsum.photos/id/1039/400/600",
        },
    }

    st.info("💡 ตั้งจิตอธิษฐานนึกถึงเรื่องที่ต้องการถาม แล้วกดปุ่มสุ่มเปิดไพ่ยิปซี")

    # ปุ่มสุ่มหลัก 3 ใบ
    if st.button("✨ กดเพื่อสุ่มเปิดไพ่ยิปซี (3 ใบ)"):
        with st.spinner("🔮 กำลังตั้งจิตอธิษฐานและสุ่มจับไพ่ 3 ใบ..."):
            time.sleep(1.2)
            st.session_state["tarot_main_cards"] = random.sample(
                list(TAROT_CARDS.keys()), 3
            )
            if "tarot_extra_cards" in st.session_state:
                del st.session_state["tarot_extra_cards"]

    # แสดงผลไพ่หลัก 3 ใบ (จัดลง Layout 2 ช่องแนวนอน)
    if "tarot_main_cards" in st.session_state:
        st.markdown("---")
        st.markdown(
            "<h3 style='text-align: center; color: #6b21a8;'>🔮 ไพ่ยิปซีหลัก 3 ใบของคุณ</h3>",
            unsafe_allow_html=True,
        )

        main_list = st.session_state["tarot_main_cards"]
        
        # แถวที่ 1: แสดง 2 ใบแรก
        col1, col2 = st.columns(2)
        with col1:
            card = TAROT_CARDS[main_list[0]]
            st.image(card["img"], caption=f"ใบที่ 1: {card['name']}", use_column_width=True)
            st.markdown(f'<div class="result-box"><b>{card["name"]}</b><br><span style="font-size:0.9rem;">{card["meaning"]}</span></div>', unsafe_allow_html=True)
            
        with col2:
            card = TAROT_CARDS[main_list[1]]
            st.image(card["img"], caption=f"ใบที่ 2: {card['name']}", use_column_width=True)
            st.markdown(f'<div class="result-box"><b>{card["name"]}</b><br><span style="font-size:0.9rem;">{card["meaning"]}</span></div>', unsafe_allow_html=True)

        # แถวที่ 2: แสดงใบที่ 3 ตรงกลาง
        _, col_mid, _ = st.columns([0.2, 1, 0.2])
        with col_mid:
            card = TAROT_CARDS[main_list[2]]
            st.image(card["img"], caption=f"ใบที่ 3: {card['name']}", use_column_width=True)
            st.markdown(f'<div class="result-box"><b>{card["name"]}</b><br><span style="font-size:0.9rem;">{card["meaning"]}</span></div>', unsafe_allow_html=True)

        st.write("")

        # ปุ่มกดสุ่มเพิ่ม 2 ใบ
        if st.button("➕ กดสุ่มไพ่เพิ่ม (2 ใบ)"):
            with st.spinner("🔮 กำลังตั้งจิตอธิษฐานและจับไพ่เพิ่ม 2 ใบ..."):
                time.sleep(1)
                available_cards = [
                    c
                    for c in TAROT_CARDS.keys()
                    if c not in st.session_state["tarot_main_cards"]
                ]
                st.session_state["tarot_extra_cards"] = random.sample(
                    available_cards, 2
                )

    # แสดงผลไพ่เพิ่ม 2 ใบ (เรียงแนวนอน 2 ช่อง)
    if "tarot_extra_cards" in st.session_state:
        st.markdown("---")
        st.markdown(
            "<h3 style='text-align: center; color: #d946ef;'>✨ ไพ่ทำนายเพิ่มเติม 2 ใบ</h3>",
            unsafe_allow_html=True,
        )

        extra_list = st.session_state["tarot_extra_cards"]
        col_ex1, col_ex2 = st.columns(2)
        
        with col_ex1:
            card = TAROT_CARDS[extra_list[0]]
            st.image(card["img"], caption=f"ใบเพิ่มที่ 1: {card['name']}", use_column_width=True)
            st.markdown(f'<div class="result-box" style="border-color:#d946ef;"><b>{card["name"]}</b><br><span style="font-size:0.9rem;">{card["meaning"]}</span></div>', unsafe_allow_html=True)
            
        with col_ex2:
            card = TAROT_CARDS[extra_list[1]]
            st.image(card["img"], caption=f"ใบเพิ่มที่ 2: {card['name']}", use_column_width=True)
            st.markdown(f'<div class="result-box" style="border-color:#d946ef;"><b>{card["name"]}</b><br><span style="font-size:0.9rem;">{card["meaning"]}</span></div>', unsafe_allow_html=True)


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
            "advice": "จงเชื่อมั่นในสติปัญญาและสัญชาตญาณของตัวเอง มารไม่มี บารมีไม่เกิด ความเพียรจะนำมาซึ่งความสำเร็จ",
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
    }

    for i in range(6, 50):
        if i not in SIAMSI_49:
            SIAMSI_49[i] = {
                "title": f"สาส์นสวรรค์มงคล ใบที่ {i}",
                "summary": "สิ่งศักดิ์สิทธิ์อำนวยพร ความเจริญรุ่งเรืองบังเกิด",
                "work_money": "การงานก้าวหน้าตามลำดับ มีผู้ใหญ่คอยหนุนหลัง การเงินมั่นคง มีรายได้เข้ามาไม่ขาดสาย",
                "love": "ความรักราบรื่น เข้าใจกันดี คนโสดมีเกณฑ์พบมิตรสหายนำพารักแท้มาให้",
                "advice": "หมั่นทำบุญทานกุศล สะสมบารมี แล้วโชคลาภและความสำเร็จจะสถิตอยู่กับท่าน",
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
            time.sleep(1.2)
            num = random.randint(1, 49)
            st.session_state["siamsi_result"] = num

    if "siamsi_result" in st.session_state:
        result_num = st.session_state["siamsi_result"]
        card_info = SIAMSI_49[result_num]

        st.markdown("---")
        img_url = f"https://picsum.photos/id/{1000 + result_num}/400/600"

        col1, col2 = st.columns([1, 1.2])

        with col1:
            st.image(
                img_url,
                caption=f"ใบที่ {result_num}: {card_info['title']}",
                use_column_width=True,
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
