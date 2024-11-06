
# FastAPI Tortoise UserManager

This is a simple user management system built using FastAPI, Tortoise ORM, and PostgreSQL for handling user authentication and management features.

## Installation Guide

### Prerequisites
- Python 3.8+
- PostgreSQL
- `pip` or `poetry` for managing Python dependencies

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ehsadev/fastapi-tortoise-usermanager.git
   cd fastapi-tortoise-usermanager
   ```

2. **Create a Virtual Environment:**
   - Using `venv` (optional but recommended):
     ```bash
     python3 -m venv venv
     source venv/bin/activate  # On Windows use venv\Scripts\activate
     ```

3. **Install Dependencies:**
   - Using `pip`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Set Up PostgreSQL:**
   - Ensure that PostgreSQL is installed and running.
   - Create a database and user for the application:
     ```sql
     CREATE DATABASE fastapi_user_manager;
     CREATE USER yourusername WITH PASSWORD 'yourpassword';
     ALTER ROLE yourusername SET client_encoding TO 'utf8';
     ALTER ROLE yourusername SET default_transaction_isolation TO 'read committed';
     ALTER ROLE yourusername SET timezone TO 'UTC';
     GRANT ALL PRIVILEGES ON DATABASE fastapi_user_manager TO yourusername;
     ```

5. **Configure the Database:**
   - Edit `app/config.py` to set your PostgreSQL connection details:
     ```python
     DATABASE_URL = "postgres://yourusername:yourpassword@localhost/fastapi_user_manager"
     ```

6. **Run Database Migrations:**
   ```bash
   alembic upgrade head
   ```

7. **Run the Application:**
   - Start the FastAPI server:
     ```bash
     uvicorn app.main:app --reload
     ```

   The server should now be running at `http://127.0.0.1:8000`.

### Testing the Application

- You can test the user management features via the FastAPI interactive docs at `http://127.0.0.1:8000/docs`.

## Features

- User registration
- Login using JWT Authentication
- Password hashing
- User profile management

## License

This project is licensed under the MIT License.
