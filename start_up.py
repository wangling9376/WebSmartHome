from flask import Flask
from flask import request
from flask import render_template
import json
import time
import os
import sys
import traceback

app = Flask(__name__, template_folder="WebConent", static_folder='WebConent')

@app.route('/',methods=['GET'])
def hello_world():
    try:
        return render_template("/html/login.html", login_background_img="/imge/login_background_img.png")
    except Exception, e:
        print 'str(Exception):\t', str(Exception)
        print 'str(e):\t\t', str(e)
        print 'repr(e):\t', repr(e)
        print 'e.message:\t', e.message
        print 'traceback.print_exc():'; traceback.print_exc()
        print 'traceback.format_exc():\n%s' % traceback.format_exc()
        return "error"

@app.route('/plus',methods=['POST'])
def plus():
    return "  File "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
    #app.run()

