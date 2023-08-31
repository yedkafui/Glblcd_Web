from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'
@app.route('/country')
def country():
    return 'Ghana'

def bold(func):
    def wrap():
        wordBold = func()
        return f"<b> {wordBold} </b>"
    return wrap

@app.route('/greet/<name>/<age>')
def hello(name, age):
    return f"Hello {name}. You're {age} years old."

@app.route('/foo/<name>')
def foo(name):
    return render_template('login.html', to=name)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=54677)
    
    