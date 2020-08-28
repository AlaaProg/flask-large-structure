from flask import Flask 


def create_app(**config:dict) -> Flask :
	"""Create Flask App 
	
		:param config: to update config flask_app  

		Return a Flask App
	"""

	app = Flask(
		__name__,
		template_folder='public/',
		static_folder='public/static'
	)

	app.config.from_object('config.Config')
	app.config.update(**config) 

	

	# blueprint register 
	from blueprint import register

	register( app )


	return app 