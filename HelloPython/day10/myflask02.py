from flask import Flask
from flask.globals import request
app = Flask(__name__)
@app.route('/')
def home():
    dan = request.args.get('dan', "1")
    
    result = dan + "단<br>"
    
    for i in range(1,10):
        result += dan+ " * " + str(i) + " = " + str(i*int(dan)) + "<br>"
    
    return result

if __name__ == '__main__':
    app.run(debug=True)