from flask import Flask, request, jsonify

app = Flask(__name__)

# 피크민 데이터베이스 (사진 주소와 설명을 저장)
# 실제 피크민 이미지 URL이 있다면 여기에 교체해서 넣으시면 됩니다.
pikmin_db = {
    "빨강": {
        "title": "❤️ 빨강 피크민 (Red Pikmin)",
        "description": "불에 강하고 공격력이 아주 높아요!\n코가 뾰족한 게 특징이죠.",
        "image": "https://raw.githubusercontent.com/olivia-pikmin/pikmin-bot/main/images/red_pikmin.png" # 예시 이미지 주소
    },
    "바위": {
        "title": "💎 바위 피크민 (Rock Pikmin)",
        "description": "단단해서 밟혀도 끄떡없고,\n유리나 벽을 부수기에 딱이에요!",
        "image": "https://raw.githubusercontent.com/olivia-pikmin/pikmin-bot/main/images/rock_pikmin.png" # 예시 이미지 주소
    },
    "보라": {
        "title": "💜 보라 피크민 (Purple Pikmin)",
        "description": "일반 피크민 10마리의 힘을 가진 천하장사예요!\n아주 듬직하답니다.",
        "image": "https://raw.githubusercontent.com/olivia-pikmin/pikmin-bot/main/images/purple_pikmin.png" # 예시 이미지 주소
    },
    # 필요한 피크민을 더 추가할 수 있습니다.
}

@app.route('/keyboard', methods=['POST'])
def keyboard():
    data = request.get_json()
    user_message = data['userRequest']['utterance'].replace(" ", "") # 공백 제거

    # 사용자가 입력한 단어에 피크민 이름이 포함되어 있는지 확인
    found_pikmin = None
    for name in pikmin_db:
        if name in user_message:
            found_pikmin = pikmin_db[name]
            break

    # 응답 바디 초기화
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": []
        }
    }

    if found_pikmin:
        # 1. 피크민을 찾았을 때: 사진 카드로 응답 (BasicCard)
        response_body["template"]["outputs"].append({
            "basicCard": {
                "title": found_pikmin["title"],
                "description": found_pikmin["description"],
                "thumbnail": {
                    "imageUrl": found_pikmin["image"]
                },
                "buttons": [
                    {
                        "action": "message",
                        "label": "다른 피크민 보기",
                        "messageText": "피크민 종류 알려줘"
                    }
                ]
            }
        })
    else:
        # 2. 피크민을 못 찾았을 때: 텍스트로 안내
        response_body["template"]["outputs"].append({
            "simpleText": {
                "text": f"'{user_message}'라는 피크민은 아직 도감에 없어요! 😢\n'빨강', '바위', '보라' 피크민의 이름을 불러주세요."
            }
        })

    return jsonify(response_body)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
