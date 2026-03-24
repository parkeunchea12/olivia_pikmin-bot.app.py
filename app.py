from flask import Flask, request, jsonify

app = Flask(__name__)

# 피크민 데이터베이스 (모든 피크민 추가 완료!)
pikmin_db = {
    "빨강": {
        "title": "❤️ 빨강 피크민",
        "description": "불에 강하고 공격력이 높아요!",
        "image": "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fi.namu.wiki%2Fi%2FndyKmzgEhIJHWB_b-vz3JECuRhWTlZkOC7OFsjVoiGr3IvncXJKf6a-V_NOB43CaOBD3a_Y08imSUrjteC1w4w.webp&type=a340" 
    },
    "노랑": {
        "title": "💛 노랑 피크민",
        "description": "전기에 강하고 아주 높이 던질 수 있어요!",
        "image": "https://via.placeholder.com/300x300.png?text=Yellow+Pikmin" 
    },
    "파랑": {
        "title": "💙 파랑 피크민",
        "description": "물속에서도 숨을 쉬고 자유롭게 헤엄칠 수 있어요!",
        "image": "https://via.placeholder.com/300x300.png?text=Blue+Pikmin"
    },
    "보라": {
        "title": "💜 보라 피크민",
        "description": "몸무게가 10배 무겁고 공격력이 매우 강해요!",
        "image": "https://via.placeholder.com/300x300.png?text=Purple+Pikmin"
    },
    "하양": {
        "title": "🤍 하양 피크민",
        "description": "독에 면역이며 발이 아주 빠르고, 먹힌 적에게 독 데미지를 줘요!",
        "image": "https://via.placeholder.com/300x300.png?text=White+Pikmin"
    },
    "바위": {
        "title": "💎 바위 피크민",
        "description": "단단해서 뭐든 부술 수 있고 밟혀도 죽지 않아요!",
        "image": "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTAzMDdfMjI3%2FMDAxNzQxMjczMjAyNTA1.sC-FYz_46GFf0O2oWvK6A31dxWMjzecwkNhIIra7k8og.2y9nmUqSjhFjrauyzpZKDfNTl5vfc9HCMTp_Xd1VGosg.JPEG%2FIMG_1455.jpg&type=a340"
    },
    "날개": {
        "title": "🩷 날개 피크민",
        "description": "하늘을 훨훨 날아서 장애물 위로 물건을 옮길 수 있어요!",
        "image": "https://via.placeholder.com/300x300.png?text=Winged+Pikmin"
    },
    "얼음": {
        "title": "🩵 얼음 피크민",
        "description": "물이나 적을 꽁꽁 얼려버릴 수 있어요!",
        "image": "https://via.placeholder.com/300x300.png?text=Ice+Pikmin"
    },
    "반짝": {
        "title": "💚 반짝 피크민",
        "description": "밤에만 나타나며 둥둥 떠다니고 여러 속성에 면역이에요!",
        "image": "https://via.placeholder.com/300x300.png?text=Glow+Pikmin"
    }
}

@app.route('/keyboard', methods=['POST'])
def keyboard():
    data = request.get_json()
    user_message = data['userRequest']['utterance'].replace(" ", "")

    response_body = {"version": "2.0", "template": {"outputs": []}}

    # 웰컴 인사 (사용자가 처음 들어오거나 '안녕', '시작'이라고 할 때)
    if user_message in ["시작", "안녕", "반가워", "누구니"]:
        response_body["template"]["outputs"].append({
            "basicCard": {
                "title": "🌱 피크민 도감에 오신 걸 환영해요!",
                "description": "궁금한 피크민의 이름을 입력해보세요.\n(예: 빨강 피크민, 얼음 피크민, 보라 피크민)",
                "thumbnail": {
                    "imageUrl": "https://raw.githubusercontent.com/parkeunchea12/olivia_pikmin-bot.app.py/main/welcome.png" # 환영 이미지
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
                "simpleText": {"text": "아직 그 피크민은 공부 중이에요! '빨강', '노랑', '파랑', '바위', '얼음' 등을 입력해보세요."}
            })

    return jsonify(response_body)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
