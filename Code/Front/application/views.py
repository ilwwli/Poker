from flask import flash, redirect, render_template, \
     request, url_for, session
from application import app
import card
import player
import board
import game

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

card.FullDeck()
board = board.GameBoard()
game = game.Game()
players = []
player_numbers = 4
player_names = ['a','b','c','d']
players = game.set_player_numbers(player_numbers, player_names)
board.ResetBoard()
cardsPerPlayer = int(54 * 2 / len(players))
index = 0
cards = []
for hand in board.Deal(cardsPerPlayer, len(players)):
    players[index].initial_cards(hand)
    index += 1
players[0].cards.sort()
def Cards2StandardCards(cards, num):
    temp = []
    for i in range(num):
        temp.append(str(cards[i].suit + cards[i].rank))
    return temp

cards = Cards2StandardCards(players[0].cards, len(players[0].cards))
print (cards)



# cards = ['h5','da','c5','s8','d5','c4','s8','h4']
options = ['claim', 'follow', 'question', 'pass'] 
# --- Game Page ---
@app.route('/play', methods = ['GET', 'PUT'])
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
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
#@auth.login_required
def get_tasks():
   # return jsonify({'tasks': map(make_public_task, tasks)})
    return render_template('index.html')