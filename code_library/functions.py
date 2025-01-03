import google.generativeai as genai


def generate_text(query, model):

    respone = model.generate_content(query)
    return respone.text

def get_input_query():
    anything_in_mind = (input("Do you have anything in mind for writing? Any specific genres? (y/n) : ")).lower()
    what_user_has_to_offer = "This is what user has to offer : "

    whats_in_mind = ""
    if anything_in_mind == 'y':
        whats_in_mind = input("Shoot anything you want! : ")

        return what_user_has_to_offer + whats_in_mind
    
    if anything_in_mind == 'n':
        print("No problem! Guess someone is going to select a random genre for you!")
        return what_user_has_to_offer + "Select a random genre for me!"
    
    

def query_formatting(default_query, user_query):
    return default_query + user_query
    

