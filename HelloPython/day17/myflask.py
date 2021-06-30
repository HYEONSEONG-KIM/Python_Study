from flask import Flask
from flask.templating import render_template
from flask.globals import request
from flask.json import jsonify
from day17 import mymudang
from day17.mymudang import getIJAjax
app = Flask(__name__, static_url_path='',
            static_folder='./static/')
@app.route('/')
def home():
    
    return render_template('omok03.html')


@app.route('/getIJAjax.ajax', methods=['POST'])
def omok_ajax():
    jsn = request.get_json()
    omokinfo = jsn['omokinfo']
    print(omokinfo)
    i,j = getIJAjax(omokinfo)
    # print(i,j)
    #
    print(i)
    print(j)
    result_i = str(i)
    result_j = str(j)
  
    return jsonify(result_i = result_i, result_j = result_j)


if __name__ == '__main__':
    app.run(debug=True,port=80)