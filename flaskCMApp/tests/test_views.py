import unittest

from app import create_app, getData
from unittest.mock import Mock, patch

class FlaskViewsTestCases(unittest.TestCase):

    def setUp(self):
        '''
        Creates test environment setup
        '''
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.client = self.app.test_client()

    @patch('app.main.views.getData.get_data')
    def test_caselist_200(self, mock_getData):
        '''
        /cases returns a 200 value
        '''
        mock_cases = [
            {
                "id": 1,
                "cmTitle": "Mocked Title",
                "cmDescription": "Mocked Description",
                "cmStatus": "Open",
                "cmDueDate": "2025-05-06T20:30:00Z"
            }
        ]
        mock_getData.return_value = mock_cases
        response = self.client.get('/cases')
        self.assertEqual(response.status_code, 200)
    
    
    @patch('app.main.views.getData.get_data')
    def test_caselist_with_mocked_data(self, mock_getData):
        '''
        /cases uses mocked getData and renders expected content
        '''
        mock_cases = [
            {
                "id": 1,
                "cmTitle": "Mocked Title",
                "cmDescription": "Mocked Description",
                "cmStatus": "Open",
                "cmDueDate": "2025-05-06T20:30:00Z"
            }
        ]
        mock_getData.return_value = mock_cases

        response = self.client.get('/cases')

        self.assertIn("Mocked Title", response.get_data(as_text=True))
