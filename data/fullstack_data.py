fullstack_data = {
    "title": "Full Stack Development",
    "youtube_playlist": "https://www.youtube.com/playlist?list=PLGLfVvg_OpP_78N6gN-YJqJ0eC8N7hY-A (Traversy Media - MERN Stack Front To Back)\nhttps://www.youtube.com/playlist?list=PL_XvLz_VbQhP2lJbQpLqX0P0qP0qP0qP0 (Simplilearn - Full Stack Web Development Tutorials)\nhttps://www.youtube.com/@TheNetNinja (The Net Ninja - Many specific tutorials on React, Node, Vue, etc.)",
    "topics": [
        {
            "name": "1. Web Fundamentals: How the Internet Works",
            "explanation": "Understanding the basics of client-server architecture, IP addresses, DNS, HTTP/HTTPS protocols, web browsers, and web servers. This is the foundation for full-stack development.",
            "example_code": "Client (Browser) <--- HTTP/HTTPS ---> Server (Web Server)\nDomain Name (e.g., google.com) -- DNS Lookup --> IP Address (e.g., 142.250.190.46)",
            "example_output": "Conceptual flow of a web request and response.",
            "youtube_link": "https://www.youtube.com/watch?v=GEoD_CRk9oA (Traversy Media - How The Internet Works)"
        },
        {
            "name": "2. HTML Structure & Semantics",
            "explanation": "HTML (HyperText Markup Language) defines the structure and meaning of web content. Semantic HTML elements like `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<footer>`, `<aside>` make your page accessible to assistive technologies and improve SEO.",
            "example_code": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <title>My Semantic Page</title>\n</head>\n<body>\n    <header>\n        <h1>Site Title</h1>\n        <nav><a href=\"/\">Home</a></nav>\n    </header>\n    <main>\n        <article>\n            <h2>Article Title</h2>\n            <p>Article content goes here...</p>\n        </article>\n        <aside>\n            <h3>Related Links</h3>\n            <ul><li>...</li></ul>\n        </aside>\n    </main>\n    <footer>\n        <p>&copy; 2025</p>\n    </footer>\n</body>\n</html>",
            "example_output": "Renders a basic, structured web page in a browser.",
            "youtube_link": "https://www.youtube.com/watch?v=UB1O3HWMxR8 (freeCodeCamp.org - HTML Course)"
        },
        {
            "name": "3. CSS Styling & Layout (Box Model, Flexbox, Grid, Responsiveness)",
            "explanation": "CSS (Cascading Style Sheets) controls the visual presentation of HTML. \n- **Box Model:** Every HTML element is a box with content, padding, border, and margin.\n- **Flexbox:** A one-dimensional layout system for distributing space among items in a container, either as a row or a column.\n- **CSS Grid:** A two-dimensional layout system for arranging items in rows and columns simultaneously.\n- **Responsiveness:** Designing web pages to look good and function well on various screen sizes (using media queries, flexible units, and fluid layouts).",
            "example_code": "/* Box Model */\n.card {\n    width: 200px;\n    padding: 15px;\n    border: 1px solid #ccc;\n    margin: 10px;\n}\n\n/* Flexbox */\n.flex-container {\n    display: flex;\n    justify-content: space-around;\n    align-items: center;\n}\n\n/* CSS Grid */\n.grid-layout {\n    display: grid;\n    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));\n    gap: 20px;\n}\n\n/* Media Query for Responsiveness */\n@media (max-width: 600px) {\n    .flex-container {\n        flex-direction: column;\n    }\n}",
            "example_output": "Elements arranged with specific spacing, alignment, and adapting to screen size.",
            "youtube_link": "https://www.youtube.com/watch?v=yfoY53QXios (freeCodeCamp.org - CSS Course)\nhttps://www.youtube.com/watch?v=wm_L7i8Qz-g (Flexbox Crash Course)\nhttps://www.youtube.com/watch?v=GridQxM2y7c (CSS Grid Crash Course)"
        },
        {
            "name": "4. JavaScript Essentials (Variables, Data Types, Control Flow, Functions)",
            "explanation": "JavaScript is the programming language of the web, enabling interactivity. Covers fundamental concepts like declaring variables (`let`, `const`, `var`), common data types (strings, numbers, booleans, arrays, objects), conditional statements (`if/else`), loops (`for`, `while`), and defining/calling functions.",
            "example_code": "let name = 'Bob'; // String\nconst age = 25;   // Number\nlet isActive = true; // Boolean\n\nif (age > 18) {\n    console.log(`${name} is an adult.`);\n} else {\n    console.log(`${name} is a minor.`);\n}\n\nfunction greet(personName) {\n    return `Hello, ${personName}!`;\n}\nconsole.log(greet(name));\n\nfor (let i = 0; i < 3; i++) {\n    console.log(`Loop: ${i}`);\n}",
            "example_output": "Console: Bob is an adult.\nConsole: Hello, Bob!\nConsole: Loop: 0\nConsole: Loop: 1\nConsole: Loop: 2",
            "youtube_link": "https://www.youtube.com/watch?v=W6NZfCO5sPU (freeCodeCamp.org - JavaScript Course)\nhttps://www.youtube.com/watch?v=2RxzN3_i-Dk (Mosh Hamedani - JavaScript Crash Course)"
        },
        {
            "name": "5. JavaScript DOM Manipulation & Event Handling",
            "explanation": "The DOM (Document Object Model) is a programming interface for web documents. It represents the page as a tree structure of objects, allowing JavaScript to modify the content, style, and structure of web pages. Event handling allows JS to respond to user interactions (clicks, keyboard input, form submissions).",
            "example_code": "\n<button id=\"myButton\">Click Me</button>\n<p id=\"displayMessage\">Initial Message</p>\n\n// JavaScript\ndocument.addEventListener('DOMContentLoaded', () => {\n    const button = document.getElementById('myButton');\n    const messageParagraph = document.getElementById('displayMessage');\n\n    button.addEventListener('click', () => {\n        messageParagraph.innerText = 'Button was clicked!';\n        messageParagraph.style.color = 'blue';\n        messageParagraph.style.fontWeight = 'bold';\n    });\n});",
            "example_output": "Initially shows 'Initial Message'. After clicking button, text changes to 'Button was clicked!' in blue, bold font."
        },
        {
            "name": "6. Asynchronous JavaScript (Callbacks, Promises, Async/Await)",
            "explanation": "Asynchronous programming handles operations that might take time (e.g., network requests, file I/O) without blocking the main execution thread. This is crucial for responsive web apps.\n- **Callbacks:** Functions passed as arguments, executed when an async operation completes.\n- **Promises:** Objects representing the eventual completion (or failure) of an async operation and its resulting value. Chainable with `.then()` and `.catch()`.\n- **Async/Await:** Syntactic sugar built on Promises, making async code look and feel more synchronous and readable.",
            "example_code": "// Using Promises\nfunction fetchData() {\n    return new Promise((resolve, reject) => {\n        setTimeout(() => {\n            const success = true;\n            if (success) resolve('Data fetched successfully!');\n            else reject('Failed to fetch data.');\n        }, 1000);\n    });\n}\nfetchData().then(data => console.log(data)).catch(error => console.error(error));\n\n// Using Async/Await\nasync function loadData() {\n    try {\n        console.log('Loading data...');\n        const data = await fetchData();\n        console.log(data);\n    } catch (error) {\n        console.error('Error loading data:', error);\n    }\n}\nloadData();",
            "example_output": "Console: Data fetched successfully! (after 1 second delay)\nConsole: Loading data...\nConsole: Data fetched successfully! (after another 1 second delay)",
            "youtube_link": "https://www.youtube.com/watch?v=PoRJgIXFNNs (Web Dev Simplified - Async JavaScript)"
        },
        {
            "name": "7. Frontend Frameworks: React.js (Basics)",
            "explanation": "React is a JavaScript library for building user interfaces, particularly single-page applications. It emphasizes component-based development (reusable UI pieces) and a declarative approach. Key concepts: JSX, components (functional and class-based), props (data passing), state (component-specific data), lifecycle methods/hooks (e.g., `useState`, `useEffect`).",
            "example_code": "import React, { useState } from 'react';\nimport ReactDOM from 'react-dom/client';\n\nfunction Counter() {\n  const [count, setCount] = useState(0); // State Hook\n\n  return (\n    <div>\n      <p>You clicked {count} times</p>\n      <button onClick={() => setCount(count + 1)}>\n        Click me\n      </button>\n    </div>\n  );\n}\n\nconst root = ReactDOM.createRoot(document.getElementById('root'));\nroot.render(<Counter />);",
            "example_output": "Renders a button and text. Clicking the button increments the displayed count.",
            "youtube_link": "https://www.youtube.com/watch?v=pHwD1K0aPzo (freeCodeCamp.org - React Course)\nhttps://www.youtube.com/watch?v=S3Q_fS-m0O0 (Traversy Media - React JS Crash Course)"
        },
        {
            "name": "8. Backend Development: Node.js & Express.js (Basics)",
            "explanation": "Node.js is a JavaScript runtime built on Chrome's V8 engine, allowing JS to be used for server-side development. Express.js is a minimalist web framework for Node.js, providing a robust set of features for web and mobile applications, including routing, middleware, and API development.",
            "example_code": "// server.js (Node.js/Express.js)\nconst express = require('express');\nconst app = express();\nconst PORT = 3000;\n\napp.get('/', (req, res) => {\n    res.send('Hello from Express.js Backend!');\n});\n\napp.listen(PORT, () => {\n    console.log(`Server running on http://localhost:${PORT}`);\n});\n\n// To run: node server.js (in terminal)",
            "example_output": "Terminal: Server running on http://localhost:3000\nBrowser (visiting http://localhost:3000): Hello from Express.js Backend!",
            "youtube_link": "https://www.youtube.com/watch?v=U8XF6AFGqpQ (freeCodeCamp.org - Node.js and Express.js Course)\nhttps://www.youtube.com/watch?v=gnsS3Yy-D4o (Traversy Media - Node.js Crash Course)"
        },
        {
            "name": "9. RESTful APIs",
            "explanation": "REST (Representational State Transfer) is an architectural style for designing networked applications. RESTful APIs (Application Programming Interfaces) use standard HTTP methods (GET, POST, PUT, DELETE) to perform CRUD (Create, Read, Update, Delete) operations on resources, typically exchanging data in JSON format.",
            "example_code": "// Conceptual API Endpoints for 'users' resource\n// GET /api/users         - Retrieve all users\n// GET /api/users/:id     - Retrieve a single user by ID\n// POST /api/users        - Create a new user\n// PUT /api/users/:id     - Update an existing user by ID\n// DELETE /api/users/:id  - Delete a user by ID\n\n// Example JSON response for GET /api/users\n// [\n//   { \"id\": 1, \"name\": \"Alice\", \"email\": \"alice@example.com\" },\n//   { \"id\": 2, \"name\": \"Bob\", \"email\": \"bob@example.com\" }\n// ]",
            "example_output": "Standardized communication between frontend and backend via HTTP and JSON."
        },
        {
            "name": "10. Database Interaction (SQL vs NoSQL, CRUD Operations)",
            "explanation": "Understanding how to store, retrieve, update, and delete data (CRUD operations) from databases.\n- **SQL (Relational):** Databases like MySQL, PostgreSQL. Data stored in structured tables with relationships, queried using SQL.\n- **NoSQL (Non-relational):** Databases like MongoDB (document-based), Cassandra (column-family). Flexible schemas, good for unstructured/semi-structured data, often highly scalable.",
            "example_code": "\n-- Create Table\nCREATE TABLE products (id INT PRIMARY KEY, name VARCHAR(255), price DECIMAL(10, 2));\n-- Insert Data\nINSERT INTO products (name, price) VALUES ('Laptop', 1200.00);\n-- Select Data\nSELECT * FROM products WHERE price > 1000;\n-- Update Data\nUPDATE products SET price = 1150.00 WHERE name = 'Laptop';\n-- Delete Data\nDELETE FROM products WHERE id = 1;\n\n/* NoSQL (MongoDB Conceptual) */\n// Create (Insert)\ndb.products.insertOne({ name: 'Keyboard', price: 75.00, brand: 'Logitech' });\n// Read (Find)\ndb.products.find({ price: { $lt: 100 } });\n// Update\ndb.products.updateOne({ name: 'Keyboard' }, { $set: { price: 70.00 } });\n// Delete\ndb.products.deleteOne({ name: 'Keyboard' });",
            "example_output": "Conceptual operations showing how data is manipulated in different database types.",
            "youtube_link": "https://www.youtube.com/watch?v=r0R0Yj3_0Jk (Traversy Media - SQL Crash Course)\nhttps://www.youtube.com/watch?v=oc_j0n32N4o (freeCodeCamp.org - MongoDB Crash Course)"
        },
        {
            "name": "11. Authentication & Authorization",
            "explanation": "Essential for secure web applications.\n- **Authentication:** Verifying the identity of a user (e.g., username/password, OAuth, JWT). 'Who are you?'\n- **Authorization:** Determining what a verified user is allowed to do (e.g., access specific resources, perform certain actions based on roles). 'What can you do?'\nCommon methods include session-based authentication (server stores session info) and token-based (e.g., JWT - client holds a token, stateless on server).",
            "example_code": "// Conceptual User Login Flow:\n// 1. Client sends username/password to /api/login (POST).\n// 2. Server verifies credentials.\n// 3. If valid, server generates JWT/session ID and sends it to client.\n// 4. Client stores token/session ID.\n// 5. For protected routes, client sends token/session ID in header.\n// 6. Server verifies token/session ID and checks user's permissions (authorization) before responding.",
            "example_output": "Conceptual flow demonstrating secure user access to an application.",
            "youtube_link": "https://www.youtube.com/watch?v=ezG3B6XhTj0 (Simplilearn - JWT Authentication Tutorial)\nhttps://www.youtube.com/watch?v=2fDEq_y-s24 (Auth0 - Authentication & Authorization Explained)"
        },
        {
            "name": "12. Deployment (Frontend & Backend)",
            "explanation": "The process of getting your full-stack application from your local development environment to a live, publicly accessible server. This involves choosing hosting providers (e.g., Netlify/Vercel for frontend, Heroku/Render/AWS/GCP/Azure for backend), configuring server environments, and potentially setting up CI/CD (Continuous Integration/Continuous Deployment) pipelines.",
            "example_code": "## Frontend Deployment (e.g., React on Netlify):\n# 1. Build your React app: `npm run build`\n# 2. Drag-and-drop the `build` folder to Netlify, or connect Git repo for automatic deploys.\n\n## Backend Deployment (e.g., Flask on Heroku):\n# 1. Create `Procfile` for Heroku: `web: gunicorn app:app`\n# 2. Ensure `requirements.txt` is updated: `pip freeze > requirements.txt`\n# 3. `heroku login`\n# 4. `git init && git add . && git commit -m \"Initial deploy\"`\n# 5. `heroku create your-app-name`\n# 6. `git push heroku main`\n# 7. `heroku run python -m flask shell` (for database migrations)",
            "example_output": "Your web application becomes live and accessible via a URL.",
            "youtube_link": "https://www.youtube.com/watch?v=R2j9G20Q4_8 (Web Dev Simplified - Deploying a React App to Netlify)\nhttps://www.youtube.com/watch?v=F3zW6iFjJ6I (Pretty Printed - Deploying Flask to Heroku)"
        },
        {
            "name": "13. Version Control with Git & GitHub",
            "explanation": "Git is a distributed version control system for tracking changes in source code during software development. GitHub (or GitLab, Bitbucket) is a web-based platform for hosting Git repositories, enabling collaboration, code review, and project management. Essential for any serious development.",
            "example_code": "# Basic Git Workflow:\n# git init                  # Initialize new Git repository\n# git add .                 # Stage all changes\n# git commit -m \"Initial commit\" # Commit staged changes\n# git remote add origin <repo_url> # Link to remote GitHub repo\n# git push -u origin main   # Push changes to GitHub\n# git pull origin main      # Pull latest changes from GitHub\n# git branch <new-branch>   # Create a new branch\n# git checkout <branch-name> # Switch to a branch\n# git merge <branch-name>   # Merge changes from one branch to another",
            "example_output": "Your code history is tracked, allowing easy collaboration, rollback, and feature development on separate branches.",
            "youtube_link": "https://www.youtube.com/watch?v=Uszj_k0DGSE (freeCodeCamp.org - Git & GitHub Crash Course)\nhttps://www.youtube.com/watch?v=RGOj5yH7evk (Traversy Media - Git & GitHub Crash Course)"
        },
        {
            "name": "14. Web Security Fundamentals",
            "explanation": "Understanding common web vulnerabilities and how to mitigate them.\n- **HTTPS:** Encrypts communication between browser and server.\n- **XSS (Cross-Site Scripting):** Injecting malicious client-side scripts.\n- **CSRF (Cross-Site Request Forgery):** Forcing authenticated users to perform unwanted actions.\n- **SQL Injection:** Injecting malicious SQL code into input fields.\n- **Password Hashing:** Storing hashed passwords, not plain text.\n- **Input Validation:** Sanitizing and validating all user inputs.",
            "example_code": "\n\n\n\n\n\n\n# Python example for password hashing (using Werkzeug's security features in Flask)\n# from werkzeug.security import generate_password_hash, check_password_hash\n# hashed_password = generate_password_hash('mysecretpassword')\n# check = check_password_hash(hashed_password, 'mysecretpassword') # True",
            "example_output": "Prevents common attacks, protects user data, and ensures application integrity.",
            "youtube_link": "https://www.youtube.com/watch?v=sO2g4yIeB_w (freeCodeCamp.org - Web Security Basics)\nhttps://www.youtube.com/watch?v=X5gK6216p68 (Fireship - Web Security in 100 Seconds)"
        },
        {
            "name": "15. Introduction to Docker",
            "explanation": "Docker is a platform that uses OS-level virtualization to deliver software in packages called containers. Containers are isolated, lightweight, and portable environments that bundle an application and all its dependencies, ensuring it runs consistently across different environments (development, testing, production).",
            "example_code": "# Simple Dockerfile for a Python Flask app:\n# FROM python:3.9-slim-buster\n# WORKDIR /app\n# COPY requirements.txt .\n# RUN pip install --no-cache-dir -r requirements.txt\n# COPY . .\n# EXPOSE 5000\n# CMD [\"flask\", \"run\", \"--host\", \"0.0.0.0\"]\n\n# Terminal commands:\n# docker build -t my-flask-app .\n# docker run -p 5000:5000 my-flask-app",
            "example_output": "The application runs inside a portable, isolated container.",
            "youtube_link": "https://www.youtube.com/watch?v=fqMsa4E8o4Q (freeCodeCamp.org - Docker Course)\nhttps://www.youtube.com/watch?v=pFAWzNf8Xy0 (Traversy Media - Docker Crash Course)"
        }
    ]
}