from flask import Flask, render_template, session, url_for, redirect, request
import sqlite3
conn = sqlite3.connect('database.db')
print ("Opened database successfully")
conn.execute('CREATE TABLE IF NOT EXISTS goorm (name TEXT, url TEXT)')
print ("Table created successfully")
con = sqlite3.connect("database.db")
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute("select * from goorm")
rows = cur.fetchall()
print("DB:")
print(rows)
app = Flask(__name__)
app.secret_key = 'this is super key'
app.config['SESSION_TYPE'] = 'filesystem'
userinfo = {'fu': 'fu'}


@app.route("/")
def homepage():
    if session.get('logged_in') :
        return render_template('loggedin.html', rows = rows)
    else:
        return render_template('index.html', rows = rows)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        try:
            if name in userinfo:
                if userinfo[name] == password:
                    session['logged_in'] = True
                    return redirect(url_for('homepage'))
                else:
                    return 'Wrong Password!'
            return 'ID does not exist'
        except:
            return 'Don\'t login'
    else:
        return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        userinfo[request.form['username']] = request.form['password']
        return redirect(url_for('login'))
    else:
        return render_template('register.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('index.html')

@app.route('/board')
def loggedin_board():
    return render_template('board.html', rows = rows) 

@app.route('/add', methods = ['POST'])
def add():
    if request.method == 'POST':
        try:
            name = request.form['name']
            url = request.form['url']
            

            with sqlite3.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO goorm (name, url) VALUES (?, ?)", (name, url))
                con.commit()
            
        finally:
            return render_template("board.html", rows = rows)
            
