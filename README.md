# Password Strength Checker

## About This Project

Password Strength Checker is a simple Python-based cybersecurity project that analyzes the strength of a password using common security rules.

This project runs as a Command-Line Interface (CLI) application, meaning users interact with the program through the terminal instead of a graphical interface. The goal of this project is to understand how password security checks work and how weak passwords can be identified.

---

## What This Project Does

The program checks a password based on several security requirements:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Commonly used weak passwords

After analyzing the password, the program provides a strength rating and suggestions to improve password security.

---

## Features

* CLI-based password security checker
* Password strength scoring system
* Detection of commonly used weak passwords
* Password improvement recommendations
* Simple and lightweight Python implementation

---

## Technologies Used

* Python 3
* Regular Expressions
* File Handling
* Basic Cybersecurity Concepts

---

## Project Structure

```text
Password-Strength-Checker/
│
├── main.py
├── password_checker.py
├── common_passwords.txt
├── README.md
└── requirements.txt
```

---

## How It Works

The program uses different checks to evaluate password security.

Example:

Input:

```text
Enter password: password123
```

Output:

```text
Score: 2/6
Strength: Weak

Suggestions:
- Add uppercase letters
- Add special characters
- Avoid commonly used passwords
```

The program compares the password against security rules and a list of common weak passwords to determine its strength.

---

## How To Run

1. Download or clone this project.

2. Open the project folder in a terminal.

3. Run the program:

```bash
python main.py
```

4. Enter a password when prompted.

---

## What I Learned

Through this project, I learned:

* How password security requirements work
* How to create a basic cybersecurity tool using Python
* How to validate user input
* How weak passwords can be detected
* The importance of strong password practices

---

## Future Improvements

Possible improvements for future versions:

* Add a graphical user interface (GUI)
* Add a secure password generator
* Add password entropy calculation
* Add password breach checking
* Generate password security reports
* Add password hashing demonstrations