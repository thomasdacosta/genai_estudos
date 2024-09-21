# -*- coding: utf-8 -*-

import os
import google.generativeai as genai
import xml.etree.ElementTree as et

github_comments = [
	{
    	"text": "Ótimo trabalho na implementação desta feature! O código está limpo e bem documentado. Isso vai ajudar muito nossa produtividade.",
    	"sentiment": ""
	},
	{
    	"text": "Esta mudança quebrou a funcionalidade X. Por favor, reverta o commit imediatamente.",
    	"sentiment": ""
	},
	{
    	"text": "Podemos discutir uma abordagem alternativa para este problema? Acho que a solução atual pode causar problemas de desempenho no futuro.",
    	"sentiment": ""
	},
	{
    	"text": "Obrigado por relatar este bug. Vou investigar e atualizar a issue assim que tiver mais informações.",
    	"sentiment": ""
	},
	{
    	"text": "Este pull request não segue nossas diretrizes de estilo de código. Por favor, revise e faça as correções necessárias.",
    	"sentiment": ""
	},
	{
    	"text": "Excelente ideia! Isso resolve um problema que estávamos enfrentando há semanas. Mal posso esperar para ver isso implementado.",
    	"sentiment": ""
	},
	{
    	"text": "Esta issue está aberta há meses sem nenhum progresso. Podemos considerar fechá-la se não for mais relevante?",
    	"sentiment": ""
	},
	{
    	"text": "O novo recurso está causando conflitos com o módulo Y. Precisamos de uma solução urgente para isso.",
    	"sentiment": ""
	},
	{
    	"text": "Boa captura! Este edge case não tinha sido considerado. Vou adicionar testes para cobrir este cenário.",
    	"sentiment": ""
	},
	{
    	"text": "Não entendo por que estamos priorizando esta feature. Existem problemas mais críticos que deveríamos estar abordando.",
    	"sentiment": ""
	}
]

def call_llm(text):
    print(f"Consultando Gemini... {text}")
    prompt = f"""
                Nossa equipe de atendimento ao cliente está sobrecarregada com feedback não estruturado. Sua tarefa é
                analisar o feedback e categorizar os problemas para nossas equipes de produto e engenharia. Use estas
                categorias: UI/UX, Desempenho, Solicitação de Recurso, Integração, Preços e Outros. Avalie também o
                sentimento (Positivo/Neutro/Negativo) e a prioridade (Alta/Média/Baixa). Aqui está um exemplo:

                <exemplo>
                Texto: O novo painel está uma bagunça! Demora uma eternidade para carregar e não consigo encontrar o botão
                de exportação. Corrijam isso o mais rápido possível!
                Categoria: UI/UX, Desempenho
                Sentimento: Negativo
                Prioridade: Alta
                </exemplo>

                Segue frases que precisam ser analisadas retorne as respostas no formato XML seguindo o seguintes formato de XML
                - Inclua uma tag resposta para englobar o resultado de cada pergunta;
                - Coloque a frase dentro da tag texto;
                - Coloque a categoria dentro da tag categoria;
                - Coloque a sentimento dentro da tag sentimento;
                - Coloque a prioridade dentro da tag prioridade;

                <comentarios>
                    <texto>{text}</texto>
                </comentarios>
            """
    
    genai.configure(api_key=os.environ['API_KEY'])
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
    response = model.generate_content(prompt)

    return response.text

def parse_llm_response(response):
    root = et.fromstring(response.replace("```xml", "").replace("```", ""))
    for child in root:
        if child.tag == "sentimento":
            return child.text
    return "Nenhum"

def analyze_sentiments(comments):
    for comment in comments:
        llm_response = call_llm(comment["text"])
        comment["sentiment"] = parse_llm_response(llm_response)

print("Iniciando processamento...")
analyze_sentiments(github_comments)

# Imprimir resultados
for comment in github_comments:
    print(f"Texto: {comment['text']}")
    print(f"Sentimento: {comment['sentiment']}")
    print("-" * 50)

print("Concluído")