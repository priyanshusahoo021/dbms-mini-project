STUDENT RECORD MANAGEMENT SYSTEM - QUICK START

1. Extract this folder to C:\Mini Project (or another folder).
2. Open the folder in VS Code.
3. In app.py, replace YOUR_MYSQL_PASSWORD with the root password you set during MySQL installation.
4. In MySQL Workbench, run the contents of schema.sql.
5. Open a VS Code terminal in this project folder.
6. Activate your existing virtual environment if you have one:
   Windows Command Prompt: venv\Scripts\activate.bat
7. Install packages:
   python -m pip install Flask mysql-connector-python
8. Start the app:
   python app.py
9. Open http://127.0.0.1:5000 in your browser.
10. Add a sample student and take a screenshot for your submission.

Features: INSERT student, SELECT/list students, DELETE student.
If you get "Access denied", verify the MySQL password in app.py.
If you get "Table doesn't exist", run schema.sql in Workbench.
