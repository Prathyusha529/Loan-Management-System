# Loan Management System

# Project Overview
The **Loan Management System** is a console-based application developed using Python and MySQL. It helps manage customer information, loan details, EMI calculations, payment transactions, and loan-related reports.

The system provides a simple menu-driven interface that allows users to perform different banking and loan management operations efficiently.

## Technologies Used
- **Programming Language:** Python
- **Database:** MySQL
- **Database Connectivity:** mysql-connector-python

## Features

### 1. Customer Management
- Add new customer details.
- View all customer records.
- Search customers using Customer ID.
- Update customer information.
- Delete customer records.

### 2. Loan Management
- Add loans for registered customers.
- View all loan details.
- Search loans using Loan ID.
- Update loan information.
- Delete loan records.
- Maintain loan status (Active/Closed).

### 3. EMI Management
- Calculate monthly EMI based on loan amount, interest rate, and tenure.
- Calculate total interest and total repayment amount.
- Generate a month-wise EMI repayment schedule.
- Display outstanding loan balance.

### 4. Payment Management
- Record loan payments.
- View payment history.
- Search payments using Payment ID.
- Delete payment records.
- Support different payment modes such as Cash, UPI, and Card.

### 5. Loan Closure
- Close active loans.
- Update loan status after closure.

### 6. Reports
- Generate total customer reports.
- Display total loan count.
- Calculate total payment collections.
- View active loans.
- View closed loans.

### 7. User Authentication
- Login system with username and password verification.
- Restricts access to the main application through authentication.

## Database Tables
The project uses the following MySQL tables:

- **users** – Stores login credentials.
- **customers** – Stores customer personal information.
- **loans** – Stores loan details and status.
- **payments** – Stores loan payment transactions.

## Installation and Execution

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   ```

2. Install the required Python package:
   ```bash
   pip install mysql-connector-python
   ```

3. Create a MySQL database:
   ```sql
   CREATE DATABASE loan_management;
   ```

4. Create the required tables (`users`, `customers`, `loans`, and `payments`) with the appropriate columns.

5. Configure your MySQL username, password, and database name in the Python program.

6. Run the application:
   ```bash
   python main.py
   ```

## Learning Outcomes
- Practiced Python functions and conditional statements.
- Implemented CRUD operations using Python and MySQL.
- Learned database connectivity using MySQL Connector.
- Applied SQL queries for data management.
- Implemented EMI calculation using mathematical formulas.
- Gained practical experience in developing a database-driven application.

## Future Enhancements
- Develop a graphical user interface using Tkinter.
- Add automatic EMI payment reminders.
- Generate downloadable loan and payment reports.
- Implement secure password hashing.
- Add automatic loan balance and repayment tracking.

## Author
**Your Name**

Python Developer | CSE Graduate