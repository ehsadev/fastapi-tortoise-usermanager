<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Tortoise UserManager</title>
</head>
<body>
    <h1>FastAPI Tortoise UserManager</h1>
    <p>This is a simple user management system built using FastAPI, Tortoise ORM, and PostgreSQL for handling user authentication and management features.</p>

    <h2>Installation Guide</h2>
    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.8+</li>
        <li>PostgreSQL</li>
        <li><code>pip</code> or <code>poetry</code> for managing Python dependencies</li>
    </ul>

    <h3>Steps to Install</h3>
    <ol>
        <li><strong>Clone the Repository:</strong>
            <pre><code>git clone https://github.com/ehsadev/fastapi-tortoise-usermanager.git
cd fastapi-tortoise-usermanager</code></pre>
        </li>
        <li><strong>Create a Virtual Environment:</strong>
            <p>Using <code>venv</code> (optional but recommended):</p>
            <pre><code>python3 -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate</code></pre>
        </li>
        <li><strong>Install Dependencies:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Set Up PostgreSQL:</strong>
            <p>Ensure that PostgreSQL is installed and running. Create a database and user for the application:</p>
            <pre><code>CREATE DATABASE fastapi_user_manager;
CREATE USER yourusername WITH PASSWORD 'yourpassword';
ALTER ROLE yourusername SET client_encoding TO 'utf8';
ALTER ROLE yourusername SET default_transaction_isolation TO 'read committed';
ALTER ROLE yourusername SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE fastapi_user_manager TO yourusername;</code></pre>
        </li>
        <li><strong>Configure the Database:</strong>
            <p>Edit <code>app/config.py</code> to set your PostgreSQL connection details:</p>
            <pre><code>DATABASE_URL = "postgres://yourusername:yourpassword@localhost/fastapi_user_manager"</code></pre>
        </li>
        <li><strong>Run Database Migrations:</strong>
            <pre><code>alembic upgrade head</code></pre>
        </li>
        <li><strong>Run the Application:</strong>
            <p>Start the FastAPI server:</p>
            <pre><code>uvicorn app.main:app --reload</code></pre>
            <p>The server should now be running at <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>.</p>
        </li>
    </ol>

    <h3>Testing the Application</h3>
    <p>You can test the user management features via the FastAPI interactive docs at <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs</a>.</p>

    <h2>Features</h2>
    <ul>
        <li>User registration</li>
        <li>Login using JWT Authentication</li>
        <li>Password hashing</li>
        <li>User profile management</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>
