🎓 Student Attendance System (Django + REST API)

A web-based Student Attendance System developed using Django and Django REST Framework, designed to manage students and their attendance records efficiently.
The project also includes API testing using Postman for backend validation.

📌 Project Overview

The Student Attendance System helps in:

Managing student information

Recording daily attendance

Viewing and filtering attendance records

Providing REST APIs for external access and testing

This project is suitable for educational institutions and serves as a learning project for Django and REST API development.

🛠️ Tech Stack

Backend Framework: Django

API Framework: Django REST Framework (DRF)

Database: SQLite (default Django DB)

API Testing Tool: Postman

Language: Python

Version Control: Git & GitHub

📂 Project Structure
Student Attendance System/
│
├── attendance_system/
│   ├── attendance_system/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │
│   ├── students/
│   │   ├── models.py
│   │   ├── admin.py
│   │   ├── views.py
│   │   └── migrations/
│   │
│   ├── attendance/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── manage.py
│
├── myenv/
├── .gitignore
└── README.md

⚙️ Features

✅ Student Registration

✅ Attendance Management

✅ REST APIs for Attendance Data

✅ Admin Panel for Data Management

✅ API Testing using Postman

✅ Clean & Modular Django App Structure

🔐 Admin Panel

URL: <http://127.0.0.1:8000/admin/>

Admin can:

Add/Edit/Delete Students

View Attendance Records

Filter & Search Data

🚀 Installation & Setup
1️⃣ Clone the Repository
git clone <https://github.com/HumaVhora/student-attendance-system.git>
cd student-attendance-system

2️⃣ Create & Activate Virtual Environment
python -m venv myenv
myenv\Scripts\activate

3️⃣ Install Dependencies
pip install django djangorestframework

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Run the Server
python manage.py runserver

🧪 API Testing (Postman)

Import API endpoints in Postman

Use GET / POST methods

Verify JSON responses

Validate status codes

📚 Learning Outcomes

Understanding Django project & app structure

CRUD operations using Django ORM

REST API development with DRF

Admin panel customization

API testing using Postman

Git & GitHub workflow

📌 Future Enhancements

Authentication & Role-based Access

Attendance Analytics Dashboard

CSV/Excel Export

Frontend Integration

Docker Support
