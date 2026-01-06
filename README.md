# Python_Automation_Scripts
Practice repository for Python automation scripts commonly used in DevOps workflows. Perfect for interview prep, certifications, and real-world automation tasks!

# **Directory File Lister**
Purpose: List files across multiple directories with error handling—ideal for log analysis, backup verification, or deployment audits.

**Features**
1. Multi-directory input via space-separated paths

2. Robust error handling (Permission Denied, Not Found)

3. Clean, formatted output with timestamps

4. DevOps-ready: Handles Linux/Windows paths

**Algorithm**
1. Accept space-separated folder paths from user input

2. Split input string into directory list

3. Iterate through each directory using for loop

4. Use os.listdir() to enumerate files

5. Wrap in try-except to catch FileNotFoundError, PermissionError

6. Display files or clear error messages print list of files in the user mentioned folder



# **Get List of Users from GitHub (or Any API)**

This script demonstrates how to call a REST API (e.g., GitHub) in Python, parse the JSON response, and print a list of users.
​

🎯 **Goal**
Fetch data from an HTTP API endpoint, extract user information from the JSON response, and display it in a readable format.

🔁 **Algorithm**
1. Use the requests library to send an HTTP GET request to an API endpoint (for example, GitHub public users API).
​

2. Receive and parse the JSON response using .json() and store it in a variable.

3. Treat the JSON as a Python object (usually a list of dictionaries or a dictionary) and iterate over it with a for loop.
​

4. From each item, extract the desired user field (e.g., login) and print or store it.


