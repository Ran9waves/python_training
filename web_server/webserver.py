from flask import Flask, render_template, url_for

app =  Flask(__name__) #equivalent of __main__

@app.route('/') #gives extra tools to decoraate the server
def hello_world():
    print(url_for('static', filename='meh.ico'))
    return render_template('index.html')

@app.route('/about.html') #gives extra tools to decoraate the server
def about():
    return render_template('about.html')

#@app.route('/favicon.ico') 
#def favicon():
#    return 'Welcome to my cult'

@app.route('/blog/2020/mantis_shrimp') #gives extra tools to decoraate the server
def blog2():
    return 'Best creature ever'