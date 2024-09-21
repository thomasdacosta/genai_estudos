# -*- coding: utf-8 -*-

import os
import ollama
import google.generativeai as genai
from groq import Groq

# export API_KEY=<>
# pip install -q -U google-generativeai
def run_gemini(prompt):
    print("Consultando Gemini...")
    genai.configure(api_key=os.environ['API_KEY'])

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        tools='code_execution')

    response = model.generate_content((prompt))

    return response.text

# pip install groq
# export GROQ_API_KEY=<>
def run_groq(prompt):
    print("Consultando Groq...")
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

# pip install ollama
def run_ollama(prompt):
    print("Consultando Ollama...")
    response = ollama.chat(model='qwen2:1.5b', messages=[
    {
        'role': 'user',
        'content': prompt,
    },
    ])

    return response['message']['content']

def format_prompt(job_description):
    ret  =  f""" Você é um assistente inteligente que ajuda a analisar descrições de emprego. 
                Considere a seguinte descrição:\n\n{job_description}\n\n
                Extraia as informações estruturadas: Nome do Cargo, Horas de Trabalho, Pais e Habilidades Técnicas.
            """
    return ret

def query_all_models(formatted_prompt):
    return { "gemini" : run_gemini(formatted_prompt), 
            "groq" : run_groq(formatted_prompt),
             "ollama" : run_ollama(formatted_prompt) }

def main():
    print("Iniciando aplicação...")
    with open("job_description.txt", "r") as file:
        job_description = file.read()
        formatted_prompt = format_prompt(job_description)
        results = query_all_models(formatted_prompt)
        for model, response in results.items():
            print(f"\n############### Análise do {model}: ###############")
            print(response)
            print("-" * 50)

if __name__ == "__main__":
    main()
