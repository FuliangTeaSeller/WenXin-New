from flask import Flask, render_template, request, jsonify
from algorithmInterface import get_prompts
import random

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/question', methods=['POST'])
def handle_question():
    data = request.get_json()
    question = data['question']

    prompts=get_prompts(question)
    response = {
            'prompt': prompts
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)