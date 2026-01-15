\
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import sqlite3
from datetime import datetime

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(APP_DIR, "database", "vulnlab.db")
UPLOAD_DIR = os.path.join(APP_DIR, "static", "uploads")

app = Flask(__name__)
app.secret_key = "dev-secret-key-change-me"  # intentionally weak for lab

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    INTENTIONALLY VULNERABLE:
    - SQL Injection due to unsafe string concatenation.
    """
    if request.method == "POST":
        u = request.form.get("username", "")
        p = request.form.get("password", "")

        # ❌ Vulnerable query (DO NOT DO THIS IN REAL APPS)
        query = f"SELECT id, username, role FROM users WHERE username='{u}' AND password='{p}'"
        conn = get_db()
        try:
            user = conn.execute(query).fetchone()
        finally:
            conn.close()

        if user:
            session["user"] = user["username"]
            session["role"] = user["role"]
            flash("Logged in successfully (vulnerable login).")
            return redirect(url_for("dashboard"))
        else:
            flash("Login failed. (Try SQLi payload on username (lab).)")
            return redirect(url_for("login"))

    return render_template("login.html", title="Login (SQLi)")

@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out.")
    return redirect(url_for("index"))

@app.route("/dashboard")
def dashboard():
    if not session.get("user"):
        flash("Please login first.")
        return redirect(url_for("login"))
    return render_template("dashboard.html", title="Dashboard")

@app.route("/search")
def search():
    """
    INTENTIONALLY VULNERABLE:
    - Reflected XSS: user input is rendered with |safe
    """
    q = request.args.get("q")
    unsafe_q = q if q is not None else ""
    return render_template("search.html", title="Search (XSS)", q=q, unsafe_q=unsafe_q)

@app.route("/comments", methods=["GET", "POST"])
def comments():
    """
    INTENTIONALLY VULNERABLE:
    - Stored XSS: comment rendered with |safe
    """
    conn = get_db()
    try:
        if request.method == "POST":
            name = request.form.get("name", "anon")
            comment = request.form.get("comment", "")
            conn.execute(
                "INSERT INTO comments(name, comment, created_at) VALUES (?, ?, ?)",
                (name, comment, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            )
            conn.commit()
            flash("Comment posted.")
            return redirect(url_for("comments"))

        rows = conn.execute(
            "SELECT id, name, comment, created_at FROM comments ORDER BY id DESC LIMIT 20"
        ).fetchall()
        items = [dict(r) for r in rows]
        return render_template("comments.html", title="Comments (Stored XSS)", comments=items)
    finally:
        conn.close()

@app.route("/upload", methods=["GET", "POST"])
def upload():
    """
    INTENTIONALLY WEAK:
    - Only checks extension; stores in public folder
    - Does not randomize filename
    """
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    if request.method == "POST":
        f = request.files.get("file")
        if not f or not f.filename:
            flash("No file selected.")
            return redirect(url_for("upload"))

        filename = f.filename

        # ❌ Weak extension check (bypassable)
        allowed = (".png", ".jpg", ".jpeg", ".gif", ".txt", ".pdf", ".html")
        if not filename.lower().endswith(allowed):
            flash("File type blocked (weak filter). Try allowed extensions in lab.")
            return redirect(url_for("upload"))

        save_path = os.path.join(UPLOAD_DIR, filename)
        f.save(save_path)
        flash(f"Uploaded: {filename}")
        return redirect(url_for("upload"))

    files = []
    try:
        files = sorted(os.listdir(UPLOAD_DIR))
    except FileNotFoundError:
        files = []
    return render_template("upload.html", title="Upload (Insecure)", files=files)

@app.route("/profile")
def profile():
    """
    INTENTIONALLY VULNERABLE:
    - IDOR: Anyone can request any user's profile via ?id=
    - No authorization checks
    """
    user_id = request.args.get("id", "1")
    conn = get_db()
    try:
        row = conn.execute(
            "SELECT id, username, email, role FROM users WHERE id = ?",
            (user_id,),
        ).fetchone()
        user = dict(row) if row else None
        return render_template("profile.html", title="Profile (IDOR)", user=user)
    finally:
        conn.close()

if __name__ == "__main__":
    # Debug enabled for local lab
    app.run(host="127.0.0.1", port=5000, debug=True)
