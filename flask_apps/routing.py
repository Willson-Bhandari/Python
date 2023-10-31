from flask import Flask
from markupsafe import escape
app = Flask(__name__)
app.debug = True

@app.route("/admin/<name>")
def hadmin(name):
    return f" Hello Admin-: {escape(name)}"

@app.route("/guest/")
def hguest():
    return f"Hello , you are in guest."

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
    