import sqlite3
from traceback import print_tb
from flask import Flask, render_template, request, flash, redirect, url_for, session, request, g
from flask_session import Session
from SQLi import detect_sql_injection
from AttackTest import attack_tester
import time

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

request_count = 0
last_reset = time.time()

def get_db_connection():
    conn = sqlite3.connect('database.db',  check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():    
    return render_template('index.html')
  
def my_route():
    client_ip = request.remote_addr
    print(f"Client IP: {client_ip}")

@app.route("/login", methods=["GET"])
def get_login():
    return render_template('login.html')

DDOS = True
@app.before_request
def limit_requests():
    global request_count, last_reset
    
    # Check if a minute has passed since the last reset
    current_time = time.time()
    print(current_time)
    if current_time - last_reset > 60:
        # Reset the request count
        request_count = 0
        last_reset = current_time
      
    
    # Check if request count has reached 60, if not, process the request
    if request_count >= 2:
        print("Too many requests. Try again later.")  # HTTP status code for "Too Many Requests"
        DDOS = False
    else:
        request_count += 1

@app.route("/login", methods=["POST"])
def post_login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if len(username) > 0:
        if(attack_tester(username)):
            print("Hello")
        else:
            conn = get_db_connection()
            user = conn.execute(f'SELECT * FROM users where username = "{username}"').fetchall()
            conn.close()
            
            if len(user) > 0:
                if len(password) > 0:
                    conn = get_db_connection()
                    query = f'SELECT username FROM users where username = "{username}" and  password = "{password}"'
                    print(query)
                    validation = conn.execute(query).fetchone()
                    conn.close()
                    print(validation[0])
                    if len(validation) > 0:
                        session["name"] = request.form.get("username")
                        return redirect("/home")
                    else:
                        flash("Wrong password", "error")
                else:
                    flash("Enter password", "error")
            else:
                flash("Wrong username", "error")
    else:
        flash("Enter username", "error")
    return render_template("login.html")

@app.route("/home")
def home():
    print(session.get("name"))
    if not session.get("name"):
        return redirect("/")
    conn = get_db_connection()
    attacks = conn.execute(f'SELECT * FROM attacks;').fetchall()
    conn.close()
    return render_template("home.html", username=session.get("name"), attacks=attacks)



@app.route('/home')
def display_attack_info():
    # Get attack information
    attack_data = get_attack_info()
    
    # Pass the data to the HTML template
    return render_template('attacks.html', attack_data=attack_data)




@app.route("/logout")
def logout():
    session["name"] = None 
    return redirect("/")

if __name__=="__main__":
   
    app.run(debug=True, host = 'localhost')