from flask import flash, redirect, render_template, \
     request, url_for, session
from application import app

app.user_name = "admin"
app.secret_key = "admin"

# --- Login Page ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.user_name or \
                request.form['password']  != app.secret_key:
            error = 'Invalid User'            
        else:
            flash('You were successfully logged in', category='error')
            session['username'] = request.form['username']
            return redirect(url_for('play'))
    return render_template('login.html', error=error)

cards = ['h5','da','h5','h8','wangsmall','d4','s8','d4'] 
# --- Game Page ---
@app.route('/play', methods = ['GET', 'PUT'])
def play():
    if 'username' not in session:
            flash('Skip Login Error', category='error')        
            return redirect(url_for('login'))
    else:
        if request.method == 'PUT':            
            flash('Submit Got', category='error')
            cards.pop()
            for card in cards:
                imagesrc = [card, "../static/pokerimg/%s.jpg " % card]
                flash(imagesrc, category='cards')
            return render_template('cards.html')
        else:
            for card in cards:
                imagesrc = [card, "../static/pokerimg/%s.jpg " % card]
                flash(imagesrc, category='cards')
            return render_template('cards.html')

# --- Home Page ---
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
#@auth.login_required
def get_tasks():
   # return jsonify({'tasks': map(make_public_task, tasks)})
    return render_template('index.html')