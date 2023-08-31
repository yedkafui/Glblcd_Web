from flask import Flask, request,  jsonify, render_template
app = Flask(__name__)
user_data = {
    'josyed' : 'josyed1',
    'eseyed' : 'eseyed',
    'makyed' : 'makyed',
    'helyed' : 2333,
    'exornam' : 'you@me'
}


@app.route('/')
def index():
     
     return render_template('index.html')


@app.route('/validate')
def validate():
    username = request.args.get('username')
    password = request.args.get('password')

    

    if username in user_data and user_data[username] == password:
        return jsonify({"message":"Login successful"})
    else:
        return jsonify({"message":"Invalid login."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=4446)


