# 🚀 OpenAI Chat Completion Demo  
Azure OpenAI Service + Python + dotenv 사용 예제 프로젝트입니다.

본 프로젝트는 Azure OpenAI Service 기반의 Chat Completion 기능을 Python 코드로 구현한 예제입니다.  
환경변수(.env)를 활용하여 민감 정보를 안전하게 관리합니다.

---

## 📦 사용 기술

- Python 3.x
- Azure OpenAI Service
- python-dotenv (환경변수 관리)
- openai 라이브러리
- Visual Studio Code + GitHub 연동

---

## 📁 프로젝트 구조

```
KTDSSAMPLE/
├── .gitignore
├── .env.example
├── README.md
├── 01.simple_chatbot.py
├── 02.AI_poem.py
├── 03.streamlit_basic.py
├── 04.AI_poem_web.py
├── requirements.txt (선택)
└── 기타 소스코드 파일들
```

---

## 🚀 실행 방법

### 1️⃣ GitHub에서 프로젝트 클론

```bash
git clone https://github.com/kwonji0597/KTDSSAMPLE.git
cd KTDSSAMPLE
```

---

## 필수 패키지 설치

```bash
pip install -r requirements.txt
# 또는
pip install python-dotenv openai
```


---

## 환경변수 설정 (.env 파일 생성)

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
AZURE_ENDPOINT=https://jiyoungkwon-openai-001.openai.azure.com
AZURE_API_TYPE=azure
AZURE_API_VERSION=2023-05-15
```

주의: .env 파일은 절대 GitHub에 Push하지 않습니다!
(.gitignore 에 포함되어 있음)

---

## 실행

```bash
python 01.simple_chatbot.py
```
→ 실행 후 질문을 입력하세요: 프롬프트에 질문 입력 → GPT-4o 모델로 응답 출력.
