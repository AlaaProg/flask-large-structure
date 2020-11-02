from flask_migrate import Migrate
from application import create_app , db


app = create_app()

Migrate(app, db)

if app.config.get("ENV") != "producation": 	
	@app.after_request
	def add_header(response):

		response.headers['Cache-Control'] = 'no-cache, no-store'
		return response
