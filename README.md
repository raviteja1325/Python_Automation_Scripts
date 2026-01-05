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
