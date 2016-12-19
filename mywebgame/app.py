from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        # The user doesn't have a session ...
        # what should you code do in response?
        return render_template('start.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput') # get data from the post request
    if 'scene' in session:
        if userinput is None:
            # Weird, a POST request to /game with no user input, what should the code do?
            return render_template('try_again.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)

            if nextscene is None:
                # there's no transition for that user input
                # what shoud your code do in response?
                tempvari = render_template('try_again.html')

            else:
                session['scene'] = nextscene.urlname
                tempvari = render_template('show_scene.html', scene=nextscene)

            return tempvari

    else:
        # there's no session, how could the user get here?
        # what should the code do in response?
        return render_template('you_died.html')

# this url initialises the session with starting values
@app.route('/')
def index():
     session['scene'] = map.START.urlname
     return redirect(url_for('game_get')) # redirect the browser to the url to our function: game_get

app.secret_key = "blubb123456789"

if __name__ == "__main__":
    app.run()
