from application import create_app 


app = create_app()


if app.config.get("ENV") != "producation": 	
	@app.after_request
	def add_header(response):

		response.headers['Cache-Control'] = 'no-cache, no-store'
		return response
