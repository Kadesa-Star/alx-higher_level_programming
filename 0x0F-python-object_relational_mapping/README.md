Project Structure and Requirements
Environment Setup

Use Ubuntu 20.04 LTS.
Python version should be 3.8.5.
MySQLdb version 2.0.x should be used.
SQLAlchemy version should be 1.4.x.
Ensure all files start with #!/usr/bin/python3 and end with a newline.
Code Style and Execution

Code should follow pycodestyle (version 2.8.x).
All Python files must be executable (chmod +x file.py).
File lengths will be checked using wc.
Documentation Requirements

README.md file at the root explaining the project.
Modules, classes, and functions must have proper docstrings explaining their purpose.
Docstrings should be sentences, not just a word.
Project Implementation Outline
Setup Database Connection

Use SQLAlchemy to connect to MySQL database using MySQLdb.
Configure SQLAlchemy to manage connections and sessions.
Define ORM Models

Create Python classes that map to database tables using SQLAlchemy's ORM capabilities.
Each class should represent a table, with attributes representing columns.
Basic CRUD Operations

Implement methods for Create, Read, Update, and Delete operations using SQLAlchemy ORM methods (session.add(), session.query(), etc.).
Ensure proper error handling and session management.
Querying and Filtering

Demonstrate various querying techniques like filtering, ordering, and aggregating using SQLAlchemy's query API.
Avoid using raw SQL queries as per requirements.
Transactions and Sessions

Manage transactions using SQLAlchemy's session object.
Ensure data integrity through proper commit and rollback mechanisms.
Testing and Validation

Create test scripts to validate ORM functionality.
Test different scenarios like edge cases, concurrent transactions, and data validation.
Documentation and README

Write a comprehensive README.md file explaining the project purpose, setup instructions, usage examples, and any other relevant information.
Ensure all code files, modules, classes, and functions have meaningful docstrings describing their purpose and usage.
Example Project Structure
Copy code
project_folder/
│
├── README.md
├── requirements.txt
├── db_connector.py
├── models.py
├── crud_operations.py
└── tests/
    ├── test_crud_operations.py
    └── test_queries.py
