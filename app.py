from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    response = bot.get_response(message)
    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)
