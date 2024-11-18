
# Simple Budget Tracker Project

## Welcome to Your Budget Adventure!

Hello, budding web developers! Are you ready to embark on an exciting journey to create your very own Simple Budget Tracker? This project will guide you through building a web application where users can manage their finances, track income and expenses, and visualize their budget. By the end of this adventure, you'll have a shiny new web app, sharpened coding skills, and a project you can proudly showcase. Let's get started!

## Overall Project Overview

### Objective

Create a Simple Budget Tracker web application that allows users to:

- Add income and expenses with descriptions and amounts.
- View a list of all transactions.
- Edit and delete entries.
- Calculate total income, expenses, and remaining budget.
- Visualize spending patterns with simple charts.
- Authenticate: Users can sign up, log in, and manage their accounts.

### Technology Stack
You will use Python and Flask for the back end, and HTML/CSS and JavaScript for the front end. You will use SQLite to store data.

##  Overall Project Features and Requirements

Here's a step-by-step guide to the features your application should include.  Let's dive into the details!

1. Setting Up the Project Environment
- Install Python and Flask: Ensure Python and Git are installed on your system.  Prepare a virtual environment then install Flask and any other packages you may need. (Pro tip: double-check versions and dependencies!)
- Set up a new Flask project: Create a directory for your project and initialize it as a Flask app.
- Git Initialization: Initialize a Git repository and make your first commit. (Tip: get into the habit of committing often to capture your progress!)
- Create Basic HTML Templates: Set up basic HTML templates for your application using a template engine like Jinja2.

2. User Interface Design
- Design a Responsive UI: Use HTML and CSS to create a user-friendly and responsive interface.
  - Implement Bootstrap or another CSS framework for quick styling. (Tip: Keep it simple and intuitive!)
- Create Transaction Forms: Design forms for adding income and expense entries.
  - Each transaction should include a description, amount, category and type (income or expense).
3. Viewing Transactions
- Display Transactions: List all transactions in a tabular format.
  - Use dynamic table generation with Flask templates. (Tip: Make your data easy to read!)
- Implement Sorting and Filtering: Allow users to sort and filter transactions by date, type, or amount.
4. Adding Transactions
- Handle Form Submission: Process form data on the server side.
  - Save transaction data in a database (use SQLite for simplicity).
- Validate Input: Ensure all required fields are filled and handle form validation. (Tip: Validations save you from a world of debugging pain!)
5. Editing and Deleting Transactions
- Edit Transactions: Allow users to update transaction details.
- Implement an edit form pre-filled with existing transaction data.
- Delete Transactions: Provide a way to delete transactions.
  - Include confirmation dialogs for delete actions to prevent accidental deletions.
6. Calculating and Displaying Totals
- Calculate Totals: Compute total income, total expenses, and remaining budget.
  - Update totals dynamically as transactions are added, edited, or deleted.
- Display Totals: Show totals prominently on the page for easy viewing. (Tip: Help users understand their financial status at a glance!)
7. Visualizing Budget Data
- Implement Charts: Use a library like Chart.js to create visual representations of budget data.
  - Create pie charts or bar graphs to display spending patterns.
- Interactive Visuals: Allow users to interact with charts (e.g., hover for details).
8. Implementing User Authentication
- User Registration: Create a registration form to allow users to sign up with a username and password.
  - Use Flask extensions like `Flask-WTF` for form handling and validation.
  - Securely store passwords using a library like `Werkzeug` for hashing.
- User Login: Implement a login form that authenticates users.
  - Use session management to keep users logged in across pages.
  - Display user-specific data once logged in.
- User Logout: Provide functionality for users to log out.
  - Clear session data on logout.


### Bonus Features (Optional Enhancements)
Unleash your creativity and add these features as stretch goals!
- Categories: Add categories for transactions (e.g., Food, Travel, Bills) and allow filtering by category.
- Monthly Reports: Generate monthly summaries of income and expenses.
- Export/Import: Allow users to export their data to a CSV file or import data from one.
- Notifications: Implement alerts for when users exceed budget limits.


