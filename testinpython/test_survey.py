import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests the class"""
    
    def setUp(self):
        """Create a survey and set of responses to use in all test cases"""
        question = "What was your first langauge? "
        self.my_survey = AnonymousSurvey(question)
        self.my_responses = ['English', 'Spanish', 'Malayalam']

    def test_store_single_response(self):
        """Test to see if a single response is stored correctly"""
        self.my_survey.store_question(self.my_responses[0])
        self.assertIn(self.my_responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test to see if three responses is stored correctly"""
        for response in self.my_responses:
            self.my_survey.store_question(response)
        for response in self.my_responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
