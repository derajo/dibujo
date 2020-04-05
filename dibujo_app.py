
from flask import Flask, escape, request
# if we don't want to run in debug mode when using 'flask run', we need to make
# the environment variable debug mode = 0. Do this by typing in the following:
# export FLASK_DEBUG=0


app = Flask(__name__)

@app.route('/')
def home():
    #name = request.args.get("name", "World")
    
    #return f'<h1>Hello, {escape(name)}!</h1>'
    return '<h2>Welcome to dibujo</h2>'

@app.route('/about')
def about():
    return '<h2>About Page</h2>'



if __name__ == '__main__':
	app.run(debug=True)