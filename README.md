# Python_Automation_Scripts
Practice repository for Python automation scripts commonly used in DevOps workflows. Perfect for interview prep, certifications, and real-world automation tasks!

📁 Directory File Lister
Purpose: List files across multiple directories with error handling—ideal for log analysis, backup verification, or deployment audits.

Features
Multi-directory input via space-separated paths

Robust error handling (Permission Denied, Not Found)

Clean, formatted output with timestamps

DevOps-ready: Handles Linux/Windows paths

Algorithm
Accept space-separated folder paths from user input

Split input string into directory list

Iterate through each directory using for loop

Use os.listdir() to enumerate files

Wrap in try-except to catch FileNotFoundError, PermissionError

Display files or clear error messages print list of files in the user mentioned folder

2. Get List of Users from GitHub (or Any API) **This is bold text**

This script demonstrates how to call a REST API (e.g., GitHub) in Python, parse the JSON response, and print a list of users.
​

🎯 Goal
Fetch data from an HTTP API endpoint, extract user information from the JSON response, and display it in a readable format.

🔁 Algorithm
Use the requests library to send an HTTP GET request to an API endpoint (for example, GitHub public users API).
​

Receive and parse the JSON response using .json() and store it in a variable.

Treat the JSON as a Python object (usually a list of dictionaries or a dictionary) and iterate over it with a for loop.
​

From each item, extract the desired user field (e.g., login) and print or store it.


