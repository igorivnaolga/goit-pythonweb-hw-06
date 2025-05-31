# 🎓 Student Management System

This project manages students, groups, teachers, subjects, and grades using:

- ✅ SQLAlchemy (ORM)
- 🧬 Alembic (migrations)
- 🐘 PostgreSQL (database)
- 🧪 Seed and select scripts
- 🛠️ Makefile for command automation

---

## ⚙️ Setup Instructions (Using `Makefile`)

### 1. Clone the project

git clone https://github.com/igorivnaolga/goit-pythonweb-hw-06.git

cd goit-pythonweb-hw-06

### 2. 🧱 Create a virtual environment

make venv

### 3. 🧰 Install all dependencies

make setup

This installs poetry, sets up your project environment, and installs all dependencies.

### 4.🔧 Configure Database

Update the config.ini file with your PostgreSQL credentials:

[DB]
PASSWORD=your_db_password
DB_NAME=postgres
DOMAIN=localhost
Ensure your PostgreSQL server is running and the postgres database exists.

### 📂 Migrations

1. Create a migration revision

make db-revision "initial migration"

2. Apply migrations to database

make db-upgrade

3. Check migration status

make db-current

4. See migration history

make db-history

### 🌱 Seed the Database

Populate the database with test data:

make db-seed

### 🔍 Run Select Queries

Run all 10 predefined SQL queries and print results:

make run

🔬 Development Tools
🧹 Format and lint code

make lint

🧪 Run tests

make test

📈 Type checking

make mypy
