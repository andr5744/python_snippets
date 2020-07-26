from survey import AnonymousSurvey

#Define a question and make a survey
question =  "What language did you first learn to speak?"
language_survey_instance = AnonymousSurvey(question)

#Show question and store responses to the question
language_survey_instance.show_question()
print("Press q at any time to quit: ")
while True:
    specific_response = input("What was your first lanaguage? ")
    if specific_response == 'q':
        break
    language_survey_instance.store_question(specific_response)

#Show the survey results
print("\nThank you for taking the survey. Please see the results: ")
language_survey_instance.print_responses()
