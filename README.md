# 🛡️ CodeSentinel AI

CodeSentinel AI is an AI-powered Python code security analyzer that detects vulnerabilities, bugs, and code quality issues using rule-based scanning and Google Gemini AI. It provides real-time analysis, security scoring, and AI-generated improvement suggestions through an interactive Streamlit dashboard.

---

## 🚀 Features
- Upload Python files for instant analysis  
- Detect security issues like SQL Injection, hardcoded passwords, unsafe functions  
- AI-powered code review using Google Gemini AI  
- Security risk score (0–100)  
- High / Medium risk classification  
- Bug detection and improvement suggestions  
- Interactive Streamlit dashboard  

---

## 🧠 AI Capabilities
- Security vulnerability detection  
- Bug identification  
- Code improvement suggestions  
- Risk level classification  

---

## 🏗️ Project Structure
Code_Sentinel_AI/  
├── app.py  
├── scanner.py  
├── ai_analyzer.py  
├── risk_score.py  
├── database.py  
├── requirements.txt  


---

## ⚙️ Installation & Setup

Clone the repository:
git clone https://github.com/your-username/CodeSentinel-AI.git  
cd CodeSentinel-AI  

Install dependencies:
pip install -r requirements.txt  

Create `.env` file:
GEMINI_API_KEY=your_api_key_here  

Get API key:
https://aistudio.google.com/app/apikey  

Run the project:
python -m streamlit run app.py  

---

## 📊 Example Output

Security Score: 50/100  

High Risk:
- Possible SQL Injection detected  
- Dangerous eval() usage  

Medium Risk:
- Hardcoded password found  

---

## 🛠️ Tech Stack
Python • Streamlit • Google Gemini AI • Pandas • dotenv  

---

## 👨‍💻 Author
Sathya Poojitha  
MCA Graduate | Python Developer   

---

## ⭐ Support
If you like this project, please star the repository ⭐
