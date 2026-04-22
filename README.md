# 🏨 Hostel Management System

A full-stack web application developed using Flask to manage hostel operations such as student records, room allocation, and fee tracking.

---

## 📸 Screenshots

### 🔐 Login Page

![Login](static/screenshots/login.png)

### 📊 Dashboard

![Dashboard](static/screenshots/dashboard.png)

### 📋 Student Management

![Students](static/screenshots/students.png)

---

## 🚀 Features

* 🔐 Secure Admin Login (Password Hashing)
* ➕ Add Student Details
* 📋 View Students List
* ✏️ Edit Student Information
* ❌ Delete Student Records
* 🔍 Search Students
* 🛏️ Automatic Room Allocation (2 students per room)
* 💳 Fee Status (Paid / Pending)
* 📊 Dashboard with Charts (Chart.js)
* 📥 Export Data to CSV
* 📱 Responsive UI using Bootstrap

---

## 🛠️ Technologies Used

* **Frontend:** HTML, CSS, Bootstrap
* **Backend:** Python (Flask)
* **Database:** SQLite
* **Charts:** Chart.js
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
hostel_management/
│
├── app.py
├── database.py
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── add_student.html
│   ├── view_students.html
│   ├── edit.html
│   ├── rooms.html
│
├── static/
│   ├── images/
│   └── screenshots/
│
├── requirements.txt
├── Procfile
└── README.md
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/hostel-management-system.git
```

2. Navigate to the project folder:

```
cd hostel-management-system
```

3. Install dependencies:

```
pip install flask werkzeug
```

4. Setup database:

```
python database.py
```

5. Run the application:

```
python app.py
```

6. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🔑 Default Login Credentials

* **Username:** admin
* **Password:** admin123

---

## 📊 Dashboard Details

* Displays total number of students
* Shows total fees collected
* Visualizes fee status (Paid vs Pending) using charts

---

## 📌 Future Enhancements

* 📷 Student Photo Upload
* 💳 Online Fee Payment Integration
* 🌐 Live Deployment
* 🔔 Notification System
* 📱 Mobile App Version

---

## 🎯 Project Objective

To design and develop a user-friendly system that automates hostel management tasks, reduces manual effort, and improves data accuracy.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
