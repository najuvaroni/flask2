from flask import Flask, render_template

app = Flask(__name__)

@app.route("/siteum")
def siteum():
    return render_template('siteum.html')

@app.route("/sitedois")
def sitedois():
    return render_template('sitedois.html')

@app.route("/sitetres")
def sitetres():
    return render_template('sitetres.html')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

