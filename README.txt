# College Online Voting System

A web-based **College Online Voting System** developed using Python Flask, MySQL, HTML, CSS, and JavaScript.

The system provides a secure and convenient platform for conducting college elections digitally. It allows administrators to manage elections, candidates, and registered users, while students can register, log in, view candidates, and cast their votes online.

---

##  Project Overview

The College Online Voting System is designed to replace the traditional paper-based voting process with a digital voting platform.

The system provides separate functionality for:

-  Administrators
-  Registered Students/Voters
-  Candidates

Administrators can manage the election and monitor voting activity, while registered voters can cast their vote electronically.

---

##  Features

###  Admin Features

- Admin login
- Admin dashboard
- View registered users
- View candidates
- Add candidates
- Delete candidates
- Delete eligible users
- Start election
- Stop election
- View voting information
- View election status
- View voting results
- Admin logout

###  Voter Features

- User registration
- User login
- View available candidates
- View candidate information
- Cast vote
- Prevent multiple voting
- View voting status
- Logout

###  Candidate Features

- Candidate registration through admin
- Candidate name
- Department
- Election manifesto
- Candidate listing
- Candidate deletion by admin

---

##  Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web framework |
| MySQL | Database |
| SQLAlchemy | Database ORM |
| PyMySQL | MySQL connection |
| HTML5 | Web page structure |
| CSS3 | Web page styling |
| JavaScript | Frontend functionality |
| Postman | API testing |
| Git | Version control |
| GitHub | Project hosting |

---

##  Project Structure

```text
Online Voting System/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── admin.py
│   ├── user.py
│   ├── candidate.py
│   └── vote.py
│
├── routes/
│   ├── auth.py
│   ├── admin.py
│   ├── candidate.py
│   └── vote.py
│
├── templates/
│   ├── login.html
│   ├── signup.html
│   ├── vote.html
│   └── admin.html
│
├── static/
│   ├── css/
│   └── js/
│
└── venv/
```

> `venv/` is a local Python virtual environment and is not uploaded to GitHub.

---

##  Requirements

Before running the project, install:

- Python 3.x
- MySQL
- MySQL Workbench
- Git
- VS Code

---

##  Installation

### 1. Clone the repository

```bash
git clone https://github.com/saurabhcreates/online-voting-system.git
```

Go inside the project directory:

```bash
cd online-voting-system
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Database Setup

This project uses **MySQL** as the database.

### 1. Open MySQL Workbench

Create the database:

```sql
CREATE DATABASE online_voting_system;
```

### 2. Select the database

```sql
USE online_voting_system;
```

### 3. Configure the database connection

Update the database configuration according to your local MySQL setup.

Example:

```text
mysql+pymysql://USERNAME:PASSWORD@localhost/online_voting_system
```

> Do not upload your real MySQL password or other sensitive credentials to GitHub.

---

##  Running the Application

Activate the virtual environment:

```powershell
venv\Scripts\activate
```

Run the Flask application:

```powershell
python app.py
```

The application should start at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser.

---

##  Application Modules

### Admin

The administrator can:

- Log in
- Manage candidates
- Manage users
- Start/stop elections
- Monitor votes
- View results
- Log out

### Voter

A registered voter can:

- Log in
- View candidates
- Cast a vote
- Vote only once
- Log out

---

##  API Endpoints

The project also contains REST-style API endpoints that can be tested using Postman.

### Authentication

```text
POST /api/login
POST /api/signup
```

### Candidates

```text
GET  /api/candidates
POST /api/candidates
DELETE /api/candidates/<id>
```

### Voting

```text
POST /api/vote
```

### Admin

```text
POST /api/admin/login
POST /api/admin/logout
GET  /api/admin/users
GET  /api/admin/candidates
GET  /api/admin/votes
GET  /api/admin/results
GET  /api/admin/election/status
```

> The exact available endpoints may depend on the routes implemented in the current version of the project.

---

##  API Testing

API requests can be tested using **Postman**.

Example candidate creation request:

```http
POST /api/candidates
```

JSON body:

```json
{
    "name": "Candidate Name",
    "department": "Artificial Intelligence",
    "manifesto": "Better facilities and student welfare"
}
```

Example voting request:

```http
POST /api/vote
```

JSON body:

```json
{
    "candidate_id": 1
}
```

---

##  Voting Security

The system includes functionality to:

- Authenticate users
- Authenticate administrators
- Prevent a user from voting multiple times
- Restrict election management to administrators
- Track voting information
- Control the election status

---

##  Admin Dashboard

The admin dashboard provides information such as:

- Total registered users
- Total candidates
- Total votes
- Registered users
- Candidate information
- Election status
- Voting results

---

##  Screenshots

Screenshots of the application can be added here.

Example:

```text
screenshots/
├── login.png
├── signup.png
├── admin-dashboard.png
├── candidate-list.png
└── voting-page.png
```

You can add screenshots to your GitHub repository and display them in this section later.

---

##  Future Improvements

Possible improvements for future versions include:

- Email verification
- OTP-based authentication
- Improved password security
- Password reset functionality
- Better responsive UI
- Election scheduling
- Detailed result charts
- PDF result generation
- Voter ID verification
- Improved database security
- Deployment to a cloud server
- Role-based access control
- Audit logs
- Improved accessibility

---

##  Learning Objectives

This project helped in understanding:

- Python programming
- Flask web development
- REST APIs
- MySQL database management
- SQLAlchemy ORM
- HTML/CSS/JavaScript
- Authentication
- CRUD operations
- API testing using Postman
- Git and GitHub
- Backend and frontend integration

---

##  Author

**Saurabh**

B.Tech Computer Science with Artificial Intelligence

---

##  License

This project is developed for educational and academic purposes.