from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard', methods=['POST'])
def keyboard():
    data = request.get_json()
    user_message = data['userRequest']['utterance'].replace(" ", "") # 공백 제거해서 인식률 높이기
    
    # 기본 답변 설정 (피크민 이름을 안 불렀을 때)
    answer = f"'{user_message}'라고 하셨나요? 피크민 이름을 불러주면 제가 소개해드릴게요! (빨강, 바위, 보라 등)"

    # 캐릭터별 소개 데이터
    if "빨강" in user_message:
        answer = "❤️ 빨강 피크민: 불에 강하고 공격력이 아주 높아요! 코가 뾰족한 게 특징이죠."
    elif "바위" in user_message:
        answer = "💎 바위 피크민: 단단해서 밟혀도 끄떡없고, 유리나 벽을 부수기에 딱이에요!"
    elif "보라" in user_message:
        answer = "💜 보라 피크민: 일반 피크민 10마리의 힘을 가진 천하장사예요! 아주 듬직하답니다."
    elif "날개" in user_message:
        answer = "💖 날개 피크민: 하늘을 날아다니며 물건을 옮길 수 있는 귀여운 친구예요."
    elif "파랑" in user_message:
        answer = "💙 파랑 피크민: 입처럼 보이는 아가미로 물속에서도 숨을 쉴 수 있어요!"
    elif "노랑" in user_message:
        answer = "💛 노랑 피크민: 전기에 강하고 높이 던져질 수 있는 가벼운 친구랍니다."
    elif "하양" in user_message:
        answer = "🤍 하양 피크민: 작고 빠르며 독을 가지고 있어요! 빨간 눈이 매력적이죠."

    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }
    return jsonify(response_body)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
