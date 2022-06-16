from flask import Flask,g, render_template,session,make_response,redirect,url_for, Response, stream_with_context, request
from flask_cors import CORS
import mysql.connector
from time import time
import json


app = Flask('__name__')
app.secret_key = 'iamgoodboi'
CORS(app)



class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

mydb = mysql.connector.connect(
	host = "remotemysql.com",
	user = "uJjQaBfJbk",
	password = "fVIWjMLvvE",
    database = "uJjQaBfJbk"
)
users = []
users.append(User(id=1, username='admin', password='12345678'))
users.append(User(id=2, username='openuser', password='govindisid'))

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user





@app.route('/')
def index():
    return '<h1>Go to login route (/login)</h1><br><a href="/login">Login</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)

        username = request.form['username']
        password = request.form['password']
        
        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if not g.user:
        return redirect(url_for('login'))

    
    return render_template('dashboard.html')

@app.route('/data', methods=["GET", "POST"])
def data():
    cursor = mydb.cursor(buffered=True)
    cursor.execute("SELECT * FROM testiot WHERE id = (SELECT MAX(id) FROM testiot);")
    records = cursor.fetchall()
    
    mydb.commit()

    data = records[0]

    humidity = data[1]
    temperature = data[2]
    uvindex = data[3]
    pressure = data[4]
    irdata = data[5]

    
    
    data = [time() * 1000, humidity, temperature,uvindex,pressure,irdata]

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

app.run(debug=False)
