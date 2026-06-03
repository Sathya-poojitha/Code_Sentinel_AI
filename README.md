# 🛡️ CodeSentinel AI

### AI-Powered Python Code Security Analyzer

CodeSentinel AI is an intelligent security analysis tool that scans Python code for vulnerabilities, bugs, and performance issues using rule-based detection and Google Gemini AI. It provides real-time analysis, risk scoring, and structured AI-generated reports through an interactive Streamlit dashboard.

---

## 🚀 Features

- 📂 Upload and analyze Python files instantly  
- 🔐 Detect security issues like SQL Injection, hardcoded passwords, and unsafe functions  
- 🧠 AI-powered code review using Google Gemini API  
- 📊 Security risk scoring system (0–100)  
- ⚠️ Categorized vulnerability detection (High / Medium / Low)  
- 📈 Interactive Streamlit dashboard  
- 🧾 Structured AI analysis output  
- 💡 Actionable recommendations for code improvement  

---

## 🧠 AI Capabilities

Uses Google Gemini AI to perform deep code analysis:

- Security vulnerability detection  
- Bug identification  
- Code quality improvements  
- Risk level classification  

---

## 🏗️ Project Structure
Code_Sentinel_AI/
│
├── app.py # Streamlit frontend
├── scanner.py # Rule-based vulnerability scanner
├── ai_analyzer.py # Gemini AI integration
├── risk_score.py # Security score calculation
├── database.py # Scan history storage
├── requirements.txt # Dependencies

---

## ⚙️ Installation & Setup


### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/CodeSentinel-AI.git
cd CodeSentinel-AI

2️⃣ Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Add API Key

Create a .env file in the root folder:

GEMINI_API_KEY=your_api_key_here

👉 Get API key from:
https://aistudio.google.com/app/apikey

5️⃣ Run the project
python -m streamlit run app.py

📊 Example Output
Security Score: 50/100

High Risk:
- Possible SQL Injection detected
- Dangerous eval() usage

Medium Risk:
- Hardcoded password found

🔥 AI Analysis Sample
{
  "security_issues": ["SQL Injection risk"],
  "bugs": ["Unsafe input concatenation"],
  "improvements": ["Use parameterized queries"],
  "risk_level": "High"
}

🛠️ Tech Stack
Python 🐍
Streamlit 🌐
Google Gemini AI 🤖
Pandas 📊
dotenv 🔐

🎯 Future Enhancements
PDF report generation
GitHub repository scanning
Authentication system
CI/CD integration
Multi-language support

👨‍💻 Author

Sathya Poojitha
MCA Graduate | Python Developer 

⭐ Support

If you like this project:

⭐ Star this repository
🍴 Fork it
🛠️ Contribute improvements
