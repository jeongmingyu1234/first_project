import streamlit as st

st.title("369 게임")

if "count" not in st.session_state:
    st.session_state.count = 1
if "message" not in st.session_state:
    st.session_state.message = ""

def check_369(num):
    s = str(num)
    clap_count = sum(1 for c in s if c in ['3', '6', '9'])
    if clap_count == 0:
        return str(num)
    else:
        return "👏" * clap_count

def user_turn(user_input):
    try:
        num = int(user_input)
    except:
        st.session_state.message = "숫자만 입력해주세요!"
        return

    if num != st.session_state.count:
        st.session_state.message = f"숫자는 {st.session_state.count}부터 순서대로 말해야 합니다."
        return
    
    st.session_state.message = f"너: {check_369(num)}"
    st.session_state.count += 1

    # 컴퓨터 차례
    comp_response = check_369(st.session_state.count)
    st.session_state.message += f"\n컴퓨터: {comp_response}"
    st.session_state.count += 1

st.text(f"현재 숫자: {st.session_state.count}")

user_input = st.text_input("숫자 입력", key="input")

if st.button("제출"):
    if user_input.strip() != "":
        user_turn(user_input)
    else:
        st.session_state.message = "숫자를 입력해주세요!"

st.text_area("게임 진행", st.session_state.message, height=150)
