from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

def analyze_code(code):

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=f"""
You are a senior software security expert.

Analyze this Python code:

1. Security issues
2. Bugs
3. Improvements

Code:
{code}
"""
    )

    return response.text