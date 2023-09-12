from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('home.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



#Manual step by step code below for one step dynamic function above

# @app.route('/index.html')
# def my_home2():
#     return render_template('index.html')

# @app.route('/elements.html')
# def blog():
#     return render_template('elements.html')

# @app.route('/generic.html')
# def blog2():
#     return render_template('generic.html')