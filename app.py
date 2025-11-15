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
@app.route('/edit_service/<int:id>', methods=['GET', 'POST'])
def edit_service(id):
    cur = mysql.connection.cursor(DictCursor)
    if request.method == 'POST':
        new_value = request.form.get('Services')
        if not new_value or new_value.strip() == "":
            flash("Service cannot be empty.", "error")
            return redirect(url_for('edit_service', id=id))

        cur.execute("UPDATE tbl_service SET Services=%s WHERE ServiceId=%s", (new_value, id))
        mysql.connection.commit()
        cur.close()
        flash("Service updated successfully!", "success")
        return redirect(url_for('list_services'))

    # GET request: fetch service
    cur.execute("SELECT * FROM tbl_service WHERE ServiceId=%s", (id,))
    service = cur.fetchone()
    cur.close()
    if not service:
        abort(404)
    return render_template("edit.html", service=service)


# Delete service
@app.route('/delete_service/<int:id>', methods=['POST'])
def delete_service(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM tbl_service WHERE ServiceId=%s", (id,))
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
##==================================
## adding customers logic
##====================================
# List all services
@app.route('/customers')
def list_customers():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT * FROM Customers")
    rows = cur.fetchall()
    cur.close()
    return render_template("customers.html", rows=rows)

# Page / Add customer
@app.route('/customer/', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        Customername = request.form.get('Customername')
        Email = request.form.get('Email')
        ServiceId = request.form.get('ServiceId')
       
        if not Customername or Customername.strip() == "":
            flash("Customer name field cannot be empty.", "error")
            return redirect(url_for('add_customer'))

        elif not Email  or Email.strip() == "":
            flash("Email field cannot be empty.", "error")
            return redirect(url_for('add_customer'))
        elif not ServiceId or ServiceId.strip() == "":
            flash("Service Id field cannot be empty.", "error")
            return redirect(url_for('add_customer'))
        
        else:
            
           cur = mysql.connection.cursor()
 
           cur.execute("INSERT INTO Customers (Customername, Email,ServiceId) VALUES (%s, %s, %s)",[Customername,Email,ServiceId])
        
           mysql.connection.commit()
        cur.close()
        flash("Customer added successfully!", "success")
        return redirect(url_for('list_customers'))

    return render_template('addcustomer.html')

#====customers logic continues==========##
# Edit Customers page
@app.route('/edit_customer/<int:id>', methods=['GET', 'POST'])
def edit_customer(id):
    cur = mysql.connection.cursor(DictCursor)
    if request.method == 'POST':
        Customername = request.form.get('Customername')
        Email = request.form.get('Email')
        ServiceId = request.form.get('ServiceId')
       
        if not Customername or Customername.strip() == "":
            flash("Customer name field cannot be empty.", "error")
            return redirect(url_for('edit_customer', id=id))
        elif not Email  or Email.strip() == "":
            flash("Email field cannot be empty.", "error")
            return redirect(url_for('edit_customer', id=id))
        elif not ServiceId or ServiceId.strip() == "":
            flash("Service ID field cannot be empty.", "error")
            return redirect(url_for('edit_customer', id=id))
        else:
            
            cur.execute("UPDATE Customers SET Customername=%s, Email=%s, ServiceId=%s WHERE CustomerId=%s", (Customername,Email,ServiceId, id))
            mysql.connection.commit()
            cur.close()
            flash("Customer updated successfully!", "success")
        return redirect(url_for('list_customers'))

    # GET request: fetch customers
    cur.execute("SELECT * FROM Customers WHERE CustomerId=%s", (id,))
    customer= cur.fetchone()
    cur.close()
    if not customer:
        abort(404)
    return render_template("editcustomer.html", customer=customer)



# Delete customer
@app.route('/delete_customer/<int:id>', methods=['POST'])
def delete_customer(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Customers WHERE CustomerId=%s", (id,))
        mysql.connection.commit()
        flash("Customer deleted successfully!", "success")
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Error deleting customer: {str(e)}", "error")
    finally:
        cur.close()
    return redirect(url_for('list_customers'))



##==================================
## adding employees logic
##====================================
# List all employees
@app.route('/employees')
def list_employees():
    cur = mysql.connection.cursor(DictCursor)
    cur.execute("SELECT * FROM Employees")
    rows = cur.fetchall()
    cur.close()
    return render_template("employees.html", rows=rows)

# Page / Add employee
@app.route('/employee/', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        Fullname = request.form.get('Fullname')
        Email = request.form.get('Email')
        ServiceId = request.form.get('ServiceId')
       
        if not Fullname or Fullname.strip() == "":
            flash("Full name field cannot be empty.", "error")
            return redirect(url_for('add_employee'))

        elif not Email  or Email.strip() == "":
            flash("Email field cannot be empty.", "error")
            return redirect(url_for('add_employee'))
        elif not ServiceId or ServiceId.strip() == "":
            flash("Service Id field cannot be empty.", "error")
            return redirect(url_for('add_employee'))
        
        else:
            
           cur = mysql.connection.cursor()
 
           cur.execute("INSERT INTO Employees (Fullname, Email,ServiceId) VALUES (%s, %s, %s)",[Fullname,Email,ServiceId])
        
           mysql.connection.commit()
        cur.close()
        flash("Employee added successfully!", "success")
        return redirect(url_for('list_employees'))

    return render_template('addemployee.html')

#====employees logic continues==========##
# Edit Employees page
@app.route('/edit_employee/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    cur = mysql.connection.cursor(DictCursor)
    if request.method == 'POST':
        Fullname = request.form.get('Fullname')
        Email = request.form.get('Email')
        ServiceId = request.form.get('ServiceId')
       
        if not Fullname or Fullname.strip() == "":
            flash("Full name field cannot be empty.", "error")
            return redirect(url_for('edit_employee', id=id))
        elif not Email  or Email.strip() == "":
            flash("Email field cannot be empty.", "error")
            return redirect(url_for('edit_employee', id=id))
        elif not ServiceId or ServiceId.strip() == "":
            flash("Service ID field cannot be empty.", "error")
            return redirect(url_for('edit_employee', id=id))
        else:
            
            cur.execute("UPDATE Employees SET Fullname=%s, Email=%s, ServiceId=%s WHERE EmployeeId=%s", (Fullname,Email,ServiceId, id))
            mysql.connection.commit()
            cur.close()
            flash("Employee updated successfully!", "success")
        return redirect(url_for('list_employees'))

    # GET request: fetch employees
    cur.execute("SELECT * FROM Employees WHERE EmployeeId=%s", (id,))
    employee= cur.fetchone()
    cur.close()
    if not employee:
        abort(404)
    return render_template("editemployee.html", employee=employee)



# Delete employee
@app.route('/delete_employee/<int:id>', methods=['POST'])
def delete_employee(id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM Employees WHERE EmployeeId=%s", (id,))
        mysql.connection.commit()
        flash("Employee deleted successfully!", "success")
    except Exception as e:
        mysql.connection.rollback()
        flash(f"Error deleting employee: {str(e)}", "error")
    finally:
        cur.close()
    return redirect(url_for('list_employees'))








if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)