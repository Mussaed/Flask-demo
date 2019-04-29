from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_mysqldb import MySQL

app = Flask('__name__')

app.config['MYSQL_HOST'] = 'sql9.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql9289830'
app.config['MYSQL_PASSWORD'] = 'gHD12Jxyj3'
app.config['MYSQL_DB'] = 'sql9289830'
mysql = MySQL(app)


# @app.route('/')
# def home(): 
    # return('<h1> Hello guys </h1>')
	
# @app.route('/')
# def home():
    # var = 'hello_guys'
    # return render_template('index.html', var = var)

# @app.route('/demo')
# def r():
	# a = 'another page'
	# return render_template('another.html', a=a)
	
@app.route('/')
def home():
	cur = mysql.connection.cursor()
	cur.execute('''select id, data from example''')
	q = cur.fetchall()
	return render_template('db.html', q = q )
	
@app.route('/insert', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO info(name, email) VALUES(%s, %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('info.html')

@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM info")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('getinf.html',userDetails=userDetails)	

	
if __name__ == '__main__':
	app.run(debug=True)
		
