from flask import Flask
from flask.templating import render_template
from flask.globals import request
from flask.json import jsonify
app = Flask(__name__, static_url_path='',
            static_folder='./static/')
@app.route('/')
def home():
    
    return render_template('myflask06.html')

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data)

    return jsonify(result = "success", result2= data)

if __name__ == '__main__':
    app.run(debug=True)