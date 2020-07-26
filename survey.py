class AnonymousSurvey():
    """Collect anonymous survey information"""

    def __init__(self, question):
        """Store a question and prepare to store responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Print the question givin"""
        print(self.question)

    def store_question(self, new_response):
        self.responses.append(new_response)

    def print_responses(self):
        starting = "Responses so far: "
        for response in self.responses:
            print(starting + " " + response)
