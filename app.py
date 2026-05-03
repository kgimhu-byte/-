import streamlit as st
import random

st.title("🍱 점심 메뉴 추천기")

korean = ["비빔밥", "김치찌개", "불고기", "된장찌개"]
japanese = ["초밥", "라멘", "돈카츠", "우동"]
chinese = ["짜장면", "짬뽕", "탕수육", "마파두부"]

side_menu = ["군만두", "샐러드", "계란찜", "감자튀김"]
drinks = ["콜라", "사이다", "아이스티", "물"]

food_type = st.selectbox("음식 종류 선택", ["한식", "일식", "중식", "랜덤"])
spicy = st.slider("매운 정도 🌶️", 0, 5)

if st.button("추천 받기"):
    if food_type == "한식":
        main = random.choice(korean)
    elif food_type == "일식":
        main = random.choice(japanese)
    elif food_type == "중식":
        main = random.choice(chinese)
    else:
        main = random.choice(korean + japanese + chinese)

    side = random.choice(side_menu)
    drink = random.choice(drinks)

    st.subheader("🍽️ 오늘의 점심 추천")
    st.write(f"메인 메뉴: {main}")
    st.write(f"사이드: {side}")
    st.write(f"음료: {drink}")
