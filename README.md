****CAR RENTAL****

Introduction

This project is a Django web application designed to streamline car rental business operations and enhance customer relationships. It provides a centralized platform for managing:

Vehicles: Fleet management, including car details, maintenance schedules, and availability tracking.

Customers: Secure storage of customer information, rental history, and preferences for personalized experiences.

Reservations: Online booking system, reservation management with status updates, and automatic confirmations and notifications.

Rentals: Streamlined rental process, including online payments, damage assessments, and contract generation.

Reporting & Analytics: Generate reports on rentals, revenue, customer trends, and fleet utilization to inform business decisions.

This CRM system aims to improve efficiency, increase customer satisfaction, and optimize resource management for car rental companies.


****Prerequisites****

Python (version 3.11 or later): You can download it from the official Python website: https://www.python.org/downloads/.
pip (package installer for Python): It usually comes bundled with Python. Verify its presence using python -m pip --version in your terminal.


****Setting Up the Project****

1.Clone the Repository:

git clone https://github.com/Soni912108/CRM.git

cd <crm_project>

2.Create a Virtual Environment (Recommended):

A virtual environment helps isolate project dependencies from your system-wide Python installations:

python -m venv venv(or a name you like)  # For Python 3.3+

source venv/bin/activate  # Activate the virtual environment (Linux/macOS)

venv\Scripts\activate.bat  # Activate on Windows

3.Install Dependencies:

Install the required packages listed in requirements.txt:

pip install -r requirements.txt


****Running the Development Server****

1.Start the development server:

python manage.py runserver

This will typically start the server at http://127.0.0.1:8000/ by default. You can access your Django application in your web browser at this URL.

****Creating an Admin User****

1.Open a terminal/command prompt.

2.Navigate to your project directory:

cd <crm_project>

3.Run the following command to create an admin user:

python manage.py createsuperuser

Follow the prompts to enter a username, email address, and password for your admin account.


****Database Migrations****

When you modify your models (e.g., adding a new field), Django needs to update the database schema to reflect those changes. Use the following commands:

1.Create database migrations:

python manage.py makemigrations

2.Apply migrations to the database:

python manage.py migrate

