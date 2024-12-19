from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def get_medicines():
    connection = sqlite3.connect("medicines.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM medicines')
    medicines = cursor.fetchall()
    connection.close()
    return medicines

@app.route('/')
def index():
    medicines = get_medicines()
    return render_template('index.html', medicines=medicines)

if __name__ == '__main__':
    app.run(debug=True)