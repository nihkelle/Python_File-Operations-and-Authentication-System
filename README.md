# 🐍 Python - File Operations and Authentication System | Data Handling and Security Essentials in Python

## Description
- This project involved developing a Python-based toolset focused on data handling and system security. Core components included creating a robust CSV file parser to read and process complex datasets, and constructing a secure user authentication system with comprehensive error logging functionality. The work demonstrated my ability to manage data workflows, implement essential security features, and maintain detailed records of system interactions—key competencies in building reliable and user-centric software solutions. This project underscores my proficiency in Python programming and my commitment to upholding best practices in data integrity and application security.

# 💻 CVS Data Parser

<b> Code Overview: </b>
- This code demonstrates how to read from a CSV file using Python's `csv` module, iterating over rows in the file and converting each row into a set to possibly eliminate duplicates or for other set-related operations.

```python
import csv
try:
    with open('multi.csv', 'r') as inputFile:
        inputCSV = csv.reader(inputFile)
        for row in inputCSV:
            currentRowContests = set(row)
except FileNotFoundError:
    print("File not found.")
```

<b> Skills Developed - </b>

File Handling: 
- Gained proficiency in reading and manipulating data from CSV files, crucial for data analytics and reporting tasks.
  
Exception Handling: 
- Learned to implement try-except blocks to handle potential I/O errors, improving the reliability and user experience of data-driven applications.
  
Data Structure Usage: 
- Developed the ability to utilize sets to process and manage unique data elements efficiently, enhancing my data preprocessing skills.

# 👥 User Authentication System 

<b> Code Overview: </b>
- This section implements a simple authentication system using a dictionary to store username-password pairs, includes user input for login credentials, and performs validation with basic error handling and logging to a file.

```python
loginData = {"admin": "password", "user52": "1234", "support": "Support" }
userName = input("Enter username: ")
passWord = input("Enter password: ")
if userName in loginData:
    if loginData[userName] == passWord:
        print("Password matches. Login allowed.")
    else:
        print("Invalid login.")
        with open('login_error_log.txt', 'w') as loginErrorOutput:
            loginErrorOutput.write("Invalid login: " + userName)
else:
    print("User not found.")
```

<b> Skills Developed - </b>

Security Fundamentals: 
- Acquired a solid understanding of basic security principles through the creation of a user login system, which is pivotal for protecting sensitive information.
  
Input Validation: 
- Honed skills in validating user credentials against stored data, a common requirement for securing access to software systems.
  
Error Logging: 
- Learned to create an error log file, an essential practice for auditing and troubleshooting within software systems, fostering accountability and maintainability.




