from flask import Flask, request, jsonify
from wheatley import talk_to_wheatley
from glados import talk_to_glados

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    char = data.get("character", "wheatley").lower()
    msg = data.get("message")
    
    if char == "glados":
        response = talk_to_glados(msg)
    else:
        response = talk_to_wheatley(msg)
        
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(port=8000)
