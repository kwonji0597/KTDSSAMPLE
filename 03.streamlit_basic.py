# F5로 실행안됨
# 실행방법 : streamlit run .\03.streamlif_basic.py

# MVP결과물 streamlit으로 만들어도 됨

import streamlit as st

st.title("hello world!!")   # 웹페이지 완성

st.title('스마일 :sunglasses:') # 상단에 메뉴 생성 - Always Rerun 버튼 누르면 소스저장만 하면 자동 반영됨

st.header("헤더")

st.subheader("서브헤더")

st.text("텍스트")

name = st.text_input("이름 입력하세요", "기본값")
if name:
    st.write(name + "님 안녕하세요")

age = st.number_input("나이를 입력하세요", 0, 120, 20)
if age<19:
    st.write("미성년자 입니다")
else:
    st.write("성인입니다")