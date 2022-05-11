from flask import Flask, render_template


# create an instance
app = Flask(__name__)

# filters you can use in jinja.  
# safe upper lower capitalize reverse title trim striptags 

# create a route decorator
@app.route("/")
def index():
	first_name = 'JohnPeter'
	stuff = "This is <strong>bold</strong> text."

	favorite_pizza = ["Pepperroni", "Mushroom", "Cheese", 43]

	return render_template('index.html', 
		name=first_name, 
		stuff=stuff, 
		favorite_pizza=favorite_pizza)


# users localhost/user/john.
@app.route('/user/<name>')
def user(name):
	return render_template('user.html', user_name=name)


# create custom error pages
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500

