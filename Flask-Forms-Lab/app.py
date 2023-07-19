from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina", "razi", "majd"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
		if request.method == 'POST':
			username_var = request.form['username']
			password_var = request.form['password']
		if (password_var == request.form['password'] and username_var == request.form['username']):
			return(redirect(url_for('home')))


@app.route('/home')
def rightinfo():
	return render_template('home.html', friends = facebook_friends)


@app.route('friend_exists/<string:name')
def exist(name):
	return render_template('friend_exists.html', n=name,list=facebook_friends)
	




  	

  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site 
		debug=True
	)