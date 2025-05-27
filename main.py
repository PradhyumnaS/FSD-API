from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

programs = {
    "1": {
        "html": """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Course Registration Form</title>
</head>
<body>
<div style="text-align: center;">
<img src="DeptHeader.png" alt="Department Header" width="65%">
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-direction:
column;">
<h2><u>Course Registration Form for the academic year 2024 - 2025</u></h2>
<form action="#">
<table>
<tr>
<td><label>Student Name:</label></td>
<td><input type="text"></td>
</tr>
<tr>
<td><label>Student USN:</label></td>
<td><input type="text"></td>
</tr>
<tr>
<td><label>Semester:</label></td>
<td><input type="text"></td>
</tr>
<tr>
<td><label>Section:</label></td>
<td><input type="text"></td>
</tr>
<tr>
<td><label>Email:</label></td>
<td><input type="email"></td>
</tr>
<tr>
<td><label>Phone Number:</label></td>
<td><input type="tel"></td>
</tr>
<tr>
<td colspan="2" style="text-align: center; padding-top: 15px;">
<input type="submit" value="Submit" style="width: 280px;">
</td>
</tr>
</table>
</form>
</div>
</body>
</html>
"""
    },
    "2": {
        "html": """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Course Registration Form</title>
</head>
<body>
<div style="text-align: center;">
<img src="DeptHeader.png" alt="Department Header" width="65%">
</div>
<div style="display: flex; justify-content: center; align-items: center; flex-direction:
column;">
<h2><u>Input Validation Course Registration Form</u></h2>
<form action="#">
<table>
<tr>
<td><label>Student Name:</label></td>
<td><input type="text" required></td>
</tr>
<tr>
<td><label>Student USN:</label></td>
<td><input type="text" required></td>
</tr>
<tr>
<td><label>Semester:</label></td>
<td><input type="text" required></td>
</tr>
<tr>
<td><label>Section:</label></td>
<td>
<select required style="width: 170px;" size="3">
<option value="" disabled selected>Select your section</option>
<option value="A">A</option>
<option value="B">B</option>
<option value="C">C</option>
</select>
</td>
</tr>
<tr>
</tr>
<tr>
</tr>
<tr>
<td>
<td><label>Email:</label></td>
<td><input type="email" required></td>
<td><label>Phone Number:</label></td>
<td><input type="tel" required></td>
<td><label>Courses:</label></td>
<select required style="width: 170px;">
<option value="">-- Choose the course --</option>
<option value="BDA">Big Data Analytics</option>
<option value="FSD">Full Stack Development</option>
<option value="SE">Software Engineering</option>
<option value="ST">Software Testing</option>
</td>
</tr>
<tr>
<td>
</td>
</tr>
<tr>
<td><label>Fees Paid:</label></td>
<input type="radio" name="feesPaid" required> Yes
<input type="radio" name="feesPaid" required> No
<td colspan="2" style="padding-top: 15px;">
<div style="display: flex; justify-content: space-between; width: 100%;">
<input type="submit" value="Submit" style="width: 48%;">
<input type="reset" value="Reset" style="width: 48%;">
</div>
</td>
</tr>
</table>
</form>
</div>
</body>
</html>
"""
    },
    "3": {
        "html": """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Profile</title>
<link rel="stylesheet" href="p3.css">
</head>
<body>
<div class="container">
<header class="header">
<img style="text-align:right;" src="/person.png" alt="Profile Picture">
<h1>Ramchandan Y</h1>
<p>Student pursuing Engineering in Information Science at DSCE</p>
</header>
<div class="box education">
<h2>Education</h2>
<p><b>Bachelor of Engineering in Information Science</b></p>
<p>Dayananda Sagar College Of Engineering <br> 2022 - 2026 </p>
</div>
<div class="box skills">
<h2>Skills</h2>
<ul>
<li>Java, Python</li>
<li>HTML, CSS, JavaScript</li>
<li>MYSQL, Tableu</li>
</ul>
</div>
<div class="box projects">
<h2> Projects</h2>
<ul>
<li>
<b>GeoStamp - Intelligent Attendence Management System</b>
<p>Developed Attendance Management using web technology and geolocation
time tracking system</p>
</li>
<li>
<b>Online Movie ticket booking system</b>
<p>Developed movie ticket booking system using HTML, CSS, Javascript along
with Node.js and MongoDB</p>
</li>
</ul>
</div>
<div class=" box Certificate">
<h2>Certificates</h2>
<ul>
</ul>
</div>
</div>
</body>
</html>
<li>Infosys Springboard: Python Fundamentals</li>
<li>Roadmap to GenAI</li>
<li>Automation using Python</li>
P3.css
body {
font-family: 'Arial', sans-serif;
background-color: #f0f4f8;
margin: 0;
padding: 20px;
}
.container {
max-width: 900px;
margin: auto;
background: white;
padding: 30px;
border-radius: 10px;
box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}
.header {
text-align: center;
margin-bottom: 30px;
}
.header img {
width: 120px;
height: 120px;
border-radius: 50%;
border: 3px solid #070707;
margin-bottom: 15px;
}
.header h1 {
margin: 0;
font-size: 2.5em;
}
.header p {
font-size: 1.2em;
}
.box {
background: #e9ecef;
padding: 20px;
margin-top: 20px;
border-radius: 8px;
box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
position: relative;
display: flex;
flex-direction: column;
justify-content: space-between;
}
.box h2 {
margin-top: 0;
font-size: 1.8em;
border-bottom: 2px solid #050505;
padding-bottom: 5px;
}
.box p, .box ul {
margin: 5px 0;
line-height: 1.6;
}
.box ul {
list-style-type: square;
padding-left: 20px;
}
"""
    },
    "4": {
        "html": """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Parent Teacher Meet</title>
<link rel="stylesheet" href="p4.css">
</head>
<body>
<div class="card">
<div class="header">
<h3>DAYANANDA SAGAR COLLEGE OF ENGINEERING</h3>
<p>(An Autonomous Institute affiliated to Visvesvaraya Technological University
(VTU), Belagavi.<br>
Approved by AICTE and UGC, Accredited by NAAC with 'A' grade & ISO 9001-
2015 Certified Institution)</p>
<h4>DEPARTMENT OF INFORMATION SCIENCE & ENGINEERING</h4>
</div>
<div class="logo-container">
<img src="DSCE Logo.jpg" alt="DSCE Logo">
<img src="iiclogo.jpg" alt="IIC Image">
<img src="iqac.jpeg" alt="IQAC Logo">
</div>
<div class="content">
<div class="meeting-box">
1st Year ISE PARENT <br> TEACHERS MEETING
</div>
<div class="illustration">
<img src="meeting.jpeg" alt="Meeting Image">
</div>
<div class="details">
April 12, 2025 | 02:00 PM<br>
<div class="venue">VENUE: ISE - 308</div>
</div>
</div>
<div class="footer">
<div class="footer-grid">
<div>
<div>Dr. Madhura J</div>
<div>Prof. Bharath B C</div>
<div class="desgination">Faculty Coordinators,</div>
<div class="desgination">Dept. of ISE</div>
</div>
<div>
<div>Dr. Annapurna P Patil</div>
<div class="desgination">Dean Academics and</div>
<div class="desgination">HoD of ISE, DSCE</div>
</div>
<div>
<div>Dr. B G Prasad</div>
<div class="desgination">Principal, DSCE</div>
</div>
</div>
</div>
</div>
</body>
</html>
P4.css
body {
font-family: Arial, sans-serif;
display: flex;
justify-content: center;
align-items: center;
min-height: 100vh;
margin: 0;
background-color: #f0f0f0;
padding: 20px;
}
.card {
display: grid;
width: 100%;
max-width: 500px;
border-radius: 10px;
overflow: hidden;
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
background-color: white;
.header {
background-color: #0047ab;
color: white;
text-align: center;
.header p {
font-size: 10px;
}
}
}
.logo-container {
display: flex;
justify-content: space-around;
padding: 8px;
background-color: #f8f8f8;
}
.logo-container img {
height: 50px;
margin: 5px;
}
.content {
padding: 20px;
display: flex;
flex-direction: column;
align-items: center;
gap: 20px;
}
.meeting-box {
background-color: #0047ab;
color: white;
padding: 10px;
font-size: 20px;
font-weight: bold;
border-radius: 8px;
width: 225px;
text-align: center;
line-height: 1.5;
}
.illustration img {
width: 100%;
max-width: 250px;
height: auto;
}
.details {
text-align: center;
font-size: 18px;
font-weight: bold;
color: #0047ab;
}
.venue {
font-size: 16px;
}
.footer {
background-color: #f8f8f8;
padding: 20px;
font-size: 12px;
color: #000000;
border-top: 1px solid #e0e0e0;
}
.footer-grid {
display: grid;
grid-template-columns: repeat(3, 1fr);
gap: 15px;
text-align: center;
font-weight: bold;
}
.desgination{
font-size: 12px;
margin-top: 2px;
font-weight: normal;
}
"""
    },
    "5": {
        "html": """
<!DOCTYPE html>
<html>
<body>
<input id="num" type="number" placeholder="Enter a number">
<button onclick="f()">Factor</button>
<p id="out"></p>
<script>
function f(){
let n=+document.getElementById("num").value,r=[];
for(let i=2;i<=n;i++)while(n%i==0){r.push(i);n/=i}
document.getElementById("out").textContent=r.join(", ")
}
</script>
</body>
</html>
"""
    },
    "6": {
        "html": """
<html>
<body>
<input id="in" placeholder="a1,b2,a10"><button onclick="s()">Sort</button>
<p id="out"></p>
<script>
function s(){
let a=document.getElementById("in").value.split(",");
a.sort((x,y)=>x.localeCompare(y,undefined,{numeric:true}));
document.getElementById("out").textContent=a.join(", ")
}
</script>
</body>
</html>
"""
    },
    "7": {
        "html": """
import React, { useState } from "react";
export default function App() {
const [votes, setVotes] = useState({
Akash: 0,
Dhanush: 0,
Srusthi: 0
});
const [showVotes, setShowVotes] = useState(false);
const handleVote = (candidate) => {
setVotes({ ...votes, [candidate]: votes[candidate] + 1 });
setShowVotes(false); // Hide votes after new vote
};
const getTotalVotes = () => {
return Object.values(votes).reduce((acc, val) => acc + val, 0);
};
return (
<div style={styles.container}>
<h1>Online Voting System</h1>
{Object.keys(votes).map((candidate) => (
<div key={candidate} style={styles.card}>
<h2>{candidate}</h2>
{!showVotes ? (
<p>Votes: </p>
) : (
<p>Votes: {votes[candidate]}</p>
)}
<button onClick={() => handleVote(candidate)} style={styles.button}>
Vote
</button>
</div>
))}
<button onClick={() => setShowVotes(true)} style={styles.viewButton}>
View Votes
</button>
{showVotes && (
<p style={styles.totalVotes}>Total Votes: {getTotalVotes()}</p>
)}
</div>
);
}
const styles = {
container: {
textAlign: "center",
fontFamily: "Arial",
padding: "20px"
},
card: {
margin: "10px auto",
padding: "10px",
border: "1px solid #ccc",
width: "200px",
borderRadius: "8px"
},
button: {
padding: "5px 10px",
fontSize: "16px"
},
viewButton: {
marginTop: "20px",
padding: "8px 16px",
fontSize: "16px",
backgroundColor: "#4CAF50",
color: "white",
border: "none",
borderRadius: "4px",
cursor: "pointer"
},
totalVotes: {
marginTop: "10px",
fontSize: "18px",
fontWeight: "bold"
}
};
"""
    },
    "8": {
        "html": """
import React, { useState } from 'react';
const LoginForm = () => {
const [email, setEmail] = useState('');
const [password, setPassword] = useState('');
const [message, setMessage] = useState('');
const validatePassword = (password) => {
const regex =
/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
return regex.test(password);
};
const handleSubmit = (e) => {
e.preventDefault();
if (!validatePassword(password)) {
setMessage(
and special character.'
);
} else {
'Password must be at least 8 characters long and include uppercase, lowercase, number,
setMessage('Login successful (dummy validation).');
}
};
return (
<div style={{ maxWidth: '400px', margin: '50px auto' }}>
<h2>Login</h2>
<form onSubmit={handleSubmit}>
<div>
<label>Email:</label><br />
<input
type="email"
value={email}
onChange={(e) => setEmail(e.target.value)}
required
/>
</div>
<br />
<div>
<label>Password:</label><br />
<input
type="password"
value={password}
onChange={(e) => setPassword(e.target.value)}
required
/>
</div>
<br />
</form>
</div>
<button type="submit">Login</button>
<p style={{ color: 'red' }}>{message}</p>
);
};
export default LoginForm;
App.jsx
import React from 'react';
import LoginForm from './LoginForm';
function App() {
return (
<div>
<LoginForm />
</div>
);
}
export default App;
"""
    },
    "9": {
        "html": """
const fs = require('fs');
const path = require('path');
function listDirectoryContents(dirPath) {
try {
const items = fs.readdirSync(dirPath);
const result = items.map(item => {
const fullPath = path.join(dirPath, item);
const isDirectory = fs.statSync(fullPath).isDirectory();
return {
name: item,
type: isDirectory ? 'directory' : 'file',
path: fullPath
};
});
console.log(JSON.stringify(result, null, 2));
} catch (err) {
console.error('Error reading directory:', err.message);
}
}
const inputPath = process.argv[2] || '.';
listDirectoryContents(inputPath);
"""
    },
    "10": {
        "html": """
Backend/index.js
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const app = express();
const PORT = 5000;
let users = [];
let results = [];
let quiz = [
{ q: "2 + 2", a: ["3", "4", "5"], correct: "4" },
{ q: "What does RAM stand for? ", a: ["Random Access Monitor", "Random Access
Memory", "Read-Only Memory"], correct: "Random Access Memory" },
{ q: "What do you call the “brain” of the computer?", a: ["CPU", "RAM", "Hard Drive"],
correct: "CPU" },
{ q: "Which of this is a leap year?", a: ["2020", "2021", "2022"], correct: "2020" },
{ q: "Who wrote 'Romeo and Juliet'?", a: ["Charles Dickens", "William Shakespeare",
"Mark Twain"], correct: "William Shakespeare" }
];
app.use(cors());
app.use(bodyParser.json());
app.post('/register', (req, res) => {
const { username, password, isAdmin } = req.body;
if (users.find(u => u.username === username)) return res.status(400).send("User exists");
users.push({ username, password, isAdmin });
res.send("Registered");
});
app.post('/login', (req, res) => {
const { username, password } = req.body;
const user = users.find(u => u.username === username && u.password === password);
if (!user) return res.status(401).send("Invalid");
res.json({ username: user.username, isAdmin: user.isAdmin });
});
app.get('/quiz', (req, res) => res.json(quiz));
app.post('/submit', (req, res) => {
const { username, answers } = req.body;
const score = quiz.reduce((s, q, i) => s + (q.correct === answers[i] ? 1 : 0), 0);
results.push({ username, score });
res.send("Submitted");
});
app.get('/results', (req, res) => res.json(results));
app.listen(PORT, () => console.log(`Server on http://localhost:${PORT}`));
Frontend/App.js
import React, { useState } from 'react';
import './App.css';
const URL = 'http://localhost:5000';
function App() {
const [user, setUser] = useState(null);
const [quiz, setQuiz] = useState([]);
const [answers, setAnswers] = useState([]);
const [results, setResults] = useState([]);
const [showLogin, setShowLogin] = useState(true);
const login = async (e) => {
e.preventDefault();
const data = Object.fromEntries(new FormData(e.target));
const res = await fetch(`${URL}/login`, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify(data),
});
if (res.ok) setUser(await res.json());
else alert('Login failed');
};
const register = async (e) => {
e.preventDefault();
const data = Object.fromEntries(new FormData(e.target));
await fetch(`${URL}/register`, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify(data),
});
alert('Registered, now login');
setShowLogin(true);
};
const startQuiz = async () => {
const res = await fetch(`${URL}/quiz`);
const data = await res.json();
setQuiz(data);
setAnswers(Array(data.length).fill(''));
};
const submitQuiz = async () => {
await fetch(`${URL}/submit`, {
method: 'POST',
headers: { 'Content-Type': 'application/json' },
body: JSON.stringify({ username: user.username, answers }),
});
alert('Submitted!');
setQuiz([]);
};
const loadResults = async () => {
const res = await fetch(`${URL}/results`);
setResults(await res.json());
};
if (!user) return (
<div className="container">
<h2>{showLogin ? 'Login' : 'Register'}</h2>
{showLogin ? (
<form className="form" onSubmit={login}>
<input name="username" placeholder="Username" required />
<input name="password" type="password" placeholder="Password" required />
<button type="submit">Login</button>
<p className="toggle-text">
Don’t have an account? <span className="link" onClick={() =>
setShowLogin(false)}>Register here</span>
</p>
</form>
) : (
<form className="form" onSubmit={register}>
<input name="username" placeholder="Username" required />
<input name="password" type="password" placeholder="Password" required />
<label className="checkbox">
<input type="checkbox" name="isAdmin" /> Register as Admin
</label>
<button type="submit">Register</button>
<p className="toggle-text">
Already have an account? <span className="link" onClick={() =>
setShowLogin(true)}>Login here</span>
</p>
</form>
)}
</div>
);
if (user.isAdmin) return (
<div className="container">
<h1>Admin Dashboard</h1>
<p><strong>Logged in as:</strong> {user.username}</p>
<button className="load-btn" onClick={loadResults}>Load Results</button>
<ul>
{results.map((r, i) => (
<li key={i}><strong>{r.username}</strong>: {r.score}</li>
))}
</ul>
</div>
);
return (
<div className="container">
<h1>Welcome, {user.username}</h1>
{!quiz.length && (
<button className="primary-btn" onClick={startQuiz}>Take Quiz</button>
)}
{quiz.length > 0 && (
<div className="quiz">
{quiz.map((q, i) => (
<div key={i} className="question">
<p>{i + 1}. {q.q}</p>
{q.a.map((opt, j) => (
<label key={j}>
<input
type="radio"
name={`q${i}`}
value={opt}
onChange={() => {
const newAns = [...answers];
newAns[i] = opt;
setAnswers(newAns);
}}
/>
{opt}
</label>
))}
</div>
))}
</div>
<button className="submit-btn" onClick={submitQuiz}>Submit</button>
)}
</div>
);
}
export default App;
"""
    },
    
"course" : {
"html":
"""<!DOCTYPE html>
<html>
<head>
  <style>
    table, td, th { border: 1px solid black; border-collapse: collapse; padding: 5px; }
    th { color: red; }
    td { color: blue; }
    td:hover, th:hover { background-color: lightgray; }
  </style>
</head>
<body>
  <table>
    <tr>
      <th>Sno</th>
      <th>Course</th>
      <th>Subject</th>
      <th colspan="2">Marks</th>
      <th>Category</th>
    </tr>
    <tr>
      <td rowspan="2">1</td>
      <td rowspan="2">BTech(CSE)</td>
      <td>Fun with Game Design</td>
      <td>30</td>
      <td>70</td>
      <td>T</td>
    </tr>
    <tr>
      <td>Fun with Programming</td>
      <td>30</td>
      <td>70</td>
      <td>P</td>
    </tr>
  </table>
</body>
</html>"""
},

"validate": {
"html":
 """<!DOCTYPE html>
<html>
<body>
<script>
function validateRegistration(form) {
  const errors = {};

  if (!form.username || form.username.trim() === "") {
    errors.username = "Username cannot be empty";
  }

  if (!form.password || form.password.length < 6) {
    errors.password = "Password must be at least 6 characters";
  }

  if (form.password !== form.confirmPassword) {
    errors.confirmPassword = "Passwords do not match";
  }

  if (!form.email || !form.email.includes("@")) {
    errors.email = "Invalid email address";
  }

  return errors;
}

// Example usage
const form = {
  username: "",
  password: "abc",
  confirmPassword: "abcd",
  email: "abc.com"
};

console.log(validateRegistration(form));
</script>
</body>
</html>"""
},

"fizzbizz": {
"html" :
"""const arr = [];
for (let i = 1; i <= 100; i++) {
  if (i % 3 === 0 && i % 5 === 0) arr.push("BizzFizz");
  else if (i % 3 === 0) arr.push("Bizz");
  else if (i % 5 === 0) arr.push("Fizz");
  else arr.push(i);
}
console.log(arr);"""
},

"grade": {
"html":
 """const students = [
  { usn: "1BS23023", name: "swachha", grade: 45 },
  { usn: "1BS23028", name: "garathi", grade: 36 },
  { usn: "1BS23024", name: "racket", grade: 42 },
  { usn: "1BS23025", name: "poocha", grade: 35 },
  { usn: "1BS23026", name: "pacchi", grade: 25 },
  { usn: "1BS23029", name: "gathi", grade: 26 },
  { usn: "1BS23030", name: "vidhi", grade: 20 }
];

function rangeOfStudents(data) {
  const count = { "0-20": 0, "21-30": 0, "31-40": 0, "41-50": 0 };
  data.forEach(({ grade }) => {
    if (grade <= 20) count["0-20"]++;
    else if (grade <= 30) count["21-30"]++;
    else if (grade <= 40) count["31-40"]++;
    else count["41-50"]++;
  });
  return count;
}

console.log(rangeOfStudents(students));"""
},

"greeting": {
"html":
"""import React from 'react';
import './styles.css';

function App() {
  const hour = new Date().getHours();
  let greeting = "", color = "";

  if (hour < 12) { greeting = "Good Morning"; color = "green"; }
  else if (hour < 18) { greeting = "Good Afternoon"; color = "blue"; }
  else { greeting = "Good Evening"; color = "red"; }

  return (
    <h1 style={{ color }}>{greeting}</h1>
  );
}

export default App;"""
},  

"issues": {
"html" :
 """import React from 'react';

const issues = [
  {
    title: "Error in Login screen",
    description: "On entry of correct password it displays incorrect password.",
    status: "Closed"
  },
  {
    title: "Server Message 200 On Error",
    description: "Instead of 204 No content, it shows Message 200 Success.",
    status: "Open"
  }
];

function Issue({ title, description, status }) {
  return (
    <div>
      <h3>{title}</h3>
      <p>{description}</p>
      <strong>Status: {status}</strong>
      <hr />
    </div>
  );
}

function App() {
  return (
    <div>
      <h2>Issue Tracker</h2>
      {issues.map((item, index) => (
        <Issue key={index} {...item} />
      ))}
    </div>
  );
}

export default App;"""
},

"card": {
"html": 
"""<!DOCTYPE html>
<html>
<head>
  <style>
    .card {
      border: 2px solid blue;
      padding: 20px;
      background-color: white;
      width: fit-content;
    }
    .header {
      color: blue;
      font-weight: bold;
      font-size: 20px;
    }
    .red-text { color: red; }
    .blue-text { color: blue; }
    .green-text { color: green; }
    .black-text { color: black; }
    .lavender-text { color: lavender; }
    .side-box {
      display: inline-block;
      width: 50px;
      height: 50px;
      vertical-align: top;
    }
    .left { background-color: blue; border: 10px solid black; padding: 20px; }
    .middle { background-color: white; border: 20px solid blue; }
    .right { background-color: red; }
  </style>
</head>
<body>

<div class="side-box left"></div>
<div class="side-box middle card">
  <div class="header">Monday (Blue color Text)</div>
  <p class="red-text">Do these things today! (redcolor text)</p>
  <ul>
    <li class="blue-text">Wash Clothes</li>
    <li class="green-text">Read</li>
    <li class="green-text">Maths Questions</li>
  </ul>
  <p class="black-text">Other items</p>
  <p class="lavender-text">The best preparation for tomorrow is doing your best today</p>
</div>
<div class="side-box right"></div>

</body>
</html>"""
},

"attendance": {
"html" :
 """<!DOCTYPE html>
<html>
<head>
  <title>Attendance</title>
  <style>
    .low { color: red; }
    .mid { color: blue; }
  </style>
</head>
<body>
  <h2>Attendance Table</h2>
  <table border="1" id="attendanceTable">
    <tr><th>Name</th><th>Class Attended</th><th>Percentage</th></tr>
  </table>

  <script>
    const students = [
      { name: "Alice", attended: 28 },
      { name: "Bob", attended: 31 },
      { name: "Charlie", attended: 38 }
    ];

    const totalClasses = 40;
    const table = document.getElementById("attendanceTable");

    students.forEach(student => {
      const percent = (student.attended / totalClasses) * 100;
      const row = table.insertRow();
      const nameCell = row.insertCell(0);
      const attendedCell = row.insertCell(1);
      const percentCell = row.insertCell(2);

      nameCell.textContent = student.name;
      attendedCell.textContent = student.attended;
      percentCell.textContent = percent.toFixed(2) + "%";

      if (percent < 75) row.classList.add("low");
      else if (percent <= 85) row.classList.add("mid");
    });
  </script>
</body>
</html>"""
},

"palindrome" : {
"html" :
 """<!DOCTYPE html>
<html>
<head><title>Palindrome Checker</title></head>
<body>
  <input type="text" id="input" placeholder="Enter string or number">
  <button onclick="checkPalindrome()">Check</button>
  <p id="result"></p>

  <script>
    function checkPalindrome() {
      const input = document.getElementById("input").value;
      const cleaned = input.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
      const reversed = cleaned.split("").reverse().join("");
      document.getElementById("result").innerText = 
        cleaned === reversed ? "Palindrome" : "Not a palindrome";
    }
  </script>
</body>
</html>"""
},

"mountevent" : {
"html" :
"""import React, { useState } from 'react';

function App() {
  const [message, setMessage] = useState("Welcome to Dayananda Sagar!");

  return (
    <div>
      <h1>{message}</h1>
      <button onClick={() => setMessage("The best place to enjoy without time")}>
        Add
      </button>
    </div>
  );
}

export default App;
Express.js Server:
const express = require('express');
const app = express();

app.get('/event', (req, res) => {
  console.log("Teacher taught --- First Message");
  console.log("Student did not listen --- Second Message");
  res.send("Event handled");
});

app.listen(3000, () => {
  console.log("Server listening on PORT 3000");
});"""
},

"poem" : {
"html" : 
 """<!DOCTYPE html>
<html>
<head>
  <title>Poems by Sir Walter Scott</title>
</head>
<body>
  <h1><u>My Native Land</u></h1>
  <p><i>Breathes there the man, with soul so dead,<br>
  Who never to himself hath said,<br>
  This is my own, my native land!</i></p>
  <p>The page should be designed such that:<br>
  (i) The title of the page is "Poems by Sir Walter Scott"<br>
  (ii) "My Native Land" is a heading<br>
  (iii) A line should be displayed in a paragraph<br>
  (iv) The remaining content is in a paragraph<br>
  (v) Poet’s name is in italics</p>
  <p><i>— Sir Walter Scott</i></p>
</body>
</html>"""
},

"invoice" : {
"html" :
 """<!DOCTYPE html>
<html>
<head>
  <style>
    table, td, th { border: 1px solid black; border-collapse: collapse; padding: 5px; }
    th { font-weight: bold; background-color: lightgray; }
    td { padding: 8px; }
  </style>
</head>
<body>
  <table>
    <tr>
      <th colspan="3">Invoice #123456789</th>
      <th colspan="2">14 January 2025</th>
    </tr>
    <tr>
      <td colspan="2">
        <b>Pay to:</b><br>
        Acme Billing Co.<br>123 Main St.<br>Cityville, NA 12345
      </td>
      <td colspan="3">
        <b>Customer:</b><br>
        John Smith<br>321 Willow Way<br>Southeast Northwestereshire, MA 54321
      </td>
    </tr>
    <tr>
      <th>Name / Description</th><th>Qty.</th><th>@</th><th>Cost</th>
    </tr>
    <tr>
      <td>Paperclips</td><td>1000</td><td>0.01</td><td>10.00</td>
    </tr>
    <tr>
      <td>Staples (box)</td><td>100</td><td>1.00</td><td>100.00</td>
    </tr>
    <tr>
      <td colspan="3">Subtotal</td><td>110.00</td>
    </tr>
    <tr>
      <td colspan="3">Tax</td><td>8.80</td>
    </tr>
    <tr>
      <td colspan="3"><b>Grand Total</b></td><td><b>$118.80</b></td>
    </tr>
  </table>
</body>
</html>"""
},

"reverse" : {
"html" :
 """function changeCase(str) {
  return str.split('').map(ch => 
    ch === ch.toUpperCase() ? ch.toLowerCase() : ch.toUpperCase()
  ).join('');
}

// Example
console.log(changeCase("HeLlo")); // hElLO"""
},

"cell" : {
"html" : 
 """<!DOCTYPE html>
<html>
<head>
  <style>
    td { padding: 8px; border: 1px solid black; text-align: center; }
    table { border-collapse: collapse; }
  </style>
</head>
<body>

<table id="table1">
  <tr><th>Num 1</th><th>Num 2</th></tr>
</table>
<br>
<button id="btn1">Add</button>
<br><br>
<div id="display"></div>

<script>
  const table = document.getElementById("table1");
  const btn = document.getElementById("btn1");
  const display = document.getElementById("display");

  btn.addEventListener("click", () => {
    const row = table.insertRow();
    for (let i = 0; i < 2; i++) {
      const cell = row.insertCell();
      const val = Math.floor(Math.random() * 200) + 1;
      cell.textContent = val;

      cell.addEventListener("mouseover", () => {
        cell.style.backgroundColor = val % 2 === 0 ? "green" : "red";
      });

      cell.addEventListener("click", () => {
        display.textContent = "Cell Content: " + val;
      });
    }
  });
</script>

</body>
</html>"""
},

"screenshot" : {
"html" :
"""<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
  <title>Screenshot Generator</title>
</head>
<body>
  <h1>Screenshot Generator</h1>
  <input type="text" id="url" placeholder="Enter URL" />
  <button onclick="captureScreenshot()">Capture</button>
  <br><br>
  <img id="screenshot" style="max-width:100%;" />

  <script>
    async function captureScreenshot() {
      const url = document.getElementById('url').value;
      const response = await fetch('http://localhost:3000/screenshot', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      });
      const blob = await response.blob();
      document.getElementById('screenshot').src = URL.createObjectURL(blob);
    }
  </script>
</body>
</html>
},

“backend.js” :

const express = require('express');
const puppeteer = require('puppeteer');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());

app.post('/screenshot', async (req, res) => {
  const { url } = req.body;
  if (!url) return res.status(400).send('URL is required');

  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'networkidle2' });
  const screenshot = await page.screenshot();
  await browser.close();

  res.set('Content-Type', 'image/png');
  res.send(screenshot);
});

app.listen(port, () => console.log(`Server running on http://localhost:${port}`));"""
},

"indiaflag" : {
"html" :
"""<!DOCTYPE html>
<html>
<head>
  <title>Indian Flag</title>
  <style>
    .flag {
      width: 300px;
      height: 180px;
      border: 1px solid black;
    }
    .saffron, .white, .green {
      height: 33.33%;
      width: 100%;
    }
    .saffron { background-color: #FF9933; }
    .white {
      background-color: white;
      position: relative;
    }
    .green { background-color: #138808; }
    .ashoka-chakra {
      width: 40px;
      height: 40px;
      border: 2px solid navy;
      border-radius: 50%;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
    .spoke {
      position: absolute;
      background: navy;
      width: 1px;
      height: 20px;
      left: 50%;
      top: 50%;
      transform-origin: bottom center;
    }
  </style>
</head>
<body>

  <h2>Indian Flag</h2>
  <div class="flag">
    <div class="saffron"></div>
    <div class="white">
      <div class="ashoka-chakra">
        <!-- 24 spokes -->
        <script>
          for (let i = 0; i < 24; i++) {
            const spoke = document.createElement("div");
            spoke.className = "spoke";
            spoke.style.transform = `rotate(${i * 15}deg) translate(-50%, -50%)`;
            document.querySelector(".ashoka-chakra").appendChild(spoke);
          }
        </script>
      </div>
    </div>
    <div class="green"></div>
  </div>

</body>
</html>"""
},


}

@app.get("/programs/{name}")
def get_program(name: str):
    if name not in programs:
        raise HTTPException(status_code=404, detail="Program not found")
    return programs[name]

@app.get("/help")
def get_help():
    return {
        "message": "Use /programs/{name} to get the HTML content for a specific program.",
        "available_programs": list(programs.keys()),
        "syntax":"npm create vite@latest npm i 7-8",
        "10 program":"npm init -y npm i express cors node index.js",
        "curl": "curl https://fsd-api.onrender.com/programs/1 | jq -r '.html' > index.html && open index.html",
    }

class Prompt(BaseModel):
    prompt: str

genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel("gemini-2.0-flash")

@app.post("/gemini")
def ask_gemini(data: Prompt):
    try:
        response = model.generate_content(data.prompt)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
