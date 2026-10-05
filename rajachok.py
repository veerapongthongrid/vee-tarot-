import random
import time
import streamlit as st

# 1. ตั้งค่าหน้าเพจ Streamlit
st.set_page_config(
    page_title="ระบบดูดวงสายเทพเซียน & ไพ่ยิปซี",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded",
)

# 2. สร้างแถบเมนูด้านข้าง (Sidebar) ให้เลือกฟังค์ชัน
st.sidebar.title("🔮 เมนูเลือกบริการดูดวง")
menu = st.sidebar.radio(
    "เลือกประเภทการดูดวง:",
    ["🃏 เปิดไพ่ทำนายดวง (ระบบเดิม)", "☯️ เซียมซีเทพเซียนห้องสิน 49 ใบ (ระบบใหม่)"],
)

# ==========================================
# 🟢 ฟังก์ชันที่ 1: ระบบเปิดไพ่ยิปซีทำนายดวงเดิม
# ==========================================
if menu == "🃏 เปิดไพ่ทำนายดวง (ระบบเดิม)":
    # --------------------------------------------------
    # พี่หมอนำโค้ดเดิมทั้งหมดที่มีใน app.py มาใส่ไว้ตรงส่วนนี้ครับ
    # --------------------------------------------------
    st.title("🔮 เปิดไพ่ทำนายดวง โดยพี่หมอวี")
    st.write("ยินดีต้อนรับสู่ระบบเปิดไพ่ทำนายดวง...")
    # (วางโค้ดไพ่ยิปซีเดิมของพี่หมอต่อตรงนี้ได้เลยครับ)


# ==========================================
# 🟣 ฟังก์ชันที่ 2: ระบบเซียมซีเทพเซียนห้องสิน 49 ใบ
# ==========================================
elif menu == "☯️ เซียมซีเทพเซียนห้องสิน 49 ใบ (ระบบใหม่)":

    # ตกแต่ง CSS เฉพาะหน้าเซียมซี
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 50%, #fff0f5 100%);
            color: #3b0764;
        }
        .main-title {
            text-align: center;
            color: #6b21a8;
            font-size: 2.2rem;
            font-weight: bold;
            margin-bottom: 5px;
        }
        .sub-title {
            text-align: center;
            color: #9333ea;
            font-size: 1rem;
            margin-bottom: 25px;
        }
        .result-box {
            background-color: rgba(255, 255, 255, 0.9);
            border: 2px solid #facc15;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0px 8px 20px rgba(168, 85, 247, 0.18);
        }
        .pred-header {
            color: #7e22ce;
            font-weight: bold;
            margin-top: 12px;
            margin-bottom: 3px;
        }
        div.stButton > button {
            background: linear-gradient(90deg, #9333ea 0%, #c026d3 100%);
            color: white;
            font-size: 1.2rem;
            font-weight: bold;
            border-radius: 25px;
            border: 2px solid #fef08a;
            width: 100%;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )

    # ฐานข้อมูลเซียมซี 49 ใบ
    SIAMSI_49 = {
        1: {
            "title": "อากงเทพสามตาเอ้อหลางเสิน (ปราบมารประทานพร)",
            "summary": "ดวงตามหาเทพส่องสว่าง อุปสรรคพ่ายแพ้ภัย",
            "work_money": "การงานโดดเด่น มีสติปัญญาแก้ปัญหาได้ทุกรูปแบบ ผู้ใหญ่เมตตาเอ็นดูสนับสนุน การเงินคล่องตัวดี มีลาภจากการงานและการเสี่ยงโชค",
            "love": "คนโสดมีเกณฑ์พบคนดีที่ถูกใจ เป็นคู่แท้สนับสนุนกัน คนมีคู่ความสัมพันธ์แน่นแฟ้น เข้าใจกันลึกซึ้ง",
            "advice": "จงเชื่อมั่นในสติปัญญาและสัญชาตญาณของตัวเอง มารไม่มี บารมีไม่เกิด ความเพียรจะนำมาซึ่งความสำเร็จอันยิ่งใหญ่",
        },
        2: {
            "title": "นาจาเหยียบกงล้อเพลิง (ชัยชนะอันว่องไว)",
            "summary": "ความสำเร็จรวดเร็วปานกามนิต ชนะอุปสรรคเด็ดขาด",
            "work_money": "การงานก้าวหน้ารวดเร็ว มีโปรเจกต์ใหม่ๆ เข้ามาตลอด การตัดสินใจเด็ดขาดนำมาซึ่งผลงานดีเยี่ยม การเงินไหลเวียนคล่องตัว มีโชคลาภแบบไม่คาดฝัน",
            "love": "ความรักสดใส มีเสน่ห์แรง คนโสดมีคนเข้ามาจีบมากมาย คนมีคู่ความสัมพันธ์ราบรื่น มีเกณฑ์ได้เดินทางร่วมกัน",
            "advice": "อย่ากลัวการเปลี่ยนแปลง จงกล้าคิดกล้าทำ ความมุ่งมั่นเด็ดเดี่ยวจะนำพาท่านสู่ชัยชนะ",
        },
        3: {
            "title": "มหาเทพเจียงจื่อหยาบัญชาทัพ (ความสำเร็จแห่งปัญญา)",
            "summary": "สติปัญญาชนะงานใหญ่ ได้รับเกียรติยศชื่อเสียง",
            "work_money": "การงานก้าวหน้า ได้รับความไว้วางใจให้คุมงานใหญ่ มีวิสัยทัศน์กว้างไกลแก้ปัญหาได้ดี การเงินมั่นคงดี มีโอกาสได้รับเงินก้อนใหญ่จากการลงทุนหรือความสามารถ",
            "love": "คนโสดมีเกณฑ์พบคนมีความรู้ความสามารถ เป็นคู่คิดคู่ชีวิต คนมีคู่ความสัมพันธ์มั่นคง เข้าใจกันและสนับสนุนกัน",
            "advice": "จงใช้สติปัญญาและวิสัยทัศน์ในการดำเนินชีวิต ความเพียรพยายามจะนำมาซึ่งความสำเร็จที่ยั่งยืน",
        },
    }

    # เพิ่มใบอื่นๆ หรือใช้ใบที่ 1 สำรองไว้
    for i in range(4, 50):
        if i not in SIAMSI_49:
            SIAMSI_49[i] = SIAMSI_49[1]

    # หน้าตา UI เซียมซี
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
