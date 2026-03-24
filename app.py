from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard', methods=['POST'])
def keyboard():
    data = request.get_json()
    user_message = data['userRequest']['utterance']
    
    # 이 아래 'response_body' 부분이 꼭 다 들어가야 해요!
    response_body = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": f"피크민이 '{user_message}'라고 대답했어요! 🌱"
                    }
                }
            ]
        }
    }
    return jsonify(response_body)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
