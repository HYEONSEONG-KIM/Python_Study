from flask import Flask
from flask.templating import render_template
from flask.globals import request
from flask.json import jsonify
import pymysql
from day12.mydao_emp import DaoEmp

app = Flask(__name__, static_url_path='',
            static_folder='./static/')
@app.route('/')
def home():
    ds = DaoEmp()
    list = ds.selectList()
    
    return render_template('empcrud.html', list = list)

@app.route('/insert.ajax', methods=['POST'])
def insert_ajax():
    sample = request.get_json()
    id = sample['id']
    ko_name = sample['ko_name']
    en_name = sample['en_name']
    mobile = sample['mobile']
    address = sample['address']
    ds = DaoEmp()
    
    cnt = ds.insert(id, ko_name, en_name,mobile,address)
    result = "fail"
    if cnt == 1 :
        result = "success"
    return jsonify(result = result)


@app.route('/update.ajax', methods=['POST'])
def update_ajax():
    sample = request.get_json()
    id = sample['id']
    ko_name = sample['ko_name']
    en_name = sample['en_name']
    mobile = sample['mobile']
    address = sample['address']
    ds = DaoEmp()
    
    cnt = ds.update(id, ko_name, en_name,mobile,address)
    result = "fail"
    if cnt == 1 :
        result = "success"
    return jsonify(result = result)


@app.route('/delete.ajax', methods=['POST'])
def delete_ajax():
    sample = request.get_json()
    id = sample['id']
   
    ds = DaoEmp()
    
    cnt = ds.delete(id)
    result = "fail"
    if cnt == 1 :
        result = "success"
    return jsonify(result = result)

if __name__ == '__main__':
    app.run(debug=True)