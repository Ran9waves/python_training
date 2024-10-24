from flask import Flask, render_template, url_for

app =  Flask(__name__) #equivalent of __main__

@app.route('/') #gives extra tools to decorate the server like user name and the post id in int format
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') #accepts dynamically the name of any page
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    return 'form submitted, epic!'