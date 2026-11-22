import random
import streamlit as st

# 1. 화면 상단 제목 및 안내 문구
st.title("🎮 컴퓨터와 한판 승부! 가위바위보 게임")
st.write("아래 버튼 중 하나를 선택해 컴퓨터를 이겨보세요!")

st.divider()

# 2. [✌️ 가위], [✊ 바위], [✋ 보] 버튼 3개 나란히 배치
col1, col2, col3 = st.columns(3)

user_choice = None
with col1:
    if st.button("✌️ 가위", use_container_width=True):
        user_choice = "✌️ 가위"
with col2:
    if st.button("✊ 바위", use_container_width=True):
        user_choice = "✊ 바위"
with col3:
    if st.button("✋ 보", use_container_width=True):
        user_choice = "✋ 보"

# 3. 사용자가 버튼을 눌렀을 때 게임 진행
if user_choice:
    choices = ["✌️ 가위", "✊ 바위", "✋ 보"]
    computer_choice = random.choice(choices)

    st.divider()

    # 나와 컴퓨터의 선택 보여주기
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        st.subheader("나 (User)")
        st.markdown(f"## {user_choice}")
    with res_col2:
        st.subheader("컴퓨터 (AI)")
        st.markdown(f"## {computer_choice}")

    # 4. 승패 판정 및 결과 상자 출력
    if user_choice == computer_choice:
        st.warning("🤝 비겼습니다! 다시 한 번 도전해 보세요.")
    elif (
        (user_choice == "✌️ 가위" and computer_choice == "✋ 보")
        or (user_choice == "✊ 바위" and computer_choice == "✌️ 가위")
        or (user_choice == "✋ 보" and computer_choice == "✊ 바위")
    ):
        st.success("🎉 축하합니다! 당신이 이겼습니다!")
        st.balloons()  # 승리 시 풍선 축하 효과
    else:
        st.error("😭 아쉽네요, 컴퓨터가 이겼습니다...")
