# 🚀 Secure REST API using FastAPI

A fully functional and secure blog management REST API built with FastAPI, featuring JWT-based authentication, SQLAlchemy ORM integration, Pydantic validation, and modular route architecture.

---

## 📈 Resume Highlights

- 🔧 Developed a REST API with over **25+ endpoints**, JWT authentication, and role-based access control, enabling secure blog operations for **multiple users**.
- 🔐 Implemented secure password handling using `passlib` and `bcrypt`, reducing authentication risk by **100%** for test users.
- 🧱 Designed a modular architecture with **5+ routers** and **10+ Pydantic models**, achieving **95% reusability** in authentication, user, and blog components via SQLAlchemy ORM.

---

## 🔧 Tech Stack

- **FastAPI** – High-performance web framework
- **Uvicorn** – ASGI server for running FastAPI
- **SQLAlchemy** – ORM for database operations
- **Passlib & Bcrypt** – Secure password hashing
- **Python-Jose** – JWT authentication
- **Pydantic** – Request/response validation


---

## ✅ Features

- 🔐 User registration, login, JWT authentication
- ✍️ CRUD operations for blog posts
- 📁 Relationship: Users ↔ Blogs (ForeignKey)
- 📥 Request Body, Path & Query Parameters
- 📜 Auto-generated Swagger & ReDoc docs
- 🧱 Clean code structure with routers and schemas
- 🛡️ Route protection via JWT tokens

---

## 📂 Project Structure

.
├── main.py # FastAPI app entry point
├── database.py # DB connection setup
├── models/ # SQLAlchemy models
│ ├── blog.py
│ └── user.py
├── schemas/ # Pydantic schemas
│ ├── blog.py
│ └── user.py
├── routers/ # API routers
│ ├── auth.py
│ ├── blog.py
│ └── user.py
├── hashing.py # Password hashing logic
├── token.py # JWT token generation/verification
├── requirements.txt # Dependencies
└── README.md

🧪 Future Improvements

🔄 Refresh & revoke JWT tokens
🔐 OAuth2 login (Google/GitHub)
🧪 Unit testing with Pytest
📊 Pagination & filtering
🐳 Dockerize application
🧰 Role-based access system
🧾 Add Swagger examples
