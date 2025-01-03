from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import code_library.functions as functions


#API KEY : AIzaSyDju66-JtD42JqKy6Af5jxJGNGU5kBdNlI






app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_lit', methods=['POST'])
def generate_lit():
    data = request.get_json()
    api_key = "AIzaSyDju66-JtD42JqKy6Af5jxJGNGU5kBdNlI"
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.0-flash-exp")

    default_prompt = "Do not use any special characters like asterisks, unless explicitly asked, as it is asked in this prompt for a reason. Your goal is to generate ideas of stories for people who are looking for inspiration, and you need to give them something they could use to start with. Your reponse should have 4 paragraphs, first is Core Concept Development, second is Character Creation, third is Setting and Context, and fourth is Plot and Conflict. Use a single hashtag to separate the paragraphs. Do use a colon after each heading. DIRECTLY START YOUR RESPONSE WITH CORE CONCEPT DEVELOPMENT without any prior message. Try to give an example character to help the user out. You may select a random genre IF USER DOES NOT SPECIFY. If user has given his insights, this is what it is : "

    user_query = data.get('user')
    new_query = functions.query_formatting(default_prompt, user_query)
    generated_text = functions.generate_text(new_query, model)
    separated_text = generated_text.split("#")

    
    return jsonify({'core': separated_text[0], 'character': separated_text[1], 'setting': separated_text[2], 'plot': separated_text[3]})



if __name__ == '__main__':
    app.run(debug=True)

