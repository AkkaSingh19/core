# Core

Core is a Django backend project demonstrating advanced backend development skills by integrating Django REST Framework (DRF), secure authentication, asynchronous task management with Celery, Redis, Telegram Bot integration, and production-ready code management.

---

## ✨ Features

- Auto-Start & Ngrok Integration  
  Automates local server startup and secure tunneling for rapid testing and webhook setup.

- Telegram Integration  
  Seamlessly connects Django app with Telegram, managing users and messaging workflows.

- Asynchronous Tasks  
  Leverages Celery for background processing, ensuring smooth user experiences.

- Command-line Management  
  Simplifies environment setup, migrations, and maintenance with Django's manage.py.

- Configurable & Extensible  
  Uses modern configuration standards for easy customization and scaling.

- Secure Authentication  
  Provides user registration, login, and protected API endpoints for robust access control.

---

## 🚀 Tech Stack

- Django
- Django REST Framework (DRF)
- Celery
- Redis
- PostgreSQL
- Telegram Bot API
- Ngrok
- Python
- uv (Package manager)

---

## 📦 Getting Started

### Prerequisites

- Python installed
- uv installed (pip install uv)

### Installation

1. Clone the repository:

`bash
git clone https://github.com/AkkaSingh19/core

2. Navigate to the project directory:

cd applications

3. Install all dependencies:

uv sync --all-extras --dev

Usage

Run the project with:

uv run python {entrypoint}

> Replace {entrypoint} with your actual entry point file (commonly manage.py for Django).




---

### 🔐 Environment Variables

The following environment variables are required for proper functioning:

Variable Description

SECRET_KEY Django secret key
SECRET_JWT_KEY API secret key for JWT authentication
DEBUG Set False for production
DATABASE_NAME Name of the PostgreSQL database
DATABASE_USER PostgreSQL user
DATABASE_PASSWORD PostgreSQL user password
EMAIL_BACKEND Email backend setting
EMAIL_HOST SMTP host
EMAIL_PORT SMTP port
EMAIL_HOST_USER SMTP user
EMAIL_HOST_PASSWORD SMTP password
CELERY_BROKER_URL URL for Celery broker (e.g. Redis)
CELERY_RESULT_BACKEND URL for Celery result backend
BOT_TOKEN Telegram Bot API token



---

#### 🖥 How to Run Locally

1. Set up your .env file with the required environment variables.


2. Apply database migrations:

uv run python manage.py migrate

3. Create a superuser (optional for admin access):

uv run python manage.py createsuperuser

4. Run the development server:

uv run python manage.py runserver

5. Run the development server along with telebot:

uv run python auto_start.py

6. Run Celery worker in another terminal (to send mails through celery):

celery -A core worker --loglevel=info

---

##### 📄 API Documentation

DRF Browsable URL (for local development)-
http://localhost:8000/api/

## Authentication
Token Based Authentication (DRF Token Auth)

After login, include the token in the request headers:

Authorization: Token your_token_here



### API Endpoints


1️⃣ User Registration

URL: /api/register/

Method: POST

Description: Register a new user.

Request Body:


{
  "username": "string",
  "email": "string",
  "password": "string"
}

Response (201 Created):


{
  "id": 1,
  "username": "string",
  "email": "string"
}


2️⃣ User Login

URL: /api/login/

Method: POST

Description: Authenticate user and receive auth token.

Request Body:


{
  "username": "string",
  "password": "string"
}

Response (200 OK):


{
  "token": "your_token_here"
}



3️⃣ Public Endpoint

URL: /api/public/

Method: GET

Description: Public data accessible without authentication.

Response Example:


{
  "message": "This is a public endpoint."
}



4️⃣ Protected Endpoint

URL: /api/protected/

Method: GET

Description: Private data, accessible only to authenticated users.

Headers:


Authorization: Bearer<Token your_token_here>

Response Example:


{
  "message": "This is a protected endpoint for authenticated users."
}




# Error Responses

Code Meaning Reason

400 Bad Request Invalid input data
401 Unauthorized Missing or invalid token
403 Forbidden Not authorized to access
404 Not Found Resource does not exist
500 Internal Server Error Server encountered an error