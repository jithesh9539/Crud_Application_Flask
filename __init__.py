from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
from flask_mysqldb import MySQL
from flask import session
from functools import wraps




app = Flask(__name__)
USERNAME = 'jithesh'
PASSWORD = 'jithesh123'

app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

def requires_authentication(view_func):
    @wraps(view_func)
    def decorated(*args, **kwargs):
        if not session.get('authenticated'):
            return redirect(url_for('login'))
        return view_func(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        auth = request.form.get('username'), request.form.get('password')
        if auth[0] == USERNAME and auth[1] == PASSWORD:
            session['authenticated'] = True
            return redirect(url_for('Index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')


@app.route('/index')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students")
    data = cur.fetchall()
    cur.close()




    return render_template('index2.html', students=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.pop('authenticated', None)
        flash('You have been logged out.', 'info')
        return redirect(url_for('login'))
    return render_template('logout.html')





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE students
               SET name=%s, email=%s, phone=%s
               WHERE id=%s
            """, (name, email, phone, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))









if __name__ == "__main__":
    app.run(debug=True)
