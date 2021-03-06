from flask import Flask
from flask.templating import render_template
from flask.globals import request
from flask.json import jsonify
import pymysql
from day11.mydao_sample import DaoSample
app = Flask(__name__, static_url_path='',
            static_folder='./static/')
@app.route('/')
def home():
    ds = DaoSample()
    list = ds.selectList()
    
    return render_template('mycrud01.html', list = list)

@app.route('/insert.ajax', methods=['POST'])
def insert_ajax():
    sample = request.get_json()
    col01 = sample['col01']
    col02 = sample['col02']
    col03 = sample['col03']
    ds = DaoSample()
    
    cnt = ds.insert(col01, col02, col03)
    result = "fail"
    if cnt == 1 :
        result = "success"
    return jsonify(result = result)


@app.route('/update.ajax', methods=['POST'])
def update_ajax():
    sample = request.get_json()
    col01 = sample['col01']
    col02 = sample['col02']
    col03 = sample['col03']
    ds = DaoSample()
    
    cnt = ds.update(col01, col02, col03)
    result = "fail"
    if cnt == 1 :
        result = "success"
    return jsonify(result = result)


@app.route('/delete.ajax', methods=['POST'])
def delete_ajax():
    sample = request.get_json()
    col01 = sample['col01']
   
    ds = DaoSample()
    
    cnt = ds.delete(col01)
    result = "fail"
    if cnt == 1 :
        result = "success"
    return jsonify(result = result)

if __name__ == '__main__':
    app.run(debug=True)