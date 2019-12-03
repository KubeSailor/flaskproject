from flask import Flask , render_template , request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.load(open('db.yml'))
app.config['MYSQL_HOST'] =db[ 'mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

@app.route('/' , methods=['GET,'POST'])
def index():
   if request.method = 'POST':
      userDetails = request.form
      name = userDetails['name']
      email=userDetails['email']
      
      cur = mysql.connection.cursor()
      cur.execute("INSERT INTO users(name , email) VALUES (%s,%s)",(name,email))
      mysql.connection.commit()
      cur.close()
      return redirect('/users')
   retrun render_template('index.html')
   
   if name == ' main ':
      app.run(debug=True)



