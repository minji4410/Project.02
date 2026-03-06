import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="돌봄 건강 센터", page_icon="🦾", layout="centered")

# 2. 디자인 적용 (따옴표 위치를 정확히 맞춘 코드입니다)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;500;700&display=swap');

    /* 배경색과 폰트 설정 */
    .stApp { 
        background-color: #F0F4F8; 
        font-family: 'Noto Sans KR', sans-serif !important;
    }
    
    /* 상단 타이틀 디자인 */
    .mobile-title {
        font-size: 28px !important;
        color: #FFFFFF;
        font-weight: 800;
        text-align: center;
        padding: 30px 15px;
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        border-radius: 0px 0px 25px 25px;
        margin: -1rem -1rem 25px -1rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    /* 카드형 박스 */
    .m-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }

    /* 버튼 디자인 */
    .stButton>button {
        width: 100%;
        height: 60px;
        background: #10B981 !important;
        color: white !important;
        border-radius: 15px !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        border: none !important;
    }
    
    /* 영상 제목 */
    .video-label {
        font-size: 14px;
        font-weight: bold;
        color: #64748B;
        margin-bottom: 8px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)
    
# 2. 상단 헤더
st.markdown('<div class="mobile-title">🦾 돌봄 가족 건강 센터</div>', unsafe_allow_html=True)

# 3. 메인 메뉴 (모바일 터치가 쉬운 선택 박스)
menu = st.selectbox("🎯 메뉴를 선택해 주세요", 
                   ["📊 나의 통증 자가진단", "🛡️ 돌봄 부상 예방 수칙", "🧘 부위별 맞춤 영상"])

st.divider()

# --- 섹션 1: 자가진단 ---
if menu == "📊 나의 통증 자가진단":
    st.markdown("### 📊 현재 몸 상태 체크")
    st.markdown('<div class="m-card">어르신 혹은 환자를 돌보며 아픈 곳이 있다면 체크해 보세요.</div>', unsafe_allow_html=True)
    c1 = st.checkbox("허리를 숙이거나 물건을 들 때 아프다.")
    c2 = st.checkbox("어깨가 돌처럼 딱딱하고 무겁다.")
    c3 = st.checkbox("손가락 마디가 붓거나 손목이 시리다.")
    c4 = st.checkbox("다리에 쥐가 자주 나거나 발목이 아프다.")
    
    if st.button("진단 결과 보기"):
        score = c1 + c2 + c3 + c4
        if score >= 3: st.error("🚨 **위험:** 휴식이 시급합니다! 아래 영상을 보며 꼭 몸을 풀어주세요.")
        elif score >= 1: st.warning("⚠️ **주의:** 통증 초기 단계입니다. 매일 스트레칭을 실천하세요.")
        else: st.success("✅ **건강:** 아주 좋습니다! 예방 수칙을 계속 지켜주세요.")

# --- 섹션 2: 돌봄 수칙 ---
elif menu == "🛡️ 돌봄 부상 예방 수칙":
    st.markdown("### 🛡️ 현장 안전 수칙")
    st.markdown("""
    <div class="m-card"><b>1. 대상자와 밀착하기</b><br>몸을 가까이 붙여야 허리 부담이 줄어듭니다.</div>
    <div class="m-card" style="border-left-color: #3B82F6;"><b>2. 다리 힘 사용하기</b><br>허리만 숙이지 말고 무릎을 굽혀 일어나세요.</div>
    <div class="m-card" style="border-left-color: #F59E0B;"><b>3. 미리 소통하기</b><br>"움직이겠습니다"라고 말해 협조를 구하세요.</div>
    """, unsafe_allow_html=True)

# --- 섹션 3: 부위별 맞춤 영상 (영상 2개 배치) ---
elif menu == "🧘 부위별 맞춤 영상":
    st.markdown("### 🧘 부위별 영상 가이드")
    part = st.radio("아픈 부위를 눌러보세요", ["목/어깨", "허리", "손목", "다리/발목"], horizontal=True)
    
    st.markdown('<div class="m-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2) # 모바일에서도 나란히 2칸 배치
    
    if part == "목/어깨":
        with col1:
            st.markdown('<p class="video-label">📺 동작 1</p>', unsafe_allow_html=True)
            st.video("https://youtube.com/watch?v=InieLaiFSaI?si=sul1eYdzUfrAsOPP")
        st.info("💡 목,어깨가 뭉친것처럼 아플때 이 동작을 해보세요!")
        with col2:
            st.markdown('<p class="video-label">📺 동작 2</p>', unsafe_allow_html=True)
            st.video("https://youtube.com/watch?v=vU1UClVSjAg?si=Ig-TmUFgQR7CT326")
        st.info("💡 팁: 턱을 당기고 어깨를 뒤로 펴는 동작을 반복하세요.")
        
    elif part == "허리":
        with col1:
            st.markdown('<p class="video-label">📺 동작 1</p>', unsafe_allow_html=True)
            st.video("https://youtube.com/watch?v=33C8ujK5drw?si=9tRK2Cejb_Cmn-Hf")
        st.info("💡 팁: 앉아서 간단하게 허리통증 줄여주는 자세")
        with col2:
            st.markdown('<p class="video-label">📺 동작 2</p>', unsafe_allow_html=True)
            st.video("https://youtube.com/watch?v=MI8rN44Qd3k?si=qcIkx4rhn2fo5H7r") # 주소는 원하시는 대로 교체 가능
        st.info("💡 팁: 자기전 한번씩! 허리에 힘을 빼고 천천히 호흡하며 따라하세요.")
        
    elif part == "손목":
        with col1:
            st.markdown('<p class="video-label">📺 동작 1</p>', unsafe_allow_html=True)
            st.video("https://youtube.com/watch?v=waEegh-wIVU?si=LZ1qK83ZuCrnHjlK")
            
    elif part == "다리/발목":
        with col1:
            st.markdown('<p class="video-label">📺 동작 1</p>', unsafe_allow_html=True)
            st.video("https://youtube.com/watch?v=ABMsOq6Lm1U?si=dIIkaXM_eUOwaTK7")
        with col2:
            st.markdown('<p class="video-label">📺 동작 2</p>', unsafe_allow_html=True)
            st.video("https://youtube.com/watch?v=Df-cIVF6Lho?si=dFzda-l3Ax0wB8Is")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. 푸터
st.divider()

st.markdown("<p style='text-align: center; color: #64748B; font-size: 12px;'>제작: 우석대학교 물리치료학과 김민지<br>본 사이트는 학술 목적으로 제작되었습니다.</p>", unsafe_allow_html=True)



