def scan_code(code):

    issues = []

    if "eval(" in code:

        issues.append({
            "severity": "High",
            "issue": "Dangerous eval() detected"
        })

    if "exec(" in code:

        issues.append({
            "severity": "High",
            "issue": "Dangerous exec() detected"
        })

    if "password =" in code:

        issues.append({
            "severity": "Medium",
            "issue": "Hardcoded Password Found"
        })

    if "SELECT * FROM" in code and "+" in code:

        issues.append({
            "severity": "High",
            "issue": "Possible SQL Injection"
        })

    return issues