from flask import Flask, request, render_template_string

app = Flask(__name__)

# Simple HTML template for the web UI
HTML = """
<!DOCTYPE html>
<html>
<head><title>Web Vulnerability Scanner</title></head>
<body>
  <h1>Web Vulnerability Scanner</h1>
  <form method="POST">
    URL to scan: <input type="text" name="url" size="50" required>
    <input type="submit" value="Scan">
  </form>
  {% if result %}
  <h2>Scan Result</h2>
  <pre>{{ result }}</pre>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        url = request.form.get("url")
        # Simple message to show scanned URL
        result = f"Scan started for: {url}\n(Scan logic will be implemented here)"
    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
