from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    
    greeting = "Welcome to the student-run website for the Trinity College Computer Science Club!"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run(host='10.252.148.28',debug=True)
