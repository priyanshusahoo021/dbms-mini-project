from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = "change-this-for-your-project"

# IMPORTANT: Replace YOUR_MYSQL_PASSWORD with your MySQL root password.
DB_CONFIG = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "0069",
    "database": "student_db",
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route("/")
def index():
    try:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT student_id, first_name, last_name, email, phone, course, semester FROM students ORDER BY student_id DESC")
        students = cur.fetchall()
        cur.close()
        conn.close()
        return render_template("index.html", students=students, error=None)
    except Error as e:
        return render_template("index.html", students=[], error=f"Database error: {e}")

@app.route("/add", methods=["POST"])
def add_student():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO students (first_name, last_name, email, phone, course, semester)
               VALUES (%s, %s, %s, %s, %s, %s)""",
            (
                request.form["first_name"].strip(),
                request.form["last_name"].strip(),
                request.form["email"].strip(),
                request.form.get("phone", "").strip() or None,
                request.form["course"].strip(),
                int(request.form["semester"]),
            ),
        )
        conn.commit()
        cur.close()
        conn.close()
        flash("Student added successfully.")
    except Error as e:
        flash(f"Could not add student: {e}")
    except ValueError:
        flash("Semester must be a number.")
    return redirect(url_for("index"))

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()
        cur.close()
        conn.close()
        flash("Student deleted.")
    except Error as e:
        flash(f"Could not delete student: {e}")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
