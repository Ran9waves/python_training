from flask import Flask, render_template, url_for

app =  Flask(__name__) #equivalent of __main__

@app.route('/') #gives extra tools to decorate the server like user name and the post id in int format
def my_home():
    return render_template('index.html')

@app.route('/about.html') #gives extra tools to decoraate the server
def about():
    return render_template('about.html')


@app.route('/blog/2020/mantis_shrimp') #gives extra tools to decoraate the server
def blog2():
    return 'Best creature ever'