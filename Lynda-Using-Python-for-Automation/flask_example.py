from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

def test():
    name = request.args.get("name", "Test")
    return f'Test, {escape(name)}!'
