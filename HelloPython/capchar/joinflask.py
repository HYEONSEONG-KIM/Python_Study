
from flask import Flask
from flask.templating import render_template
from flask.globals import request
from flask.json import jsonify
from capchar.getKey import getKeys
from capchar.getImage import getImages
from capchar.check import checkImg

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('join.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    
    id = "8QmjmYiEJMrhyGHrDvCI"
    secret = "J5dy8izeWq"
    key = getKeys(id,secret)
    keys = key[8:-2]
    print(keys)
    
    imageName = getImages(id,secret, keys)
    

    return jsonify(result = "success", key = keys, img = imageName)

@app.route('/check.ajax', methods=['POST'])
def check_ajax():
    
    data = request.get_json()
    id = "8QmjmYiEJMrhyGHrDvCI"
    secret = "J5dy8izeWq"
    key = data['key']
    input = data['input']
    print(key)
    print(input)
    result = checkImg(id,secret,key,input)
    resultNum = result.find('true')
    
    
    
    if resultNum == -1 :
        result = "실패" 
    else :
        result = "성공"

    return jsonify(result = result)

if __name__ == '__main__':
    app.run(debug=True)
    
