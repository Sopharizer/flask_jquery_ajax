import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    return json.dumps({"message" : "通信成功!!"})

if __name__ == '__main__':
    app.run()
