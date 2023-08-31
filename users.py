from flask import Flask, request,  jsonify
app = Flask(__name__)
user_data = {
    'josyed' : 'josyed1',
    'eseyed' : 'eseyed',
    'makyed' : 'makyed',
    'helyed' : 2333,
}


@app.route('/')
def index():
    app.send_static_file('login.html')


@app.route('/validate')
def validate():
    username = request.args.get('username')
    password = request.args.get('password')

    if username in user_data and user_data[username] == password:
        return jsonify({"message":"Login successful"})
    else:
        return jsonify({"message":"Invalid login."})

