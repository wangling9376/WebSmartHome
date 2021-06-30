from flask import Flask
from flask import request
import json
import time

app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():
    return 'Hello. Under test   ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@app.route('/plus',methods=['POST'])
def plus():
    return "  File "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
    #app.run()

