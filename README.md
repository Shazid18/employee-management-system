# Employee Management System

This project is an Employee Management System built using the Django web framework. The system allows users to manage employee data, including adding, editing, and deleting employee records.

## Key Features
- **Add & Edit Employees**: Form-based user interface to add and modify employee information. Images of employees are resized before storing.
- **Search Functionality**: Search employees by name, email, date of birth, and mobile. Search also work for partial matches in case of name and email.
- **Sorting**: Sort employee data by various fields such as name, email, and date of birth.
- **Pagination**: Efficient navigation through the list of employees.
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices.

## Technologies Used
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap)
- **Database**: SQLite (default Django database)

## Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-repo-name/employee-management-system.git](https://github.com/Shazid18/employee-management-system.git)
   cd employee-management-system
   
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install the required packages:
   ```bash
   pip install -r requirements.txt

6. Run the application:
   ```bash
   python manage.py migrate
   python manage.py runserver

8. Access the application at http://127.0.0.1:8000/
