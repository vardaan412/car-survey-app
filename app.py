from flask import Flask, render_template, request, redirect
import mysql.connector
import config

app = Flask(__name__)

# Connect to MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=config.MYSQL_HOST,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        database=config.MYSQL_DB
    )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        fav_car = request.form['fav_car']
        own_car = request.form['own_car']

        db = get_db_connection()
        cursor = db.cursor()
        cursor.execute("INSERT INTO cars (name, fav_car, own_car) VALUES (%s, %s, %s)", (name, fav_car, own_car))
        db.commit()
        cursor.close()
        db.close()

        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

