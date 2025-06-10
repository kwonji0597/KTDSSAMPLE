# 필요한 라이브러리 설치 (처음 1번만 하면 됨)
# !pip install python-dotenv

# 디버거 : F5번으로 확인 - Python Debugger
import openai

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


question = input("질문을 입력하세요: ")

response = openai.chat.completions.create(
    # model = "gpt-3.5-turbo"
    model = "dev-gpt-4o-mini",  # 배포한 배포명 입력
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": question},
    ]
)

print(response.choices[0].message.content)

# 디버거 : F5번으로 확인 - python Debugger