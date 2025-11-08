import os
from flask import Flask, render_template, request, redirect, url_for, flash, abort
from dotenv import load_dotenv
from flask_mysqldb import MySQL
from MySQLdb.cursors import DictCursor

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "supersecretkey")  # needed for flash messages

# Configure MySQL
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'Super7898$$#')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'serviceDB')

mysql = MySQL(app)


# -------------------------------
# ROUTES
# -------------------------------

# Home page / Add Service
@app.route('/add/', methods=['GET', 'POST'])
def add_service():
    if request.method == 'POST':
        new_service = request.form.get('new_service')
        if not new_service or new_service.strip() == "":
            flash("Service cannot be empty.", "error")
            return redirect(url_for('add_service'))

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO tbl_service (Services) VALUES (%s)", [new_service])
        mysql.connection.commit()
        cur.close()
        flash("Service added successfully!", "success")
        return redirect(url_for('list_services'))

    return render_template('add.html')


# List all services
@app.route('/list')
def list_services():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT * FROM tbl_service")
    rows = cur.fetchall()
    cur.close()
    return render_template("list.html", rows=rows)


# Edit Service page
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_service(id):
    cur = mysql.connection.cursor(DictCursor)
    if request.method == 'POST':
        new_value = request.form.get('Services')
        if not new_value or new_value.strip() == "":
            flash("Service cannot be empty.", "error")
            return redirect(url_for('edit_service', id=id))

        cur.execute("UPDATE tbl_service SET Services=%s WHERE Id=%s", (new_value, id))
        mysql.connection.commit()
        cur.close()
        flash("Service updated successfully!", "success")
        return redirect(url_for('list_services'))

    # GET request: fetch service
    cur.execute("SELECT * FROM tbl_service WHERE Id=%s", (id,))
    service = cur.fetchone()
    cur.close()
    if not service:
        abort(404)
    return render_template("edit.html", service=service)


# Delete service
@app.route('/delete/<int:id>', methods=['POST'])
def delete_service(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tbl_service WHERE Id=%s", (id,))
        mysql.connection.commit()
        flash("Service deleted successfully!", "success")
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Error deleting service: {str(e)}", "error")
    finally:
        cur.close()
    return redirect(url_for('list_services'))


# Index redirects to list
@app.route('/')
def index():
    return redirect(url_for('list_services'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)