from .app import app as main_app 
from .api import api 


def register ( app ):


	app.register_blueprint( main_app, url_perfix='/' )
	app.register_blueprint( api, url_perfix='/api/' )
