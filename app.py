from flask import Flask, request, jsonify

app = Flask(__name__)

# 피크민 데이터베이스 (에러 수정 완료!)
pikmin_db = {
    "빨강": {
        "title": "❤️ 빨강 피크민",
        "description": "불에 강하고 공격력이 높아요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/red.jpeg?raw=true"
    }, # <-- 여기에 닫는 괄호와 쉼표가 빠져있어서 수정했습니다!
    "노랑": {
        "title": "💛 노랑 피크민",
        "description": "전기에 강하고 아주 높이 던질 수 있어요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/yellow.jpeg?raw=true" 
    },
    "파랑": {
        "title": "💙 파랑 피크민",
        "description": "물속에서도 숨을 쉬고 자유롭게 헤엄칠 수 있어요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/blue.jpeg?raw=true"
    },
    "보라": {
        "title": "💜 보라 피크민",
        "description": "몸무게가 10배 무겁고 공격력이 매우 강해요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/puple.jpeg?raw=true"
    },
    "하양": {
        "title": "🤍 하양 피크민",
        "description": "독에 면역이며 발이 아주 빠르고, 먹힌 적에게 독 데미지를 줘요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/white.jpeg?raw=true"
    },
    "바위": {
        "title": "💎 바위 피크민",
        "description": "단단해서 뭐든 부술 수 있고 밟혀도 죽지 않아요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/qkdnl.jpeg?raw=true"
    },
    "날개": {
        "title": "🩷 날개 피크민",
        "description": "하늘을 훨훨 날아서 장애물 위로 물건을 옮길 수 있어요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/skfro.jpeg?raw=true"
    },
    "얼음": {
        "title": "🩵 얼음 피크민",
        "description": "물이나 적을 꽁꽁 얼려버릴 수 있어요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/ice.jpeg?raw=true"
    }
}

@app.route('/keyboard', methods=['POST'])
def keyboard():
    data = request.get_json()
    user_message = data['userRequest']['utterance'].replace(" ", "")

    # 응답 기본 형태 만들기
    response_body = {
        "version": "2.0", 
        "template": {
            "outputs": [],
            "quickReplies": [] # 하단에 뜰 바로가기 버튼 자리
        }
    }

    # 🌟 바로가기 버튼(QuickReplies) 자동 생성 🌟
    # 데이터베이스에 있는 모든 피크민 이름으로 버튼을 만듭니다.
    for name in pikmin_db.keys():
        response_body["template"]["quickReplies"].append({
            "messageText": name,
            "action": "message",
            "label": name
        })

    # 웰컴 인사 (사용자가 처음 들어오거나 '안녕', '시작'이라고 할 때)
    if user_message in ["시작", "안녕", "반가워", "누구니"]:
        response_body["template"]["outputs"].append({
            "basicCard": {
                "title": "🌱 피크민 도감에 오신 걸 환영해요!",
                "description": "아래 버튼을 누르거나 궁금한 피크민을 입력해보세요.",
                "thumbnail": {
                    "imageUrl": "https://raw.githubusercontent.com/parkeunchea12/olivia_pikmin-bot.app.py/main/welcome.png"
                }
            }
        })
    # 피크민 찾기
    else:
        found = None
        for name in pikmin_db:
            if name in user_message:
                found = pikmin_db[name]
                break
        
        if found:
            response_body["template"]["outputs"].append({
                "basicCard": {
                    "title": found["title"],
                    "description": found["description"],
                    "thumbnail": {"imageUrl": found["image"]}
                }
            })
        else:
            response_body["template"]["outputs"].append({
                "simpleText": {"text": "아직 그 피크민은 공부 중이에요! 아래 버튼을 눌러 다른 피크민을 찾아보세요."}
            })

    return jsonify(response_body)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
