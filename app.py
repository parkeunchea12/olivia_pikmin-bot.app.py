import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# 피크민 데이터베이스
pikmin_db = {
    "빨강": {
        "title": "❤️ 빨강 피크민",
        "description": "불에 강하고 공격력이 높아요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/red.jpeg?raw=true",
        "link": "https://search.naver.com/search.naver?query=빨강+피크민"
    },
    "노랑": {
        "title": "💛 노랑 피크민",
        "description": "전기에 강하고 아주 높이 던질 수 있어요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/yellow.jpeg?raw=true",
        "link": "https://search.naver.com/search.naver?query=노랑+피크민"
    },
    "파랑": {
        "title": "💙 파랑 피크민",
        "description": "물속에서도 숨을 쉬고 자유롭게 헤엄칠 수 있어요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/blue.jpeg?raw=true",
        "link": "https://search.naver.com/search.naver?query=파랑+피크민"
    },
    "보라": {
        "title": "💜 보라 피크민",
        "description": "몸무게가 10배 무겁고 공격력이 매우 강해요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/puple.jpeg?raw=true",
        "link": "https://search.naver.com/search.naver?query=보라+피크민"
    },
    "하양": {
        "title": "🤍 하양 피크민",
        "description": "독에 면역이며 발이 아주 빠르고, 먹힌 적에게 독 데미지를 줘요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/white.jpeg?raw=true",
        "link": "https://search.naver.com/search.naver?query=하양+피크민"
    },
    "바위": {
        "title": "💎 바위 피크민",
        "description": "단단해서 뭐든 부술 수 있고 밟혀도 죽지 않아요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/qkdnl.jpeg?raw=true",
        "link": "https://search.naver.com/search.naver?query=바위+피크민"
    },
    "날개": {
        "title": "🩷 날개 피크민",
        "description": "하늘을 훨훨 날아서 장애물 위로 물건을 옮길 수 있어요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/skfro.jpeg?raw=true",
        "link": "https://search.naver.com/search.naver?query=날개+피크민"
    },
    "얼음": {
        "title": "🩵 얼음 피크민",
        "description": "물이나 적을 꽁꽁 얼려버릴 수 있어요!",
        "image": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/ice.jpeg?raw=true",
        "link": "https://search.naver.com/search.naver?query=얼음+피크민"
    }
}

