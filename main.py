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
    "5": {
        "html": """
<!DOCTYPE html>
<html>
<head><title>Prime Factor Calculator</title></head>
<body>
<h1>Prime Factor Calculator</h1>
<input id="n" type="number" placeholder="Enter a number">
<button onclick="calc()">Calculate</button>
<div id="res"></div>
<script>
function calc() {
  let n = +document.getElementById('n').value, res = [], i = 2;
  if (n < 1) return document.getElementById('res').textContent = 'Enter a positive integer';
  while (i * i <= n) {
    if (n % i === 0) res.push(i), n /= i;
    else i++;
  }
  if (n > 1) res.push(n);
  document.getElementById('res').textContent = 'Prime factors: ' + res.join(' × ');
}
</script>
</body>
</html>
"""
    },
}

@app.get("/programs/{name}")
def get_program(name: str):
    if name not in programs:
        raise HTTPException(status_code=404, detail="Program not found")
    return programs[name]

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
