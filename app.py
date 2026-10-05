import base64
import random
import time
import streamlit as st

# 1. ตั้งค่าหน้าเพจ Streamlit
st.set_page_config(
    page_title="ระบบดูดวงพี่หมอวี - ไพ่ยิปซี & เซียมซีห้องสิน",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded",
)


# ฟังก์ชันสร้างหน้าไพ่ยิปซี Rider-Waite คลาสสิกแบบ SVG ฝังลงในโค้ด 100% (รูปไม่ดับชัวร์)
def generate_tarot_card(
    title_en, title_th, symbol, roman_num, bg_color="#fffbeb"
):
    svg_code = f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 320" width="100%" height="100%">
        <defs>
            <linearGradient id="goldBorder" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ca8a04" />
                <stop offset="50%" stop-color="#facc15" />
                <stop offset="100%" stop-color="#854d0e" />
            </linearGradient>
        </defs>
        <!-- กรอบไพ่ยิปซีคลาสสิก -->
        <rect x="4" y="4" width="192" height="312" rx="8" fill="{bg_color}" stroke="url(#goldBorder)" stroke-width="4"/>
        <rect x="10" y="10" width="180" height="300" rx="4" fill="none" stroke="#b45309" stroke-width="1.5"/>
        
        <!-- เลขโรมันประจำไพ่ -->
        <text x="100" y="32" font-family="'Times New Roman', serif" font-size="16" font-weight="bold" text-anchor="middle" fill="#78350f">{roman_num}</text>
        
        <!-- รูปหน้าไพ่ยิปซีคลาสสิก -->
        <rect x="20" y="42" width="160" height="190" rx="4" fill="#ffffff" stroke="#d97706" stroke-width="1"/>
        <circle cx="100" cy="137" r="48" fill="#fef3c7" stroke="#b45309" stroke-width="1"/>
        <text x="100" y="153" font-family="'Sarabun', sans-serif" font-size="48" text-anchor="middle" fill="#78350f">{symbol}</text>
        
        <!-- ป้ายชื่อไพ่ -->
        <rect x="20" y="242" width="160" height="55" rx="4" fill="#fffbeb" stroke="#b45309" stroke-width="1"/>
        <text x="100" y="264" font-family="'Times New Roman', serif" font-size="13" font-weight="bold" text-anchor="middle" fill="#78350f">{title_en}</text>
        <text x="100" y="284" font-family="'Sarabun', sans-serif" font-size="12" font-weight="bold" text-anchor="middle" fill="#92400e">{title_th}</text>
    </svg>
    """
    b64 = base64.b64encode(svg_code.encode("utf-8")).decode("utf-8")
    return f"data:image/svg+xml;base64,{b64}"


# 2. ตกแต่ง CSS โทนเทพมงคลจีน + บังคับรูปไพ่เรียงแนวนอน 3 ใบพอดีจอมือถือ
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

    /* บังคับคอลัมน์ให้อยู่แนวนอน 3 ช่องไม่ตกแถวบนจอมือถือ */
    [data-testid="column"] {
        width: 33.33% !important;
        flex: 1 1 33.33% !important;
        min-width: 33.33% !important;
    }

    /* ย่อขนาดไพ่ให้เล็กพอดีตาเห็นครบ 3 ใบในจอเดียว */
    div[data-testid="stImage"] > img {
        max-height: 150px !important;
        width: auto !important;
        margin: 0 auto;
        display: block;
    }

    .result-box-small {
        background-color: rgba(255, 255, 255, 0.95);
        border: 1.5px solid #facc15;
        border-radius: 8px;
        padding: 6px;
        box-shadow: 0px 3px 8px rgba(168, 85, 247, 0.12);
        margin-top: 4px;
        font-size: 0.75rem;
        line-height: 1.25;
        text-align: center;
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

# 3. แถบเมนูด้านข้าง
st.sidebar.title("☯️ เมนูดูดวงเทพมงคล")
selected_menu = st.sidebar.radio(
    "กรุณาเลือกประเภทการทำนาย:",
    ["🃏 เปิดไพ่ยิปซีทำนายดวง", "☯️ เซียมซีเทพเซียนห้องสิน 49 ใบ"],
)

# ==========================================
# 🟢 เมนูที่ 1: ระบบเปิดไพ่ยิปซีทำนายดวง (3 ใบเรียงแนวนอน + สุ่มเพิ่ม 2 ใบ)
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
            "img": generate_tarot_card("THE FOOL", "ผู้เริ่มต้น", "🃏", "0"),
        },
        2: {
            "name": "The Magician (นักมายากล)",
            "meaning": "ความสามารถรอบด้าน การติดต่อสื่อสารสำเร็จ เงินทองมาจากความสามารถ",
            "img": generate_tarot_card(
                "THE MAGICIAN", "นักมายากล", "🪄", "I"
            ),
        },
        3: {
            "name": "The High Priestess (นักบวชหญิง)",
            "meaning": "สัญชาตญาณแม่นยำ เสน่ห์ดึงดูด มีโชคด้านลางสังหรณ์ ให้เชื่อมั่นความคิดแรก",
            "img": generate_tarot_card(
                "HIGH PRIESTESS", "นักบวชหญิง", "🌙", "II"
            ),
        },
        4: {
            "name": "The Empress (จักรพรรดินี)",
            "meaning": "ความอุดมสมบูรณ์ ความรักอบอุ่น มั่งคั่ง มีเกณฑ์ได้รับข่าวดีเรื่องเงินทอง",
            "img": generate_tarot_card(
                "THE EMPRESS", "จักรพรรดินี", "👑", "III"
            ),
        },
        5: {
            "name": "The Emperor (จักรพรรดิ)",
            "meaning": "อำนาจบารมี ความมั่นคง การได้รับการสนับสนุนจากผู้ใหญ่ งานใหญ่สำเร็จ",
            "img": generate_tarot_card("THE EMPEROR", "จักรพรรดิ", "⚔️", "IV"),
        },
        6: {
            "name": "The Lovers (คนรัก)",
            "meaning": "ความรักสมหวัง การตัดสินใจครั้งสำคัญ พันธมิตรที่ดี ความสัมพันธ์ก้าวหน้า",
            "img": generate_tarot_card("THE LOVERS", "คนรัก", "💖", "VI"),
        },
        7: {
            "name": "The Sun (ดวงอาทิตย์)",
            "meaning": "ความสำเร็จสูงสุด ข่าวดี ชื่อเสียง ความสุขความสดใส ได้รับโชคลาภใหญ่",
            "img": generate_tarot_card("THE SUN", "ดวงอาทิตย์", "☀️", "XIX"),
        },
        8: {
            "name": "Wheel of Fortune (กงล้อโชคชะตา)",
            "meaning": "โชคชะตาเปลี่ยนไปในทางที่ดี ได้รับโอกาสทอง โชคลาภฟลุ๊กๆ ไหลมา",
            "img": generate_tarot_card(
                "WHEEL OF FORTUNE", "กงล้อโชคชะตา", "☸️", "X"
            ),
        },
    }

    st.info(
        "💡 ตั้งจิตอธิษฐานนึกถึงเรื่องที่ต้องการถาม แล้วกดปุ่มสุ่มเปิดไพ่ยิปซี"
    )

    # ปุ่มสุ่มหลัก 3 ใบ
    if st.button("✨ กดเพื่อสุ่มเปิดไพ่ยิปซี (3 ใบ)"):
        with st.spinner("🔮 กำลังตั้งจิตอธิษฐานและสุ่มจับไพ่ยิปซี 3 ใบ..."):
            time.sleep(0.8)
            st.session_state["tarot_main_cards"] = random.sample(
                list(TAROT_CARDS.keys()), 3
            )
            if "tarot_extra_cards" in st.session_state:
                del st.session_state["tarot_extra_cards"]

    # แสดงผลไพ่หลัก 3 ใบเรียงแนวนอนแบบกะทัดรัดพอดีจอเดียว
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
            with cols[idx]:
                st.image(
                    card["img"],
                    caption=f"ใบที่ {idx+1}",
                    use_container_width=True,
                )
                st.markdown(
                    f'<div class="result-box-small"><b>{card["name"]}</b><br><span style="color:#3b0764;">{card["meaning"]}</span></div>',
                    unsafe_allow_html=True,
                )

        st.write("")

        # ปุ่มกดสุ่มเพิ่ม 2 ใบ
        if st.button("➕ กดสุ่มไพ่เพิ่ม (2 ใบ)"):
            with st.spinner("🔮 กำลังสุ่มจับไพ่ยิปซีเพิ่ม 2 ใบ..."):
                time.sleep(0.8)
                available_cards = [
                    c
                    for c in TAROT_CARDS.keys()
                    if c not in st.session_state["tarot_main_cards"]
                ]
                st.session_state["tarot_extra_cards"] = random.sample(
                    available_cards, 2
                )

    # แสดงผลไพ่เพิ่ม 2 ใบ
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
            with extra_cols[idx]:
                st.image(
                    card["img"],
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
    }

    for i in range(4, 50):
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
            time.sleep(1)
            num = random.randint(1, 49)
            st.session_state["siamsi_result"] = num

    if "siamsi_result" in st.session_state:
        result_num = st.session_state["siamsi_result"]
        card_info = SIAMSI_49[result_num]

        st.markdown("---")
        img_url = generate_tarot_card(
            f"SIAMSI NO. {result_num}",
            card_info["title"],
            "☯️",
            f"№ {result_num}",
            "#fae8ff",
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
            
