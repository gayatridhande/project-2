from flask import Flask, render_template, request

app = Flask(__name__)

players = []

@app.route('/')
def index():
    return render_template('index.html', players=players)

@app.route('/add_player', methods=['POST'])
def add_player():
    name = request.form['player_name']
    goals = int(request.form['goals_scored'])
    assists = int(request.form['assists'])
    players.append({'name': name, 'goals': goals, 'assists': assists})
    return index()

if __name__ == '__main__':
    app.run(debug=True)
