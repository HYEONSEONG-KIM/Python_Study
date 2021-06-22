from flask import Flask
from flask.templating import render_template
from flask.globals import request
from flask.json import jsonify
import pymysql
app = Flask(__name__, static_url_path='',
            static_folder='./static/')
@app.route('/')
def home():
    value = []
    db = pymysql.connect(host = 'localhost', user = 'root', password='python', database='pydb', port=3307)

    cursor = db.cursor()
    
    query = "SELECT col01,col02,col03 FROM sample"
    cursor.execute(query)
    data = cursor.fetchall()
    
    for i in data :
        obj = {'col01' : i[0], 'col02' : i[1], 'col03' : i[2]}
        value.append(obj)
            
    print(value)
    db.commit()
    db.close()
    cursor.close()
    
    return render_template('mycrud01.html', value=value)

@app.route('/ajax', methods=['POST'])
def ajax():
    data = request.get_json()
    print(data)

    return jsonify(result = "success", result2= data)

if __name__ == '__main__':
    app.run(debug=True)