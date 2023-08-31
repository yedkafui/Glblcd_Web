from flask import Flask, render_template
app = Flask(__name__)
@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')





from flask import Flask, request, jsonify

app = Flask(__name__)

# Your dictionary of usernames and passwords
user_credentials = {
    "user1": "password1",
    "user2": "password2",
    # ... add more username-password pairs as needed
}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/validate')
def validate():
    username = request.args.get('username')
    password = request.args.get('password')
    
    if username in user_credentials and user_credentials[username] == password:
        return jsonify({"message": "Login successful."})
    else:
        return jsonify({"message": "Invalid username or password."})

if __name__ == '__main__':
    app.run(debug=True)
