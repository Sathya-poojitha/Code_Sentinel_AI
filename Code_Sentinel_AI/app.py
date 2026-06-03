import streamlit as st
import pandas as pd

from scanner import scan_code
from database import save_scan
from database import get_scans
from risk_score import calculate_score

# AI Analyzer
try:
    from ai_analyzer import analyze_code
    AI_AVAILABLE = True
except:
    AI_AVAILABLE = False

st.set_page_config(
    page_title="CodeSentinel AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ CodeSentinel AI")
st.write("Upload a Python file and scan for security vulnerabilities.")

uploaded_file = st.file_uploader(
    "Upload Python File",
    type=["py"]
)

if uploaded_file:

    code = uploaded_file.read().decode("utf-8")

    st.subheader("Uploaded Code")

    st.code(code, language="python")

    # Scan Code
    issues = scan_code(code)

    # Security Score
    score = calculate_score(issues)

    st.subheader("Security Score")

    st.metric(
        "Security Score",
        f"{score}/100"
    )

    # Vulnerability Summary
    high_count = sum(
        1 for issue in issues
        if issue["severity"] == "High"
    )

    medium_count = sum(
        1 for issue in issues
        if issue["severity"] == "Medium"
    )

    st.subheader("Vulnerability Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "High Risk",
            high_count
        )

    with col2:
        st.metric(
            "Medium Risk",
            medium_count
        )

    # Chart
    chart_data = pd.DataFrame({
        "Severity": ["High", "Medium"],
        "Count": [high_count, medium_count]
    })

    st.bar_chart(
        chart_data.set_index("Severity")
    )

    # Scan Results
    st.subheader("Scan Results")

    if issues:

        for issue in issues:

            if issue["severity"] == "High":

                st.error(
                    f"{issue['severity']} - {issue['issue']}"
                )

            else:

                st.warning(
                    f"{issue['severity']} - {issue['issue']}"
                )

    else:

        st.success(
            "No security issues found."
        )

    # Recommendations
    st.subheader("Recommendations")

    for issue in issues:

        if "eval" in issue["issue"]:

            st.info(
                "Avoid eval(). Use safer alternatives."
            )

        elif "Password" in issue["issue"]:

            st.info(
                "Store passwords in environment variables."
            )

        elif "SQL" in issue["issue"]:

            st.info(
                "Use parameterized SQL queries."
            )

    # AI Analysis
    st.subheader("AI Analysis")

    if AI_AVAILABLE:

        try:

            analysis = analyze_code(code)

            st.write(analysis)

        except Exception as e:

            st.error(
                f"AI Analyzer Error: {e}"
            )

    else:

        st.warning(
            "AI Analyzer not available."
        )

    # Save Scan
    save_scan(
        uploaded_file.name,
        len(issues)
    )

# History
st.subheader("Scan History")

history = get_scans()

for row in history:

    st.write(
        f"ID: {row[0]} | File: {row[1]} | Issues: {row[2]}"
    )