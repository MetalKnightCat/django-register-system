# 🚀 Django User Registration and Login System

This project is a test I’ve made while learning Django. It’s a simple user registration and login system that allows users to create an account, log in, and view a list of registered users.

---

## 🛠️ Features

1. **User Registration**:
   - Users can create an account by providing their email and password.
   - Passwords are securely stored in the database.

2. **User Login**:
   - Registered users can log in using their email and password.

3. **User List**:
   - Admins or logged-in users can view a list of all registered users, including their email and registration date.

4. **Dark Red/Black Theme**:
   - The app features a sleek, modern design with dark red accents and rounded elements.

---

## 🛠️ How to Run the Project

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/django-simple-register-user.git
cd django-simple-register-user
```

### 2. Set UP a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

### 7. Access the App
- Open your browser and go to http://127.0.0.1:8000/. 
- Use the login and registration forms to create an account or log in.

## 🖥️ How It Works
1. **Backend**:
Built with Django, the backend handles user registration, login, and database management.
The User model stores user details like email, password, and registration date.

2. **Frontend**:
The frontend is built with HTML, CSS, and JavaScript.
It features a responsive design with smooth transitions and a dark red/black theme.

3. **Database**:
SQLite is used as the default database for development.

## 📝 Notes
- This project is a learning exercise and is not intended for production use.
- Passwords are stored in plain text for simplicity. In a real-world application, use Django’s built-in authentication system for secure password handling.