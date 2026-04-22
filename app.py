from flask import Flask, render_template, request, redirect, session, flash, make_response
import sqlite3, csv
from io import StringIO
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = "secret123"

def connect_db():
    return sqlite3.connect('database.db')

# LOGIN (SECURE)
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM admin WHERE username=?", (user,))
        data = cur.fetchone()
        conn.close()

        if data and check_password_hash(data[1], pwd):
            session['user'] = user
            return redirect('/dashboard')
        else:
            flash("Invalid login")

    return render_template('login.html')

# DASHBOARD WITH DATA FOR CHARTS
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')

    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM students")
    total = cur.fetchone()[0]

    cur.execute("SELECT SUM(fee) FROM students")
    fee = cur.fetchone()[0] or 0

    # chart data
    cur.execute("SELECT status, COUNT(*) FROM students GROUP BY status")
    status_data = cur.fetchall()

    conn.close()

    labels = [row[0] for row in status_data]
    values = [row[1] for row in status_data]

    return render_template('dashboard.html',
                           total=total,
                           fee=fee,
                           labels=labels,
                           values=values)

# ADD
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        fee = request.form['fee']
        status = request.form['status']

        conn = connect_db()
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM students")
        count = cur.fetchone()[0]
        room = (count // 2) + 1

        cur.execute("INSERT INTO students (name, room, fee, status) VALUES (?, ?, ?, ?)",
                    (name, room, fee, status))

        conn.commit()
        conn.close()

        return redirect('/view')

    return render_template('add_student.html')

# VIEW
@app.route('/view')
def view_students():
    search = request.args.get('search')

    conn = connect_db()
    cur = conn.cursor()

    if search:
        cur.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + search + '%',))
    else:
        cur.execute("SELECT * FROM students")

    data = cur.fetchall()
    conn.close()

    return render_template('view_students.html', students=data)

# DELETE
@app.route('/delete/<int:id>')
def delete(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect('/view')

# EDIT
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        fee = request.form['fee']
        status = request.form['status']

        cur.execute("UPDATE students SET name=?, fee=?, status=? WHERE id=?",
                    (name, fee, status, id))
        conn.commit()
        conn.close()
        return redirect('/view')

    cur.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cur.fetchone()
    conn.close()

    return render_template('edit.html', student=student)

# ROOMS
@app.route('/rooms')
def rooms():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT room, COUNT(*) FROM students GROUP BY room")
    rooms = cur.fetchall()

    conn.close()

    return render_template('rooms.html', rooms=rooms)

# EXPORT
@app.route('/export')
def export():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    conn.close()

    si = StringIO()
    writer = csv.writer(si)

    writer.writerow(['ID','Name','Room','Fee','Status'])
    for row in data:
        writer.writerow(row)

    response = make_response(si.getvalue())
    response.headers["Content-Disposition"] = "attachment; filename=students.csv"
    response.headers["Content-type"] = "text/csv"

    return response

# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)