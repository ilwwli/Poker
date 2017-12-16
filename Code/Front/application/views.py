from flask import flash, redirect, render_template, \
     request, url_for, session
from application import APP, GAME
# import card
# import player
# import board
# import game

APP.user = {'admin':'admin',
            'player1':'player1', 'player2':'player2',
            'player3':'player3', 'player5':'player5'}

# --- Login Page ---
@APP.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] not in APP.user or \
                request.form['password']  != APP.user[request.form['username']]:
            error = 'Invalid User'
        elif request.form['username'] == 'admin':
            flash('You were successfully logged in', category='error')
            session['username'] = request.form['username']
            return redirect(url_for('config'))
        else:
            flash('You were successfully logged in', category='error')
            session['username'] = request.form['username']
            return redirect(url_for('play'))
    return render_template('login.html', error=error)

@APP.route('/config', methods=['GET', 'POST'])
def config():
    return redirect(url_for('play'))



cards = ['h5','da','c5','s8','d5','c4','s8','h4']
options = ['claim', 'follow', 'question', 'pass']
# --- Game Page ---
@APP.route('/play', methods=['GET', 'POST'])
def play():
    if 'username' not in session:
            flash('Skip Login Error', category='error')
            return redirect(url_for('login'))
    else:
        alpha = request.args.get('Cards')
        beta = request.args.get('Option')
        if alpha:
            alpha = alpha.split(',')
            print(alpha)
            for card in alpha[:-1]:
                if card in cards:
                    cards.remove(card)
        if beta:
            flash("your last choice is %s" % beta, category='error')
        for card in cards:
            imagesrc = [card, "../static/pokerimg/%s.jpg " % card]
            flash(imagesrc, category='cards')
        for op in options:
            flash(op, category='options')
        return render_template('cards.html')

# --- Home Page ---
@APP.route('/', methods=['GET'])
@APP.route('/index', methods=['GET'])
#@auth.login_required
def get_tasks():
   # return jsonify({'tasks': map(make_public_task, tasks)})
    return render_template('index.html')