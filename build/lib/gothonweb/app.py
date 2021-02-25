from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello', methods=['POST', 'GET'])
def index():

    # how to pass parameter to args - localhost:5000/hello?greet=Hola
    #greet = request.args.get('greet', 'Hello')
    # localhost:5000/hello?name=Will&greet=Hola
    #name = request.args.get('name', 'Nobody')

    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f'{greet}, {name}'
        return render_template('index.html', greeting=greeting)
    else:
        return render_template('hello_form.html')

if __name__ == "__main__":
    app.run()