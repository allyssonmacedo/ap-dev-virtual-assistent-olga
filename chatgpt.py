import openai
import keys
import functions as func #importing Olga's functions

import functions as func #importing Olga's functions
import phrases #importing Phrases of Olga
import pyttsx3 #pip install pyttsx3 (lib to speaking)
import time
import settings, mod

def CallChatGPT():

    # def TakeCommand():
    #     r = mod.sr.Recognizer()
    #     with mod.sr.Microphone() as source:
    #         print("Listening...")
    #         r.adjust_for_ambient_noise(source) #noise reduction
    #         r.pause_threshold = settings.time_recognition #set the time of waiting for the answer until the recognition of the command
    #         audio = r.listen(source)  #start the speech recognition 
    #     try:
    #         print("Understanding...")
    #         query = r.recognize_google(audio, language= settings.english).lower() #set the language of the recognition and use the google speech recognize
                  
    #     except Exception as e:
    #         print(e)
    #         pass
    #     return query



    #Configuration and initializing 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice.id, voice.name, voice.languages)
        
    engine.setProperty('voice', voices[1].id) ### Select english language

    chave_api = keys.api_olga
    openai.api_key = chave_api


    def enviar_mensagem(mensagem, lista_mensagens=[]):
        lista_mensagens.append(
            {"role": "user", "content": mensagem}
            )

        resposta = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = lista_mensagens,
        )

        return resposta["choices"][0]["message"]

    lista_mensagens = []

    texto0 = 'I will provide some inputs and I want that you help me with the english practice. So keep a normal conversation and ask questions like a normal human being. Try to not give long answers.'

    print('Wait a minute, I am thinking...')
    resposta = enviar_mensagem(texto0, lista_mensagens)
    lista_mensagens.append(resposta)

    print("Chatbot:", resposta["content"])
    func.speak(resposta["content"])

    while True:

        texto = func.TakeCommand()
        print('User:', texto)

        if 'stop talking' in texto:
            func.speak('OK')
            break

        else:
            resposta = enviar_mensagem(texto, lista_mensagens)
            lista_mensagens.append(resposta)
            print('Wait a minute, I am thinking...')
            print("Chatbot:", resposta["content"])
            func.speak(resposta["content"])

#CallChatGPT()