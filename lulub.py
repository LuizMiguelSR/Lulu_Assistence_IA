from dotenv import load_dotenv
import os
import speech_recognition as sr
import pyttsx3
import openai

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Define as credenciais da API do OpenAI a partir da variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configuração da síntese de voz
engine = pyttsx3.init()

# Configuração do reconhecimento de voz
r = sr.Recognizer()

# Função para transcrever o áudio em texto e enviar para o GPT-3
def send_to_gpt3(audio):
    # Transcrição do áudio em texto
    text = r.recognize_google_cloud(audio, credentials_json=open('proven-gasket-383807-f2aed7bb450b.json').read(), language='pt-BR')
    
    # Envio da mensagem para o GPT-3
    response = openai.Completion.create(
      engine="davinci",
      prompt=text,
      temperature=0.7,
      max_tokens=50,
      n=1,
      stop=None,
      timeout=10,
    )
    
    # Retorno da resposta gerada pelo GPT-3
    return response.choices[0].text

# Função para reproduzir a resposta por meio da síntese de voz
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Loop infinito para aguardar o comando "Lulu"
while True:
    with sr.Microphone() as source:
        print("Ouvindo...")
        audio = r.listen(source)
    
    try:
        # Verifica se a palavra "Lulu" foi dita
        if "Lulu" in r.recognize_google_cloud(audio, credentials_json=open('proven-gasket-383807-f2aed7bb450b.json').read(), language='pt-BR'):
            # Envia a mensagem para o GPT-3 e obtém a resposta
            response_text = send_to_gpt3(audio)
            
            # Reproduz a resposta por meio da síntese de voz
            speak(response_text)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
    except sr.RequestError as e:
        print("Erro ao solicitar serviço de reconhecimento de fala; {0}".format(e))
