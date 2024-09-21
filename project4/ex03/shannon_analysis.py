import os
import google.generativeai as genai
from dotenv import load_dotenv

# pip install python-dotenv
def get_api_keys():
    load_dotenv()

def run_gemini(user_prompt):
    genai.configure(api_key=os.environ['API_KEY'])

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash')

    response = model.generate_content(user_prompt)
    return response.text

result = ""
prompts = [
    "Quem foi Claude Shannon, qual foi sua trajetória acadêmica e profissional",
    """
        De acordo com as informações obtidas da sua trajetória acadêmica e profissional informado a seguir: 
            <resposta>
                <![CDATA[##resposta]]
            <resposta>. 
            Analisar suas principais contribuições para a teoria da informação""",
    """
        De acordo com as informações obtidas de suas principais contribuições para a teoria da informação 
            <resposta>
                <![CDATA[##resposta]]
            <resposta>. 
            Explorar o impacto de seu trabalho na computação moderna e nas tecnologias de comunicação.""",
    """ 
        Sintetizar as informações obtidas de acordo com o resultado abaixo:
        <respostas>
            <trajetoria><![CDATA[##trajetoria]]</trajetoria>
            <contribuicoes><![CDATA[##contribuicoes]]</contribuicoes>
            <impacto><![CDATA[##impacto]]</impacto>
        </respostas>
    """
]

respostas = []

get_api_keys()

def show_resp():
    for resp in respostas:
        print("-" * 50)
        print(resp)
        print("-" * 50)
        input()

def run_prompt_chain():
    i = 0
    print(len(prompts))

    for prompt in prompts:
        if i == len(prompts)-1:
            prompt = prompt.replace("##trajetoria", respostas[0])
            prompt = prompt.replace("##contribuicoes", respostas[1])
            prompt = prompt.replace("##impacto", respostas[2])

        resposta = run_gemini(prompt)
        respostas.append(resposta)

        if (i+1) < len(prompts):
            prompts[i+1] = prompts[i+1].replace("#resposta", resposta)

        i += 1

if __name__ == "__main__":
    print("Iniciando...")
    run_prompt_chain()
    show_resp()
    print("Concluído")
