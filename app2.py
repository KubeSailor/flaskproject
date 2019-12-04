from flask import Flask, request, render_template
import pymysql

db = pymysql.connect("localhost", "root", "root", "mysql")

app = Flask(__name__)
#api = Api(app)

@app.route('/')
def someName():
    cursor = db.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('sample.html', results=results)

if __name__ == '__main__':
        app.run(debug=True)
