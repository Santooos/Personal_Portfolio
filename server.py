from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('home.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline = '', mode='a') as database2:
        name = data["name"]
        email = data["email"]
        # subject = data["subject"]
        message = data["message"]
        
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"',quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to databases'
    else:
        return 'Something went wrong.Try Again !!'



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