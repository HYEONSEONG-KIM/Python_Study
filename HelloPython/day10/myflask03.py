from flask import Flask
from flask.globals import request
app = Flask(__name__)
@app.route('/',methods=['POST', 'GET'])
def home():
    dan = request.values.get('dan')
    
    result = dan + "단<br>"
    
    for i in range(1,10):
        result += dan+ " * " + str(i) + " = " + str(i*int(dan)) + "<br>"
    
    return result

if __name__ == '__main__':
    app.run(debug=True)