Cab Booking App (CLI)
A command-line interface (CLI) application built with Python and MySQL for managing taxi bookings, driver assignments, and trip records. 
This project serves as a lightweight backend demonstration for a ride-hailing system.

 Features
User Management: Register and manage passenger profiles.

Cab/Driver Management: Store and retrieve driver information and vehicle details.

Booking System: Create new ride requests with pickup and drop-off locations.

Database Integration: Full persistence using MySQL to track rides and user history.

CLI Interface: Simple terminal-based interaction for easy use.

 Tech Stack
Language: Python 3.x

Database: MySQL

Libraries: mysql-connector-python, python-dotenv

 Project Structure
main.py: The entry point of the application containing the CLI logic.

table_db.py: Handles the creation of database tables and schema setup.

db.py: Contains the database connection logic and reusable CRUD operations.

taxify.sql: SQL script containing the database schema and sample data.

.env: (Ignored in Git) Used for storing sensitive database credentials.

 Setup Instructions
1. Prerequisites
Ensure you have Python installed.

Ensure MySQL Server is installed and running.

2. Database Setup
Log into your MySQL terminal:

Bash
mysql -u your_username -p
Import the provided SQL schema:

SQL
SOURCE path/to/taxify.sql;
3. Installation
Clone the repository:

Bash
git clone https://github.com/Francesscodes/cab-booking-app.git
cd cab-booking-app
Install the required dependencies:

Bash
pip install mysql-connector-python python-dotenv
4. Configuration
Create a .env file in the root directory and add your MySQL credentials:

Code snippet
DB_HOST=localhost
DB_USER=your_username
DB_PASSWORD=your_password
DB_NAME=taxify

 Usage
Run the application using:

Bash
python main.py
Follow the on-screen prompts to register as a user, view available cabs, or book a ride.

 Contributing
Contributions are welcome! If you'd like to improve the code or add features:

Fork the repository.

Create a new branch (git checkout -b feature-name).

Commit your changes.

Push to the branch and open a Pull Request.

Developed by Francesscodes
