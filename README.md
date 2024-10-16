<!-- # Database Migration
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head -->

Personal Financial Management API
This project is a personal financial management backend built with Python's FastAPI. It allows users to track daily spending, manage future spending plans, and view monthly reports of their finances.

🚀 Features
User Authentication: Secure user registration and login with JWT-based authentication.
Daily Spending Tracker: Log daily expenses and categorize them for better financial awareness.
Monthly Financial Reports: Get a detailed report of your spending patterns for each month.
Future Spending Plans: Set financial goals and track your progress toward achieving them.
Data Visualization: View your remaining balance and spending habits with interactive charts (coming soon).
🛠️ Tech Stack
Backend: FastAPI
Database: PostgreSQL
ORM: SQLAlchemy
Migrations: Alembic
Authentication: JWT (JSON Web Tokens)
Containerization: Docker
📦 Installation
To set up the project locally, follow these steps:

Clone the repository:

git clone https://github.com/boekaungkyaw22/fms_boe.git
cd fms_boe
Install the required dependencies:

pip install -r requirements.txt
Set up the environment variables. Create a .env file with the following:

DATABASE_URL=postgresql://user:password@localhost/dbname
JWT_SECRET_KEY=your_jwt_secret_key
Set up the database and run migrations:

alembic upgrade head
Start the FastAPI server:

uvicorn src.main:app --reload
🔄 Database Migration
To generate a new migration after changes to the data models:

alembic revision --autogenerate -m "Your migration message"
alembic upgrade head
📚 Usage
Once the server is running, you can access the API docs at:

http://localhost:8000/docs
🧪 Running Tests
To run unit tests:

pytest
🐳 Docker Setup
To run the project using Docker:

Build the Docker image:

docker build -t fms_boe .
Run the Docker container:

docker-compose up
📖 API Documentation
The API is fully documented using FastAPI's auto-generated documentation system. After running the server, visit:

Swagger UI - Interactive API documentation
Redoc - API Reference
👥 Contributing
Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Open a pull request.
📝 License
This project is licensed under the MIT License.

Author: Boe Kaung Kyaw
Contact: boekaungkyaw@gmail.com
