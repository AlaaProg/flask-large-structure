import os
from flask import Blueprint, render_template


app = Blueprint('MainAPP', __name__,
		template_folder=os.path.join(os.getcwd(), 'resources/templates')
	);



@app.route("/")
def index():

	return render_template("home.html")