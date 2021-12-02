from flask import Flask, request
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

@app.route('/login', methods = ["get"])
def login():
  codef = request.args.get("code")
  return codef
  

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
