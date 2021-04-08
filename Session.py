from flask import Flask, request, session, render_template, redirect, url_for

app = Flask(__name__)
app.secret_key = 'srm123'

@app.route('/')
def index():
    if 'usr' in session:
        return 'Welcome - ' + session['usr']

    else:
        return """Click here <br /> <a href='/login'>Login</a>"""

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session['usr'] = request.form['nm']
        return redirect(url_for('index'))
    else:
        return (render_template('session.html'))  

@app.route('/logout', methods=['GET'])
def logout():
        session.pop('usr')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()