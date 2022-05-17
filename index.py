from flask import Flask, render_template, request, redirect, url_for, session, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
from dotenv import load_dotenv
import os
import pickle
from utils.utility import strand_map, table_map
from random_forest_main.category import WeightFactorAlgorithm

load_dotenv()

app = Flask(__name__)
app.secret_key = "yey"

# DB Connection
# Enter your database connection details below

app.config['MYSQL_HOST'] = 'us-cdbr-east-05.cleardb.net'
app.config['MYSQL_USER'] = 'b1156bf8bbcd21'
app.config['MYSQL_PASSWORD'] = '7fb49349'
app.config['MYSQL_DB'] = 'heroku_3e72b37b0c5d4db'

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'aery'


# Intialize MySQL
mysql = MySQL(app)

FILE_NAME = 'random_forest_main/random_forest_model.sav'
sc = pickle.load(open('random_forest_main/scaler.pkl', 'rb'))
loaded_model = pickle.load(open(FILE_NAME, 'rb'))


# Load Records from database
@app.route('/aery/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        # Create variables for easy access
        email = request.form['email']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = %s AND password = %s', (email, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            session["dataX"] = []
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or email/password incorrect
            msg = 'Incorrect email/password!'
    # Show the login form with message (if any)
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['email'])
    # User is not loggedin redirect to login page
    return render_template('login.html', msg=msg)


