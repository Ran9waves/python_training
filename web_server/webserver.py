from flask import Flask, render_template, url_for, request, redirect
import csv

app =  Flask(__name__) #equivalent of __main__

@app.route('/') #gives extra tools to decorate the server like user name and the post id in int format
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') #accepts dynamically the name of any page
def html_page(page_name):
    return render_template(page_name)

#def write_to_txt_file(data):
#    with open('database.txt', mode='a') as database:
#        email = data['email']
#        subject = data['subject']
#        message = data['message']
#        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(email, subject, message)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #turns the form data into a dictionary
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'Something went wrong. Try again!'