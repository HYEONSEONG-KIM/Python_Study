from flask import Flask, render_template
from flask.globals import request
from flask.json import jsonify
from capchar import getKey, getImage

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('join.html')

def ajax():
    id = "8QmjmYiEJMrhyGHrDvCI"
    secret = "J5dy8izeWq"
    key = getKey(id,secret)
    
    getImage(id,secret, key)
    
    
    data = request.get_json()
    print(data)

    return jsonify(result = "success", result2= data)

if __name__ == '__main__':
    app.run(debug=True)
    
