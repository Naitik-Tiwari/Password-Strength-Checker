
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check_password():

    data = request.get_json()
    password = data.get("password", "")

    checks = {
        "length": len(password) >= 8,
        "long": len(password) >= 12,
        "upper": bool(re.search(r"[A-Z]", password)),
        "lower": bool(re.search(r"[a-z]", password)),
        "number": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[^A-Za-z0-9]", password))
    }

    score = sum(checks.values())

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    suggestions = []

    if not checks["length"]:
        suggestions.append("Use at least 8 characters")

    if not checks["upper"]:
        suggestions.append("Add an uppercase letter")

    if not checks["lower"]:
        suggestions.append("Add a lowercase letter")

    if not checks["number"]:
        suggestions.append("Add a number")

    if not checks["special"]:
        suggestions.append("Add a special character")

    return jsonify({
        "strength": strength,
        "score": score,
        "checks": checks,
        "suggestions": suggestions
    })


if __name__ == "__main__":
    app.run(debug=True)
