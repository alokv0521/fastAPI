# 🚀 FastAPI Learning Playground

Welcome to the **FastAPI Learning Playground**, a hands-on repo by [me](https://github.com/alokv0521) to learn and experiment with **FastAPI** — one of the fastest Python frameworks for building APIs.

---

## 📁 Project Structure

| File Name             | Purpose                                                                 |
|----------------------|-------------------------------------------------------------------------|
| `main.py`            | Basic setup and root route (`/`) with intro comments                   |
| `path_parameters.py` | Examples for handling dynamic URLs and path parameters                 |
| `post_method.py`     | Demonstrates POST requests, model validation, and debugging            |
| `response_model.py`  | Shows use of Pydantic models in responses                              |
| `requirements.txt`   | Project dependencies (`fastapi`, `uvicorn`, etc.)                      |
| `.gitignore`         | Excludes virtual environment and system files                          |

---

## ✅ Features Covered

- ✅ GET and POST routes
- ✅ Path and Query Parameters
- ✅ Pydantic models and request validation
- ✅ Swagger UI and ReDoc for API docs
- ✅ Debugging with FastAPI
- 🔜 Modular routers (clean architecture)
- 🔜 Middleware, Authentication, and Dependency Injection

---

## 📦 Tech Stack

- **FastAPI** – High-performance web framework
- **Uvicorn** – ASGI server to run FastAPI
- **SQLAlchemy** – ORM for database operations *(planned)*
- **Passlib & Bcrypt** – Secure password hashing *(planned)*
- **Python-Jose** – JWT-based authentication *(planned)*
- **Pydantic** – Data validation and serialization

---

## 🛠 Getting Started

### 🔧 Installation

```bash
# 1. Clone the repo
git clone https://github.com/alokv0521/fastAPI
cd fastAPI

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
