import unittest
from application import create_app , db

class BaseTestCase(unittest.TestCase):
    """This class represents the trivia test case"""


    """This class represents the trivia test case"""
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config={	
        		"SQLALCHEMY_DATABASE_URI": "sqlite:///testing.sqlite3",
        		"TESTING" : True,
        	}
        )

        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():

            # create all tables
            db.create_all()