from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET']) # home, should be mapped to the path '/'
def home():
    return "hello";

app.run();