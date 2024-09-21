import os
import google.generativeai as genai
from groq import Groq
from dotenv import load_dotenv

# pip install python-dotenv
def get_api_keys():
    load_dotenv()

def run_groq(system_prompt, user_prompt):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],        
        # messages=[
        #     {
        #         "role": "user",
        #         "content": prompt,
        #     }
        # ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

def run_gemini(system_prompt, user_prompt):
    genai.configure(api_key=os.environ['API_KEY'])

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=system_prompt)

    response = model.generate_content(user_prompt)
    return response.text

roles = {
    "Educador tradicional": "Você é um educador tradicional com anos de experiência em universidades convencionais. Analise a École 42 de uma perspectiva acadêmica.",
    "Estudante de tecnologia": "Você é um estudante de tecnologia ansioso para aprender programação. Analise a École 42 do ponto de vista de um potencial aluno.",
    "Recrutador de tecnologia": "Você é um recrutador de profissionais de uma grande empresa de tecnologia. Avalie a École 42 considerando as habilidades que você busca em candidatos."
}

user_prompt = "Descreva a École 42 e seu método de ensino. Destaque os pontos principais que seriam relevantes para sua perspectiva."

def role_analysis_gemini():
    for role, system_prompt in roles.items():
        prompt = f"""
                    {system_prompt}
                """
        print("=== Análises usando GEMINI ===")
        print(f"--- Analise da perspectiva de {role} ---")
        print("École 42: " + run_gemini(role, prompt))
        print()


def role_analysis_groq():
    for role, system_prompt in roles.items():
        prompt = f"""
                    {system_prompt}
                    Inclua o resultado em somente uma única linha
                """
        print("=== Análises usando LLAMA ===")
        print(f"--- Analise da perspectiva de {role} ---")
        print("École 42: " + run_groq(role, prompt))
        print()

get_api_keys()
role_analysis_gemini()
role_analysis_groq()