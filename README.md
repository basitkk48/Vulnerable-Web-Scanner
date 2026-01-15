# 🛡️ VulnLab — Vulnerable Web Application & Penetration Testing Lab (Flask)

> ⚠️ **Disclaimer:**  
> This project is intentionally vulnerable and is created **only for educational and training purposes**.  
> Do NOT deploy this application on the public internet.

---

## 🎯 Project Objective

The purpose of this project is to demonstrate how common web application vulnerabilities occur due to insecure coding practices and how attackers exploit them in real-world scenarios.

This lab helps students to:

- Understand **OWASP Top 10 vulnerabilities**
- Practice **penetration testing techniques**
- Learn **secure coding concepts**
- Gain hands-on cybersecurity experience

---

## 🧠 Problem Statement

Many web applications today are insecure because of:

- Poor input validation  
- Unsafe database queries  
- Weak authentication mechanisms  
- Improper access control  
- Insecure file handling  

As a result, attackers can exploit systems using:

- SQL Injection  
- Cross-Site Scripting (XSS)  
- Unauthorized data access (IDOR)  
- Malicious file uploads  

Students often study these attacks theoretically but lack practical exposure.

---

## ✅ Proposed Solution

We developed **VulnLab**, a deliberately vulnerable web application that allows:

- Practicing real attack techniques
- Observing real security failures
- Understanding attacker behavior
- Learning how vulnerabilities can be fixed

This project follows a **Red Team (Attack) + Blue Team (Defense)** learning model.

---

## 🔥 Implemented Vulnerabilities (OWASP Based)

| # | Vulnerability | Description |
|---|---------------|------------|
| 1 | SQL Injection (Authentication) | Login bypass using SQL payload |
| 2 | Reflected XSS | JavaScript execution via search input |
| 3 | Stored XSS | Persistent scripts via comments |
| 4 | Insecure File Upload | Weak extension-based validation |
| 5 | IDOR (Broken Access Control) | Access other users’ profiles by changing ID |

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)  
- **Database:** SQLite  
- **Frontend:** HTML, CSS (Jinja Templates)  
- **Security Testing:** Burp Suite, Browser DevTools  

---

## 📁 Project Structure

```

VulnLab/
│── app.py
│── requirements.txt
│── README.md
│
├── database/
│   ├── init_db.py
│   └── vulnlab.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── search.html
│   ├── comments.html
│   ├── upload.html
│   └── profile.html
│
├── static/
│   ├── style.css
│   └── uploads/
│
└── reports/
├── pentest_report.md
└── screenshots/

````

---

## 🚀 How to Run the Project

### 🔹 Step 1 — Install Dependencies
```bash
pip install -r requirements.txt
````

### 🔹 Step 2 — Initialize Database

```bash
python database/init_db.py
```

### 🔹 Step 3 — Run Application

```bash
python app.py
```

### 🔹 Step 4 — Open in Browser

```
http://127.0.0.1:5000
```

---

## 🔑 Demo Credentials

| Username | Password |
| -------- | -------- |
| admin    | admin123 |
| user1    | pass123  |
| user2    | pass123  |

---

## 🧪 Penetration Testing Payloads

**SQL Injection (Login)**

```
admin' --
```

**Reflected XSS**

```
<script>alert(1)</script>
```

**Stored XSS**

```
<img src=x onerror=alert(1)>
```

**IDOR**

```
/profile?id=2
```

---

## 📝 Pentest Report

A penetration testing report template is included at:

```
/reports/pentest_report.md
```

It documents:

* Vulnerability description
* Exploitation steps
* Risk level
* Impact
* Recommended fixes

---

## 🎓 Learning Outcomes

After completing this project, students will understand:

* How attackers exploit web apps
* Why insecure coding is dangerous
* How vulnerabilities affect systems
* How to implement secure coding practices

This project is ideal for:

* Cybersecurity students
* Ethical hacking beginners
* Secure coding labs

---

## 👨‍💻 Developers

| Name                      | LinkedIn                                                  | GitHub                                        |
| ------------------------- | --------------------------------------------------------- | --------------------------------------------- |
| Qazi Muhammad Mustafa Ali | 🔗 [https://www.linkedin.com/in/mustafa-ali-7b2a34338/) | 🐙 [https://github.com/Qmma52) |
| Muhammad Hamza Kamran     | 🔗 [https://www.linkedin.com/in/hamza-kamran-271872297/) | 🐙 [https://github.com/Hamza-hani) |


> 👉 Replace links with your actual profiles.

---

## 🚧 Future Enhancements

* Secure version of application
* CSRF protection
* Password hashing
* Role-based access control
* Logging and alert system
* Docker deployment
