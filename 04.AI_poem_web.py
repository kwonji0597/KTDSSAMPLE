
# 필요한 라이브러리 설치 (처음 1번만 하면 됨)
# !pip install python-dotenv

# 디버거 : F5번으로 확인 - python Debugger
# F5로 실행안됨
# 실행방법 : streamlit run .\04.AI_poem_web.py

# MVP결과물 streamlit으로 만들어도 됨

import openai
import streamlit as st # streamlit 추가(이 한줄로 streamlit쓸수있음)

# .env 파일 로드
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수에서 값 읽기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT")
AZURE_API_TYPE = os.getenv("AZURE_API_TYPE")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")

openai.api_key = OPENAI_API_KEY
openai.azure_endpoint = AZURE_ENDPOINT
openai.api_type = AZURE_API_TYPE
openai.api_version = AZURE_API_VERSION

# streamlit text input 스타일
# title = st.text_input("Movie title", "Life of Brian")
# st.write("The current movie title is", title)

name = st.text_input("작가의 이름을 입력하세요: ")
subject = st.text_input("시의 주제를 입력하세요:")
content = st.text_input("시의 내용을 입력하세요: ")

button_click = st.button("시 생성하기")

if button_click: # 버튼 클릭했다면
    response = openai.chat.completions.create(
        # model = "gpt-3.5-turbo"
        model = "dev-gpt-4o-mini",  # 배포한 배포명 입력
        temperature=0.9, # 0으로 가면 T에 가깝고, 1로 가면 F에 가깝다.. 회사같은경우 0.3정도..
        messages=[
            {"role": "system", "content": "You are a AI Poem assistant"},
            {"role": "system", "content": f"Please write a poem name of {name} about {subject}. The content should include : {content}."},  # 변수앞에 f써서 바로 변수 처리 된거임
            {"role": "system", "content": "Please write the poem in Korea."},
            # {"role": "user", "content": name},
        ],
    )

    # print(response.choices[0].message.content)
    st.write(response.choices[0].message.content)


    #  Hello Mart에서 고객응대하는 챗봇 만들기- 추후 과제