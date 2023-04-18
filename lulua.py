from dotenv import load_dotenv
import os
import openai
import pyttsx3

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
        mensagem_motivacional = obter_resposta("Quem me criou foi o Luiz Miguel, utilizando a inteligência artificial do chat gpt 3")

        # Converte a mensagem em fala e reproduz o áudio
        engine.say(mensagem_motivacional)
        engine.runAndWait()

    if pergunta == "motivação":
        # Gera uma mensagem motivacional usando a API do OpenAI
        mensagem_motivacional = obter_resposta("gerar mensagem motivacional")

        # Converte a mensagem em fala e reproduz o áudio
        engine.say(mensagem_motivacional)
        engine.runAndWait()
    else:
        # Envia a pergunta para o GPT-3 e obtém a resposta
        resposta = obter_resposta(pergunta)

        # Converte a resposta em fala e reproduz o áudio
        engine.say(resposta)
        engine.runAndWait()

# Encerra o programa
print("Programa encerrado.")