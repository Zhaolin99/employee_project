# Employee Management System API

A backend project built with **Django**, **Django REST Framework (DRF)**, **PostgreSQL**, **JWT Authentication**, and **Swagger UI**. This system provides APIs for managing Employees, Departments, Attendance Records, and Performance Evaluations.

---

## 🔹 Project Features

- **Employee Management**: CRUD operations for employees and departments
- **Attendance Tracking**: Record and view monthly attendance
- **Performance Tracking**: Add and manage performance evaluations
- **JWT Authentication**: Secure endpoints with Access/Refresh tokens
- **API Documentation**: Interactive Swagger UI and ReDoc generated automatically
- **Visualization**: Dynamic Pie and Bar charts for employees and attendance
- **PostgreSQL Database**: Robust and scalable relational database
- **Dockerized Setup**: Run the entire project inside Docker containers easily

---

## 🔹 Technologies Used

- Django 4.2
- Django REST Framework (DRF)
- PostgreSQL 14+
- drf-yasg (Swagger / ReDoc Documentation)
- djangorestframework-simplejwt (JWT Authentication)
- django-filter
- Chart.js (Frontend visualizations)
- Docker, Docker Compose

---

## 🔹 Installation & Setup (Local Machine)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/employee-management-api.git
cd employee-management-api
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file at the project root:

```
DB_NAME=employee_db
DB_USER=your_postgres_username
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5433
```

### 5. Migrate Database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Server
```bash
python manage.py runserver
```

Server runs at: `http://127.0.0.1:8000/`

---

## 🔹 Running the Project with Docker

### 1. Build and Start the Containers
```bash
docker-compose up --build
```

This will:
- Build Django and PostgreSQL services
- Connect Django to PostgreSQL inside Docker

### 2. Access Application
- Django App: `http://localhost:8000/`, not build for any functions
- Swagger API Docs: `http://localhost:8000/swagger/`
- Admin Panel: `http://localhost:8000/admin/`

---

## 🔹 API Documentation

After running the server, visit:

- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

The documentation includes:
- All CRUD endpoints
- Authentication flow (JWT login/refresh)
- Filtering, searching, ordering
- Visualization endpoints for charts


---

## 🔹 Authentication Flow

- Obtain tokens:
```POST /api/token/```

- Refresh access token:
```POST /api/token/refresh/```

Authorization header required:
```
Authorization: Bearer <access_token>
```

Protected endpoints require authentication.

---

## 🔹 Visualization

### Employees per Department (Pie Chart)
- API: `/api/charts/employees-per-department/`
- Frontend: `/charts/`

### Monthly Attendance Overview (Bar Chart)
- API: `/api/charts/monthly-attendance-overview/`
- Frontend: `/charts/`

Charts are built dynamically using **Chart.js**.

---

## 🔹 Project Structure

```
employee_project/
├── employees/         # Employees & Departments app (models, views, serializers, urls)
├── attendance/        # Attendance & Performance app (models, views, serializers, urls)
├── templates/         # HTML templates (charts.html)
├── employee_project/  # Project settings and URLs
├── Dockerfile         # Docker image definition
├── docker-compose.yml # Docker multi-service orchestration
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🔹 Future Improvements
- Add Role-based Authentication (Admin, HR, Employee). 
- Add Unit Tests for APIs. 
- Build a simple UI with Django Templates for charts. 
---

## 🔹 License

This project is licensed under the [MIT License](LICENSE).

---

## 🔹 Author

Built with Zhaolin Zhong

GitHub: @Zhaolin99
