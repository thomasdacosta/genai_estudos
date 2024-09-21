# -*- coding: utf-8 -*-

import os
import google.generativeai as genai

def send_to_gemini(prompt):
    print("Consultando Gemini...")
    genai.configure(api_key=os.environ['API_KEY'])

    model = genai.GenerativeModel( 
        model_name='gemini-1.5-flash',
        tools='code_execution')

    response = model.generate_content(prompt)

    return response.text

def create_prompt(role, task, topic, specific_question):
    prompt = f"""
    <prompt>
        <role>{role}</role>
        <task>{task}</task>
        <topic>{topic}</topic>
        <specific_question>{specific_question}</specific_question>
    </prompt>
    """
    return prompt

role = "especialista em filosofia e história da ciência"
task = "explicar o pensamento de Descartes e sua influência para iniciantes em filosofia"
topic = "René Descartes e o Método Cartesiano"
specific_question = "Quem foi René Descartes e qual é o significado da frase 'Penso, logo existo'?"

prompt = create_prompt(role, task, topic, specific_question)
response = send_to_gemini(prompt)
print("\nResposta do Gemini 1.5 Flash:")
print(response)