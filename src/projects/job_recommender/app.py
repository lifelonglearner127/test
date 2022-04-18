from flask import Flask
from src.libs import run

app = Flask(__name__)


@app.route('/')
def hello():
    return run()
