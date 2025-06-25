# 🚀 FastAPI Learning Playground

Welcome to the **FastAPI Learning Playground**, a hands-on project by [Alok V](https://github.com/alokv0521) to learn and experiment with FastAPI — one of the fastest Python frameworks for building APIs.

---

## 📁 Current Files & Modules

| File Name             | Purpose                                                                 |
|----------------------|-------------------------------------------------------------------------|
| `main.py`            | Intro + basic FastAPI theory & root route (`/`)                        |
| `path_parameters.py` | Dynamic path handling and path parameter examples                      |
| `post_method.py`     | `POST` request handling, debugging techniques, model validation        |
| `requirements.txt`   | All necessary dependencies (`fastapi`, `uvicorn`, etc.)                |
| `.gitignore`         | Keeps virtual env and other junk out of Git                           |

---

## ✅ Features Covered So Far

- ✅ GET and POST routes
- ✅ Path Parameters (dynamic URLs)
- ✅ Query Parameters
- ✅ Pydantic models and validation
- ✅ Debugging with FastAPI
- ✅ Swagger UI and ReDoc docs
- 🔜 Modular routers (file separation)
- 🔜 Middleware, Auth, and Dependency Injection

---

## 📦 Requirements

fastapi
uvicorn
pydantic
(will update as i learn more)


Install them all:
```bash
pip install -r requirements.txt
# 1. Clone the repo
git clone https://github.com/alokv0521/fastAPI
cd fastAPI

# 2.Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run a specific file 
uvicorn response_model:app --reload
