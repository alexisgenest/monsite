from flask import Flask, render_template, request, redirect
import os
import csv


app = Flask(__name__)

cwd = os.path.dirname(os.path.abspath(__file__)) # absolute path for this file
my_cvs_dbfile = os.path.join(cwd, 'db', 'database.csv')
my_txt_dbfile = os.path.join(cwd, 'db', 'database.txt')

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open(my_txt_dbfile, mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open(my_cvs_dbfile, newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Oups, something went wrong. Try again!'

