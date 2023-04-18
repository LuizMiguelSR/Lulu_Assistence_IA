from dotenv import load_dotenv
import os
import openai
import pyttsx3
import re
import random

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define as credenciais da API do OpenAI a partir da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

# Cria o objeto de conversão de texto em fala
engine = pyttsx3.init()

# Função para obter resposta do GPT-3
def obter_resposta(pergunta):
    # Define o modelo a ser usado pelo GPT-3
    modelo = "text-davinci-002"

    # Define o prompt de entrada com a pergunta do usuário
    prompt = f"Q: {pergunta}\nA:"

    # Gera a resposta usando a API do OpenAI
    resposta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Obtém a resposta gerada pelo GPT-3
    resposta = resposta.choices[0].text.strip()

    return resposta

# Loop principal do programa
while True:
    # Recebe a pergunta do usuário
    pergunta = input("Pergunta: ")

    # Verifica se o usuário digitou a palavra-chave para sair
    if pergunta.lower() == "sair":
        break

    if pergunta == "Quem te criou?":
        # Gera uma mensagem motivacional usando a API do OpenAI
        criacao = obter_resposta("Quem me criou foi o Luiz Miguel, utilizando a inteligência artificial do chat gpt 3 'em português'")

        # Converte a mensagem em fala e reproduz o áudio
        print(criacao)
        # Converte a mensagem em fala e reproduz o áudio
        engine.say(criacao)
        engine.runAndWait()

    elif pergunta == "motiva":
        # Gera uma mensagem motivacional usando a API do OpenAI
        mensagem_motivacional = obter_resposta("Gerar mensagem motivacional 'em português'")

        # Converte a mensagem em fala e reproduz o áudio
        print(mensagem_motivacional)
        # Converte a mensagem em fala e reproduz o áudio
        engine.say(mensagem_motivacional)
        engine.runAndWait()
        # Verifica se a pergunta começa com "dado"
    elif pergunta.startswith("dado"):
        # Extrai o tipo de dado e o número correspondente
        resultado = re.search(r"dado\s+(\w+)\s*(\d+)?", pergunta)
        if resultado:
            tipo_de_dado = resultado.group(1)
            numero_do_dado = int(resultado.group(2)) if resultado.group(2) else 1

            # Gera um número aleatório correspondente ao dado
            resultado_do_dado = random.randint(1, int(tipo_de_dado[1:]))
            resultado_final = f"O resultado do {tipo_de_dado} foi {resultado_do_dado}"
            if numero_do_dado > 1:
                resultado_final += f" x {numero_do_dado} = {resultado_do_dado * numero_do_dado}"

            # Converte a mensagem em fala e reproduz o áudio
            print(resultado_final)
            # Converte a resposta em fala e reproduz o áudio
            engine.say(resultado_final)
            engine.runAndWait()

    elif pergunta == "ler arquivo":
        # Lê o conteúdo do arquivo
        with open("arquivo.txt", "r") as arquivo:
            conteudo = arquivo.read()

        # Obtém a resposta do GPT-3 a partir do conteúdo do arquivo
        resposta = obter_resposta(conteudo)

        # Converte a mensagem em fala e reproduz o áudio
        print(resposta)
        # Converte a resposta em fala e reproduz o áudio
        engine.say(resposta)
        engine.runAndWait()

    else:
        # Envia a pergunta para o GPT-3 e obtém a resposta
        resposta = obter_resposta(pergunta)

        # Converte a mensagem em fala e reproduz o áudio
        print(resposta)
        # Converte a resposta em fala e reproduz o áudio
        engine.say(resposta)
        engine.runAndWait()

# Encerra o programa
print("Programa encerrado.")