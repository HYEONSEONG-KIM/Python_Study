from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    mystr = "good morning"
    arr = ["홍길동", "전우치", "허균"]
    list = [
            {'s_name' : '삼성전자', 's_code' : '000001', 'price' : 80000},
            {'s_name' : 'LG', 's_code' : '000002', 'price' : 100000}
        ]
    return render_template('flask05.html', mystr = mystr, arr = arr, list = list)

if __name__ == '__main__':
    app.run(debug=True)
    
