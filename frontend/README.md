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
git clone https://github.com/your-username/task-management-frontend.git
cd task-management-frontend

```

### 2. Install dependencies

Run the following command to install the core dependencies:

```bash
npm install
or
yarn install
```

### 3. Install Tailwind CSS

Tailwind CSS is used for styling the app. To install and configure it, follow these steps:

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```

Then, update the tailwind.config.js file as follows:

```bash
module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
```

In your src/index.css, add the following Tailwind imports:

```bash
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 4. Install Axios

Axios is used to make HTTP requests to the backend API. To install it, run the following command:

```bash
npm install axios
```

### 5. Install React Router DOM

React Router DOM is used for handling routing in the React application. Install it using:

```bash
npm install react-router-dom
```

### 6. Set up environment variables (optional)

If your backend API runs on a different URL than http://localhost:5000, update the base URL in your API calls within the React components (App.js, EditTask.js, etc.).

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
├── components/ # Reusable components like Loading
|   |-- CreateTask.js # Component for creating new tasks
|   |-- EditTask.js # Component for editing existing tasks
├── App.js # Main app file
├── index.js # Entry point for React
├── App.css # Styling file for the app

```

# Technologies Used

### React.js: For building the frontend UI.

### Axios: For making HTTP requests to the backend API.

### React Router DOM: For navigation between different pages (e.g., home, create, edit).

### Tailwind CSS: For responsive, utility-first styling.

### CSS: For additional custom styling.
