from flask import *

# when the Falsk is initialized without 2nd param for template path, it defaults looks for template in ./templates folder!
app = Flask(__name__)
app.secret_key = "abc"


@app.route('/')
def home():
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")
    session['response'] = 'session#1'
    return res;


@app.route('/get')
def getVariable():
    if 'response' in session:
        s = session['response'];
        return render_template('getsessions.html', name=s)


if __name__ == '__main__':
    app.run(debug=True)