@app.route('/keyboard', methods=['POST'])
def keyboard():
    try: # 에러가 나도 봇이 멈추지 않도록 예외 처리 시작!
        data = request.get_json()
        user_message = data['userRequest']['utterance'].replace(" ", "")

        response_body = {
            "version": "2.0", 
            "template": {
                "outputs": [],
                "quickReplies": []
            }
        }

        # 퀴즈 모드인지 확인하기 위한 스위치 (기본은 꺼짐)
        is_quiz_mode = False 

        # --------------------------------------------------------
        # 1. 사용자의 메시지에 따른 응답(Outputs) 만들기
        # --------------------------------------------------------
        
        # 1-1. 웰컴 인사
        if user_message in ["시작", "안녕", "반가워", "누구니"]:
            response_body["template"]["outputs"].append({
                "basicCard": {
                    "title": "🌱 피크민 도감에 오신 걸 환영해요!",
                    "description": "궁금한 피크민을 입력하거나 아래 버튼을 눌러보세요.\n'도감'을 치면 전체를, '퀴즈'를 치면 게임을 할 수 있어요!",
                    "thumbnail": {
                        "imageUrl": "https://github.com/parkeunchea12/olivia_pikmin-bot.app.py/blob/main/ehrka.jpeg?raw=true"
                    }
                }
            })
            
        # 1-2. 🎲 랜덤 뽑기
        elif "랜덤" in user_message or "뽑기" in user_message:
            random_name = random.choice(list(pikmin_db.keys()))
            found = pikmin_db[random_name]
            
            response_body["template"]["outputs"].append({
                "basicCard": {
                    "title": f"🎉 오늘의 행운 픽: {found['title']}!",
                    "description": found["description"],
                    "thumbnail": {"imageUrl": found["image"]},
                    "buttons": [
                        {
                            "action": "webLink",
                            "label": "🔍 더 알아보기",
                            "webLinkUrl": found["link"]
                        }
                    ]
                }
            })

        # 1-3. 📖 전체 도감 보기 (케로셀 슬라이드)
        elif "전체" in user_message or "도감" in user_message or "목록" in user_message:
            carousel_items = []
            for name, info in pikmin_db.items():
                carousel_items.append({
                    "title": info["title"],
                    "description": info["description"],
                    "thumbnail": {"imageUrl": info["image"]},
                    "buttons": [
                        {
                            "action": "webLink",
                            "label": "🔍 더 알아보기",
                            "webLinkUrl": info["link"]
                        }
                    ]
                })
            
            response_body["template"]["outputs"].append({
                "carousel": {
                    "type": "basicCard",
                    "items": carousel_items
                }
            })

        # 1-4. 🎯 미니 퀴즈
        elif "퀴즈" in user_message or "문제" in user_message:
            is_quiz_mode = True # 퀴즈 모드 켜기!
            answer_name = random.choice(list(pikmin_db.keys()))
            answer_info = pikmin_db[answer_name]
            
            # 정답을 포함해 랜덤으로 보기 3개 만들기
            choices = random.sample(list(pikmin_db.keys()), 3)
            if answer_name not in choices:
                choices[0] = answer_name 
            random.shuffle(choices) 
            
            # 퀴즈 전용 하단 버튼 세팅 (3개만 나옴)
            for choice in choices:
                response_body["template"]["quickReplies"].append({
                    "messageText": choice,
                    "action": "message",
                    "label": f"🤔 {choice} 피크민!"
                })

            response_body["template"]["outputs"].append({
                "simpleText": {
                    "text": f"Q. 다음 특징을 가진 피크민은 누구일까요?\n\n💡 힌트: {answer_info['description']}\n\n(아래 버튼에서 정답을 골라보세요!)"
                }
            })

        # 1-5. 일반 피크민 검색 (예: "빨강", "파랑 피크민 어때" 등)
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
                        "thumbnail": {"imageUrl": found["image"]},
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "🔍 더 알아보기",
                                "webLinkUrl": found["link"]
                            }
                        ]
                    }
                })
            else:
                response_body["template"]["outputs"].append({
                    "simpleText": {"text": "아직 그 피크민은 공부 중이에요! 아래 버튼을 눌러 다른 기능을 이용해보세요."}
                })

        # --------------------------------------------------------
        # 2. 기본 하단 버튼(QuickReplies) 세팅 (퀴즈 모드가 아닐 때만)
        # --------------------------------------------------------
        if not is_quiz_mode:
            # 필수 기능 고정 버튼 3개
            response_body["template"]["quickReplies"].extend([
                {"messageText": "랜덤 뽑기", "action": "message", "label": "🎲 랜덤"},
                {"messageText": "전체 도감", "action": "message", "label": "📖 도감"},
                {"messageText": "피크민 퀴즈", "action": "message", "label": "🎯 퀴즈"}
            ])

            # 나머지 7개 자리에 랜덤 피크민 이름 채우기 (카카오톡 10개 제한 방어)
            pikmin_names = list(pikmin_db.keys())
            random.shuffle(pikmin_names)
            for name in pikmin_names[:7]: 
                response_body["template"]["quickReplies"].append({
                    "messageText": name,
                    "action": "message",
                    "label": name
                })

        return jsonify(response_body)

    # --------------------------------------------------------
    # 3. 에러 발생 시 예외 처리 (500 에러 방지)
    # --------------------------------------------------------
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            "version": "2.0",
            "template": {
                "outputs": [{"simpleText": {"text": "앗, 잠깐 서버에 쥐가 났어요! 다시 한 번 말씀해주시겠어요?"}}]
            }
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
