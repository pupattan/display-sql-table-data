from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
app = Flask(__name__, static_folder=BASE_DIR,
            template_folder=os.path.join(BASE_DIR, "templates"))
app.config['SECRET_KEY'] = 'yasyduyu1dbhaghsdabsdt56858agsdiagsd2312312312'

DB_FILE = os.path.join(BASE_DIR, "data", "users.db")

ROWS_PER_PAGE = 2

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("printdatabase"))


@app.route("/printdatabase", methods=["GET"])
def printdatabase():
    """
    Prints the entire database, more than 5 per page. Use pagination like previous program.
    """
    page = request.args.get('page', 1, type=int)
    offset = (page  - 1 ) * ROWS_PER_PAGE
    con = sqlite3.connect(DB_FILE)
    cur = con.cursor()
    query = f"SELECT * FROM employees LIMIT {ROWS_PER_PAGE} OFFSET {offset}"
    cur.execute(query)
    employees = cur.fetchall()

    cur.close()
    con.close()

    return render_template("view_all.html", employees=employees)


if __name__ == '__main__':
    app.run(debug=True)