# Task Management Frontend

This is a simple task management frontend built with **React.js**. It allows users to create, read, update, and delete (CRUD) tasks via interaction with a RESTful API.

## Features

- View all tasks.
- Create new tasks.
- Edit existing tasks.
- Delete tasks.
- Search for tasks by ID or keyword.
- Sort tasks by date (ascending/descending).

# Frontend

## Prerequisites

Before running this project, ensure that you have the following installed:

- **Node.js** (v14 or above)
- **npm** or **yarn**

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/amanakhtar78/TO-DO-LIST-PYTHON.git
cd frontend

```

### 2. Install dependencies

Run the following command to install the core dependencies:

```bash
npm install
or
yarn install
```
### 7. Run the development server

To start the app in development mode, use:

```bash
npm start
or
yarn start
```

This will start the application at http://localhost:3000.

Project Structure

```bash
src/
├── components/ 
|   |-- CreateTask.js 
|   |-- EditTask.js 
├── App.js 
├── index.js
├── App.css 

```

# Technologies Used

### React.js:

For building the frontend UI.

### Axios:

For making HTTP requests to the backend API.

### React Router DOM:

For navigation between different pages (e.g., home, create, edit).

### Tailwind CSS:

For responsive, utility-first styling.

### CSS:

For additional custom styling.

# BACKEND

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
# or
venv\Scripts\activate      # On Windows
```

### 2. Install dependencies
   Install all required Python packages:

```bash
pip install -r requirements.txt
```

Dependencies include:

Flask: Core web framework
Flask-CORS: Handling Cross-Origin Resource Sharing (CORS)
Flasgger: For Swagger API documentation
SQLite: For the lightweight database


### 3. Running the application

```bash
cd backend
python app.py
```
The application will start running on http://localhost:5000.

Application Structure

```bash
task-management-backend/
  ├── app/
      ├── db.py              
      ├── __init__.py        
      ├── tasks.py           
      ├── schema.sql         
  ├── instance/
  |   |-- task_manager.db    
  ├── run.py                 
  └── requirements.txt
  |-- backend/swagger.json

```
## API SWAGGER DOCUMENT 

```bash
http://localhost:5000/apidocs/
```

# API Endpoints

### GET /api/tasks/

Retrieve a list of all tasks.

Response:
200 OK: Returns a JSON array of tasks.
POST /api/tasks/
Create a new task.

Request: JSON body with title and description.
Response:
201 Created: Returns the task ID and success message.
400 Bad Request: If title or description is missing.

### GET /api/tasks/<int:id>

Retrieve a single task by its ID.

Response:
200 OK: Returns the task as JSON.
404 Not Found: If the task does not exist.

### PUT /api/tasks/<int:id>

Update an existing task.

Request: JSON body with updated title and description.
Response:
200 OK: Returns success message.
400 Bad Request: If title or description is missing.

### DELETE /api/tasks/<int:id>

Delete a task by its ID.

Response:
200 OK: Returns success message.
404 Not Found: If the task does not exist.
