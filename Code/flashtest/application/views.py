from flask import flash, redirect, render_template, \
     request, url_for
from application import app

app.secret_key = 'daydayup'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != app.secret_key:
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route('/play', methods = ['GET', 'POST'])
def play():
    cards = ['h5','h6','da']    
    for card in cards:
        imagesrc = ("../static/pokerimg/%s.jpg " % card)
        flash(imagesrc,category='cards')
    return render_template('cards.html')