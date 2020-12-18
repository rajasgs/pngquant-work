from flask import Flask, request, jsonify, render_template
from json import dumps
import os

# Local import
import string_util as su


app = Flask(__name__)

'''
    http://localhost:8071/
'''
@app.route("/")
def main():

    result = {
        'result' : "1.7"
    }

    app.logger.info('Inside api')

    return render_template('main.html')


'''
    http://localhost:8071/api
'''
@app.route("/api")
def api():

    result = {
        'content' : 'sdf'
    }

    return jsonify(result) 

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=int(os.environ.get('CONTAINER_PORT')), debug=True)
