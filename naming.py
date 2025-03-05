import streamlit as st
from deep_translator import GoogleTranslator
import re
import keyword


# 변수명 생성 함수
def generate_variable_name(korean_text, style="snake_case"):
    try:
        # 한글을 영어로 번역
        translated_text = GoogleTranslator(source="ko", target="en").translate(
            korean_text
        )
    except Exception as e:
        translated_text = "번역 실패: " + str(e)
        return translated_text

    # 번역된 영어를 스네이크 케이스로 변환
    translated_text = re.sub(r"[^\w\s]", "", translated_text)  # 특수문자 제거
    translated_text = translated_text.replace(
        " ", "_"
    ).lower()  # 스네이크 케이스로 변환

    return translated_text


# 예약어 감지 함수
def is_reserved_keyword(variable_name):
    return variable_name in keyword.kwlist


# Streamlit 페이지 설정
st.title("변수 이름 한/영 변환기 🤖")
st.divider()
st.write("한글 변수명을 영어로 바꿔드립니다.")
st.write("*예시) 사용자 이름  ->  user_name* / 첫 글자가 숫자라면 한글로 입력!")

# 사용자가 입력한 텍스트를 받기 위한 텍스트 박스
user_input = st.text_input("변수 이름을 한글로 입력하세요✏️")

# 변환 버튼 클릭 시 동작
if user_input:
    # 번역 및 변수명 생성
    result = generate_variable_name(user_input, style="snake_case")

    # 예약어 확인
    if is_reserved_keyword(result):
        st.write(f" 추천 변수명 : {result}_1")
    else:
        st.write(f"추천 변수명 : {result}")

# 수정
# 수정
