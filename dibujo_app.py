
from flask import Flask, escape, request, render_template,url_for
# if we don't want to run in debug mode when using 'flask run', we need to make
# the environment variable debug mode = 0. Do this by typing in the following:
# export FLASK_DEBUG=0
app = Flask(__name__)
from Model import Get

get = Get.Get()
#notebook = get.load_notebook()
notebook = get.group_by('date')

@app.route('/')
@app.route('/home')
def home():
    #name = request.args.get("name", "World")
    
    #return f'<h1>Hello, {escape(name)}!</h1>'
    return render_template('home.html', posts=notebook)

@app.route('/about')
def about():
    return render_template('about.html', title='About')



if __name__ == '__main__':
	app.run(debug=True)