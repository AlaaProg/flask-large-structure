import os 

class Config(object):

	APP_NAME   = os.getenv("FLAKS_APP_NAME", "My Server")

	ENV        = os.getenv("FLASK_ENV", "producation")
	SECRET_KEY = os.getenv("FLAKS_SECRET_KEY", os.urandom(16))
	
	# DATABASE 
	DATABASE_URI = os.getenv(
			"FLAKS_DATABASE_URI", 
			'sqlite:///producation.sqlite3'
		);