def calculate_score(issues):

    score = 100

    for issue in issues:

        if issue["severity"] == "High":
            score -= 20

        elif issue["severity"] == "Medium":
            score -= 10

    return max(score, 0)