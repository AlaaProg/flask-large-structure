import json
from base_test import BaseTestCase


class AppTestCase(BaseTestCase):
    """This class represents the App test case"""



    def test_server_is_up_and_running(self):
    	
        response = self.client().get("/")

        self.assertEqual(response.status_code, 200)

