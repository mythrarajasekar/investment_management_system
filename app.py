from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'sri'

# MySQL Database Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@Abi2005'  # Your MySQL password here
app.config['MYSQL_DB'] = 'db3'  # Your database name here
mysql = MySQL(app)

# Route to render the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to display all investments
@app.route('/investments')
def investments():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM investments")  # Query to fetch investment data
    investment_info = cur.fetchall()
    cur.close()
    return render_template('homepage.html', investments=investment_info)  # Render investments info

# Route to search investments by ID
@app.route('/search', methods=['POST', 'GET'])
def search():
    search_results = []
    search_term = ''
    if request.method == "POST":
        search_term = request.form['investment_id']
        cur = mysql.connection.cursor()
        query = "SELECT * FROM investments WHERE investment_id LIKE %s"
        cur.execute(query, ('%' + search_term + '%',))
        search_results = cur.fetchmany(size=1)
        cur.close()
        return render_template('homepage.html', investments=search_results)

# Route to insert a new investment
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == "POST":
        investment_id = request.form['investment_id']
        investment_type = request.form['investment_type']
        amount = request.form['amount']
        investor_name = request.form['investor_name']
        interest_rate = request.form['interest_rate']
        duration = request.form['duration']
        start_date = request.form['start_date']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO investments (investment_id, investment_type, amount, investor_name, interest_rate, duration, start_date) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                    (investment_id, investment_type, amount, investor_name, interest_rate, duration, start_date))
        mysql.connection.commit()
        return redirect(url_for('investments'))

# Route to delete an investment
@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM investments WHERE investment_id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('investments'))

# Route to edit investment details (Display the Edit Form)
@app.route('/edit/<string:id_data>', methods=['GET'])
def edit(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM investments WHERE investment_id=%s", (id_data,))
    investment = cur.fetchone()  # Fetch the investment details to edit
    cur.close()
    return render_template('edit_investment.html', investment=investment)

# Route to handle the update of investment details
@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        investment_id = request.form['investment_id']
        investment_type = request.form['investment_type']
        amount = request.form['amount']
        investor_name = request.form['investor_name']
        interest_rate = request.form['interest_rate']
        duration = request.form['duration']
        start_date = request.form['start_date']
        
        cur = mysql.connection.cursor()
        cur.execute("UPDATE investments SET investment_type=%s, amount=%s, investor_name=%s, interest_rate=%s, duration=%s, start_date=%s WHERE investment_id=%s", 
                    (investment_type, amount, investor_name, interest_rate, duration, start_date, investment_id))
        mysql.connection.commit()
        return redirect(url_for('investments'))  # Redirect back to the investment list page

if __name__ == "__main__":
    app.run(debug=True)
