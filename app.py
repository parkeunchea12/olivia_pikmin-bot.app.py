from flask import Flask, request, jsonify

app = Flask(__name__)

# 피크민 데이터베이스
pikmin_db = {
    "빨강": {
        "title": "❤️ 빨강 피크민",
        "description": "불에 강하고 공격력이 높아요!",
        "image": "https://raw.githubusercontent.com/parkeunchea12/olivia_pikmin-bot.app.py/main/red.png" 
    },
    "바위": {
        "title": "💎 바위 피크민",
        "description": "단단해서 뭐든 부술 수 있어요!",
        "image": "https://raw.githubusercontent.com/parkeunchea12/olivia_pikmin-bot.app.py/main/rock.png"
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
                "description": "궁금한 피크민의 이름을 입력해보세요.\n(예: 빨강 피크민, 바위 피크민)",
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
                "simpleText": {"text": "아직 그 피크민은 공부 중이에요! '빨강'이나 '바위'를 입력해보세요."}
            })

    return jsonify(response_body)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
