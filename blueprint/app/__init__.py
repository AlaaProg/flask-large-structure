import os
from flask import Blueprint, render_template

from blueprint.app import views

app = Blueprint('MainAPP', __name__,

		template_folder=os.path.join(os.getcwd(), 'resources/templates'),
	)




app.add_url_rule("/", view_func=views.index )