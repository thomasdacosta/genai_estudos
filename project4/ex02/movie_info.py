import os
import ast
import google.generativeai as genai
from dotenv import load_dotenv

# pip install python-dotenv
def get_api_keys():
    load_dotenv()

def run_gemini(system_prompt, user_prompt):
    genai.configure(api_key=os.environ['API_KEY'])

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=system_prompt)

    response = model.generate_content(user_prompt)
    return response.text.replace("```json", "").replace("```", "")

def get_movie_info(movie_title):
    user_prompt = f"""
        Provide information about the movie "{movie_title}" in JSON format. 
        Start your response:
        {{
            "title": "{movie_title}",
        }}

        If the film does not exist and has no further information, start your response with:
        {{}}
        """
    
    system_prompt = """ {
                        "title": "Movie Title",
                        "year": 0000,
                        "director": "Director's Name",
                        "genre": ["Genre1", "Genre2"],
                        "plot_summary": "Brief plot summary"
                    } """
    
    return run_gemini(system_prompt, user_prompt)

movie_titles = ["The Matrix", "Inception", "Pulp Fiction", "The Shawshank Redemption", "The Godfather", "Bla"]

get_api_keys()

for title in movie_titles:
    print(f"\nAnalyzing: {title}")
    result = ast.literal_eval(get_movie_info(title))

    if result:
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print("Filme não existe")
    
    print("-" * 50)
