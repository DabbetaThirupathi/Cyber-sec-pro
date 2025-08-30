from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load verified links
with open("verified_links.json") as f:
    verified_links = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = request.form.get("query", "").strip().lower()
        
        if not user_input:
            result = "⚠️ Please enter a software name or URL."
        else:
            matched = False

            # 🔹 Check if input matches software name (exact or substring)
            for software, link in verified_links.items():
                if software.lower() in user_input or user_input in software.lower():
                    result = f"✅ Verified download link: {link}"
                    matched = True
                    break

            # 🔹 Check if input matches or contains a safe URL
            if not matched:
                for link in verified_links.values():
                    if user_input in link.lower() or link.lower() in user_input:
                        result = f"✅ This link is verified: {user_input}"
                        matched = True
                        break

            # 🔹 If nothing matched
            if not matched:
                result = "❌ Warning: Link not in verified list."
                    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
