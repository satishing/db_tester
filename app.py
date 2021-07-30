import os
from flask import Flask, render_template
from flask_mysql_connector import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_PORT'] = os.getenv('MYSQL_PORT')
app.config['MYSQL_DATABASE'] = os.getenv('MYSQL_DATABASE')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')

mysql = MySQL(app)
TEST_QUERY = 'select * from sys.user_summary'


@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    status = 'Unknown'
    try:
        conn = mysql.connection
        cur = conn.cursor()
        cur.execute(TEST_QUERY)
        output = cur.fetchall()
        status = 'Success'
    except Exception as e:
        status = 'Failed'

    return render_template('index.html', title='Welcome!', status=status, config=app.config)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
