# Gas-Utility


This is a Django-based web application designed to help a gas utility company manage customer service requests and provide customer support. The application allows customers to submit service requests online, track request statuses, and provides tools for customer support representatives to manage requests.

## Features

- Customer can submit service requests online.
- Customers can track the status of their service requests.
- Customer support representatives have tools to manage and support requests.
- Admin interface for managing service requests and user data.

## Technologies Used

- Django
- HTML/CSS
- SQLite (you can use other databases as well)
- etc.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gas-utility-app.git
   cd gas-utility-app
   
2. Set up the database:
   python manage.py migrate
   
3. Create a superuser:
   python manage.py createsuperuser
   
4. Run the development server:
   python manage.py runserver

5. Access the application in your web browser at http://127.0.0.1:8000/.

Usage
Customers can register and log in to submit service requests.
Customer support representatives can log in to manage requests.
Admin interface at /admin/ to manage data.