## Version Control and Project Management
- Use Git for Version Control: Regularly commit your changes and use meaningful commit messages. (Tip: Think of each commit as a snapshot of your project's journey!)
- Branching Strategy: Use branches for developing new features and merge changes into the main branch once complete.
- Track Your Progress: Utilize GitLab to track progress and document your development journey.
- Share it with me! Make sure to invite/add me to your repository as a developer so I can have a look at your commits and code.

## Project Assessment Strategy

This project is divided into two submissions, to focus mastery of each aspect of modern web application development independently.  Part 1 emphasizes the importance of good front end design and using Git effectively, while Part 2 deepens understanding of back-end development, databases and authentication.  This approach helps build a solid foundation for developing full-stack applications.  Below is a detailed plan for each part of the assessment, including a breakdown of the tasks, learning objectives and assessment criteria.


 
# Part 1: Front-End Development and Version Control (30%) due Friday Week 4 @ 19:00 (11/10/2024)

## Objective

Students will focus on setting up the project using Flask, creating basic templates, and employing Git for version control. This part emphasizes HTML, CSS, and the use of Flask’s templating system to create a simple but complete structure for the application.  Project management will be assessed via the use of Git and frequency and quality of the commits to version control.
## Requirements
### 1.	Project Setup and Git (15 Marks)
   - Initialize a Git repository for the project.
   - Create a basic Flask application structure with separate folders for templates, static files, and configurations.
   - Commit initial setup to the repository with meaningful commit messages.

### 2.	Basic Flask Application (20 Marks)
   - Set up Flask to serve pages from a templates directory.
   - Create routes for each of the following views:
     - Home Page
     - Login/Registration Page
     - Dashboard Page
     - Add Transaction Page
     - Edit Transaction Page
     - Manage Categories Page
     - Reports Page

### 3.	Template Inheritance (20 Marks)
   - Use a base template (base.html) to define the overall structure (header, footer, navigation bar) and extend this for other templates.
   - Ensure that all other templates inherit from base.html.

### 4.	Forms and HTML Structure (20 Marks)
   - Create HTML forms for adding and editing transactions, managing categories, and generating reports. (Optionally use Flask-WTF library to define your forms as Python classes)
   - Mock data for forms/views using dictionaries or static data.
   - Implement form validation on the client side using HTML5 attributes like required.

### 5.	Styling with CSS (20 Marks)
   - Add any necessary custom styling using CSS to enhance the appearance of the application.
   - Ensure the application is responsive and visually appealing.

### Submission Requirements (5 Marks)
- Source Code Repository: Submit a link to your source code repository on GitLab or another platform.
- Video Demonstration: Record a short video (no more than 5 minutes) demonstrating your application’s features, code supporting those, and discussing the development process. (Tip: Show off your favourite parts!)
- Reflection Document: Include a brief reflection on what you learned and any challenges you faced.

## Learning Outcomes

- Understanding of Flask’s project structure and routing.
- Ability to use HTML, CSS, and Flask’s templating system to create a web application.
- Familiarity with Git commands and version control best practices.
- Basic client-side form validation.

# Detailed Guidance for Students
## Front-End and Version Control

- Git and Project Setup: Begin by initializing a Git repository and organizing your Flask project structure. Commit each step with clear, descriptive messages.

- Flask Basics: Set up routes using Flask’s @app.route decorator. Focus on creating separate functions for each view.

- Template Inheritance: Create a `base.html` file to hold common elements (header, footer, navigation). Use {% block app_content %}{% endblock %} in `base.html` and extend it in other templates using {% extends 'base.html' %}.

- Forms and HTML: Create your forms with appropriate HTML or define them in Python using Flask-WTF. Use mock data to simulate interactions. Ensure each form field is represented in the HTML.

- CSS Styling: Write CSS to style your application. Use Bootstrap or another framework to ensure responsiveness. (Hint:  you can use the Flask-Bootstrap library, or any other front end framework, to help you achieve a professional look)
 

# Part 2: Back-End Development and Database Integration (70%) due Friday Week 12 @ 19:00 (06/12/2024)

## Objective

In this part, students will focus on back-end development by adding database support, creating models, implementing authentication, and ensuring data validation and persistence.

## Requirements

### 1.	Database Setup and Models (15 Marks)
   - Integrate a SQL database using SQLAlchemy.
   - Define models for Users, Transactions, and Categories.
   - Create appropriate relationships between models (e.g., many-to-many for transactions and categories).

### 2.	User Authentication (20 Marks)
   - Implement user registration and login functionality using `flask_login`.
   - Ensure that users can only access their own data.

### 3.	Data Validation and Forms (10 Marks)
   - Implement server-side form validation using Flask-WTF validators.
   - Ensure all inputs are properly sanitized and validated before saving to the database.

### 4.	CRUD Functionality (40 Marks)
   - Implement full CRUD operations for transactions and categories.
   - Ensure users can add, edit, delete, and list transactions and categories.

### 5.	Reports and Data Presentation (10 Marks)
   - Implement a monthly report feature that aggregates transaction data and presents it clearly.
   - Allow users to filter reports by date and categories.
     
### Submission Requirements (5 Marks)
- Source Code Repository: Submit a link to your source code repository on GitHub or another platform.
- Video Demonstration: Record a short video (no more than 10 minutes) demonstrating your application’s features and discussing the development process. (Tip: Show off your favorite parts!)
- Reflection Document: Include a brief reflection on what you learned and any challenges you faced.


## Learning Outcomes
- Understanding of database design and integration with a web application.
- Ability to implement secure user authentication and authorization.
- Experience with CRUD operations and data validation in a web application context.
- Skills in creating dynamic reports and presenting data effectively.
  
# Detailed Guidance for Students
## Back-end and database integration
- Database Models: Define your models in models.py. Use SQLAlchemy to define relationships, and manage your SQLite database, ensuring that each user has their own transactions and categories.

- Authentication: Implement user registration and login. Use flask_login to manage user sessions.

- Form validation: Implement forms as Python classes using Flask-WTF.  Define appropriate validation for each field accordingly.

- CRUD Operations: Implement functionality to create, read, update, and delete transactions and categories. Ensure that operations are restricted to the current user.

- Reports: Implement logic to generate reports based on transaction data. Allow filtering by category and date.
- 
# Grading Criteria
Your project will be graded based on the following criteria:
- Functionality: Does the application meet the requirements for each submission and perform all specified tasks?
- User Interface: Is the design user-friendly and visually appealing?
- Code Quality: Is the code well-organized, efficient, and documented?
- Version Control: Is Git used effectively for version management?
- Creativity: Did you add any unique features or enhancements?
- Adherence to requirements: Did you produce good reflection documents at each stage?  Were you able to demonstrate code ownership in your video discussions?

# Ready, Set, Code!

You're now equipped to build a Simple Budget Tracker that not only meets user needs but also showcases your growing skills in web development. Embrace the challenges, enjoy the process, and remember: every bug is just a learning opportunity in disguise. Happy coding, and let the adventure begin!
