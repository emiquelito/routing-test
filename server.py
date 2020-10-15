from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    SQUASH_CUSTOM_VAR1 = os.environ.get('SQUASH_CUSTOM_VAR1')
    return '<body>Hello world. <a href="/about">About this page</a> - Env Var: %s.</body>' % SQUASH_CUSTOM_VAR1

@app.route('/about')
def about():
    return '<body>This is the about page</body>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
