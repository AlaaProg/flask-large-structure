import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()

def create_app(**config:dict) -> Flask :
	"""Create Flask App 
	
		:param config: to update config flask_app  

		Return a Flask App
	"""

	app = Flask(
		__name__,
		template_folder=os.path.join(os.getcwd(), 'public'),
		static_folder=os.path.join(os.getcwd(), 'public/static')
	)

	
	app.config.from_object('application.config.Config')
	app.config.update(**config) 

	
	CORS(
		app, 
		resources={
			r"/api/*": {
				"origins": "*"
			}
		}
	)

	db.init_app(app)

	# blueprint register 
	from blueprint import register

	register( app )

	return app 