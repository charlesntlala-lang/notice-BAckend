# Notice Board - Django Project

## Overview
Notice Board is a Django web application for managing notices with categories (Exam, Event, General), priorities (Low, Medium, High), publish/expiry dates, and admin interface. Users can login, view active notices, create/edit/delete.

**Key Features:**
- Notice CRUD with filtering by category/priority/active status
- User authentication (login/logout)
- Admin dashboard
- MongoDB backend (recently configured)

## Tech Stack
- Django 3.1.12 (djongo for MongoDB)
- MongoDB Atlas (via MONGODB_URI in .env)
- HTML/CSS/JS templates
- python-decouple for .env

## Project Structure
```
flask101/
├── notice_board/
│   ├── core/ (Django settings, urls)
│   ├── notices/ (models.py, views.py, forms.py, admin.py)
│   ├── templates/ (base.html, home.html, login.html, etc.)
│   ├── static/ (CSS/JS)
│   ├── manage.py
│   ├── db.sqlite3 (legacy)
│   └── venv/ (Python env)
├── .env (SECRET_KEY, MONGODB_URI)
├── TODO.md
└── README.md
```

## Setup & Run
1. cd notice_board
2. venv\\Scripts\\activate
3. pip install -r requirements.txt (or djongo python-decouple)
4. Add to .env:
   ```
   SECRET_KEY=django-insecure-... (generate if needed)
   MONGODB_URI=mongodb+srv://user:pass@cluster.xxxxx.mongodb.net/dbname?retryWrites=true&w=majority
   ```
5. python manage.py makemigrations notices
6. python manage.py migrate
7. python manage.py createsuperuser
8. python manage.py runserver

**Access:**
- http://127.0.0.1:8000/ (home)
- /admin/ (admin dashboard)
- /login/

## Models
- Notice: title, content, category, priority, publish_date, expiry_date, is_active

## Recent Changes
- Switched to MongoDB (djongo) from SQLite
- .env config for DB URI
- Fixed Python 3.12 compat (legacy-cgi, setuptools)

Happy coding!