@app.route('/aery/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('email', None)
    # Redirect to login page
    return redirect(url_for('login'))


@app.route('/aery/register', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
            return redirect(url_for('login'))


    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)


@app.route('/aery/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/')
def index():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/create')
def create():
    return render_template('register.html')


@app.route('/stem')
def stem():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('stem-page.html', username=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/abm')
def abm():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('abm-page.html', username=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/humss')
def humss():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('humms-page.html', username=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/gas')
def gas():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('gas-page.html', username=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/test')
def test():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('test.html', username=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/test2')
def test2():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('test2.html', username=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/test3')
def test3():
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('test3.html', username=session['email'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))


@app.route('/slearning', methods=['GET', 'POST'])
def save_learning():
    if 'loggedin' in session:
        if request.method == 'POST':
            check_naturalist = round(len(request.form.getlist("check_naturalist")) / 8 * 100, 2)
            check_intrapersonal = round(len(request.form.getlist("check_intrapersonal")) / 8 * 100, 2)
            check_interpersonal = round(len(request.form.getlist("check_interpersonal")) / 8 * 100, 2)
            check_musical = round(len(request.form.getlist("check_musical")) / 8 * 100, 2)
            check_bodily = round(len(request.form.getlist("check_bodily")) / 8 * 100, 2)
            check_spatial = round(len(request.form.getlist("check_spatial")) / 8 * 100, 2)
            check_logical = round(len(request.form.getlist("check_logical")) / 8 * 100, 2)
            check_linguistic = round(len(request.form.getlist("check_linguistic")) / 8 * 100, 2)

            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO learning_style VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                session['id'], check_linguistic, check_logical, check_spatial, check_bodily,
                check_musical, check_interpersonal, check_intrapersonal, check_naturalist))
            mysql.connection.commit()

        return redirect(url_for("profile"))

    return redirect(url_for('login'))


@app.route('/sinterest', methods=['GET', 'POST'])
def save_interest():
    if 'loggedin' in session:
        check_realistic = round(len(request.form.getlist("check_realistic")) / 7 * 100, 2)
        check_investigate = round(len(request.form.getlist("check_investigate")) / 7 * 100, 2)
        check_artistic = round(len(request.form.getlist("check_artistic")) / 7 * 100, 2)
        check_social = round(len(request.form.getlist("check_social")) / 7 * 100, 2)
        check_enterprising = round(len(request.form.getlist("check_enterprising")) / 7 * 100, 2)
        check_conventional = round(len(request.form.getlist("check_conventional")) / 7 * 100, 2)

        if request.method == 'POST':
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO interest VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)', (
                session['id'], check_realistic, check_investigate, check_artistic, check_social, check_enterprising,
                check_conventional))
            mysql.connection.commit()

        return redirect(url_for('profile'))
    return redirect(url_for('login'))


@app.route('/sacademic', methods=['GET', 'POST'])
def save_academic():
    if 'loggedin' in session:
        if request.method == 'POST' and "mathematics" in request.form and "science" in request.form and "english" in request.form and "social_science" in request.form:
            mathematics = request.form.get("mathematics")
            science = request.form.get("science")
            english = request.form.get("english")
            social_science = request.form.get("social_science")
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('INSERT INTO academic VALUES (NULL, %s, %s, %s, %s, %s)', (
                session['id'], mathematics, science, social_science, english))
            mysql.connection.commit()

        return redirect(url_for("profile"))
    return redirect(url_for('login'))


@app.route('/profile')
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            f'SELECT * FROM learning_style WHERE user_id={session["id"]} ORDER BY id DESC LIMIT 1')
        learning_style = cursor.fetchone()
        cursor.execute(f'SELECT * FROM academic WHERE user_id={session["id"]} ORDER BY id DESC LIMIT 1')
        academic = cursor.fetchone()
        cursor.execute(f'SELECT * FROM interest WHERE user_id={session["id"]} ORDER BY id DESC LIMIT 1')
        interest = cursor.fetchone()
        cursor.execute(f'SELECT * FROM result WHERE user_id={session["id"]} ORDER BY id DESC LIMIT 1')
        result = cursor.fetchone()
        mysql.connection.commit()

        results = None
        finalresult = None
        
        if result:
            results = [("stem", round(result["stem"] * 100, 2)), ("humss", round(result["humss"] * 100, 2)), ("abm", round(result["abm"] * 100, 2)),
                       ("gas", round(result["gas"] * 100, 2))]

            results.sort(key=lambda x: -x[1])

            print("1",result["weight"])
            print("2",results[0][0].upper())

            resultrandomforest = results[0][0].upper()
            if result["weight"] != resultrandomforest:
                finalresult = result["weight"]
            else:
                finalresult = results[0][0]

        return render_template('profile.html',
                               username=session['email'],
                               results=finalresult,
                               learning_style=learning_style,
                               academic=academic, interest=interest
                               )
    return redirect(url_for('login'))
    

@app.route('/generate')
def generate():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            f'SELECT * FROM learning_style WHERE user_id={session["id"]} ORDER BY id DESC LIMIT 1')
        learning_style = cursor.fetchone()
        cursor.execute(f'SELECT * FROM academic WHERE user_id={session["id"]} ORDER BY id DESC LIMIT 1')
        academic = cursor.fetchone()
        cursor.execute(f'SELECT * FROM interest WHERE user_id={session["id"]} ORDER BY id DESC LIMIT 1')
        interest = cursor.fetchone()

        if not (learning_style and academic and interest):
            return render_template('profile.html', username=session['email'], result=None,
                                   learning_style=learning_style,
                                   academic=academic, interest=interest)

        x = [interest["result_realistic"], interest["result_investigate"], interest["result_artistic"],
             interest["result_social"], interest["result_enterprising"],
             interest["result_conventional"], learning_style["result_linguistic"], learning_style["result_logical"],
             learning_style["result_spatial"],
             learning_style["result_bodily"], learning_style["result_musical"], learning_style["result_interpersonal"],
             learning_style["result_intrapersonal"], learning_style["result_naturalist"], academic["result_math"],
             academic["result_english"],
             academic["result_science"], academic["result_social_science"]]

        stem, humss, abm, gas = predict_probabilities([x])[0]
        weight = getRecommendedTrack(x)
        cursor.execute('INSERT INTO result VALUES (NULL, %s, %s, %s, %s, %s, %s)', (session['id'], stem, humss, abm, gas, weight))
        mysql.connection.commit()

        return redirect(url_for('profile'))

    return redirect(url_for('login'))


def predict_probabilities(data_from_user):
    x_input = sc.transform(data_from_user)
    probabilities = loaded_model.predict_proba(x_input)
    return probabilities
  
def getRecommendedTrack(data):
    weightFactor = WeightFactorAlgorithm(data)
    
    return weightFactor


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  
    