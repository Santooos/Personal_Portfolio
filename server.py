from flask import Flask, render_template
app = Flask(__name__)

@app.route('/index.html')
def hello_world():
    return render_template('./index.html')

@app.route('/elements.html')
def blog():
    return render_template('./elements.html')

@app.route('/generic.html')
def blog2():
    return render_template('./generic.html')