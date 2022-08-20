import settings #set the configuration of Olga such like languages and other settings
from gettext import translation
import pyttsx3 #pip install pyttsx3 (lib to speaking)
import datetime #lib to get the time of the OS
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia  
#import smtplib
import webbrowser as wb
import os
import pyautogui #pip install pyautogui (Para Screenshot)
import psutil #pip install pustil
import pyjokes #pip install pyjokes (Para piadas)
import random
import operator
import json
#import wolframalpha
import time
from urllib.request import urlopen
import requests
import pywhatkit as kit
from googletrans import Translator #pip install googletrans==4.0.0-rc1
#from contacts import contact (para importar contatos)

#Configuration and initializing 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Functions of Olga:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def time_():
    Time=datetime.datetime.now().strftime('%Horas e %Minutos') #24hr
    #Time=datetime.datetime.now().strftime("%I:%M:%S") #12h
    speak('São {}'.format(Time))

def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak('São {} do {} de {}'.format(date, month, year))

def wishme():
    #speak('Bem-vindo de volta Senhor!')
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Bom dia. Como está se sentindo hoje?")
    elif hour >=12 and hour<18:
        speak("Boa tarde. Como está se sentindo hoje?")
    else:
        speak("Boa noite. Como está se sentindo hoje?")
    time_()
    date()
    speak("Olga a seu serviço. Como posso lhe ajudar?")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        r.adjust_for_ambient_noise(source) #noise reduction
        r.pause_threshold = 0.5 #set the time of waiting for the answer until the recognition of the command
        audio = r.listen(source)  #start the speech recognition 
    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language= settings.portuguese) #set the language of the recognition and use the google speech recognize
        if "olga" in query.lower():
           query = replace("olga", "")   #drop the word "Olga" from the query
        print(query)
        
    except Exception as e:
        print(e)
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # the email has to be with low security level
    server.login(settings.your_email, settings.your_password) #configuration of the login and password
    server.sendmail(settings.your_email, to, content) #configuration of the message of the receiver and the content of the message
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save(settings.save_image) #set the path of the image

def cpu():
    usage = str(psutil.cpu_percent())
    speak('O uso da CPU está em'+ usage)

def jokes():
    joke_en = pyjokes.get_joke() #get a random joke
    print(joke_en) #print the joke on terminal
    trans = Translator() 
    joke_pt = trans.translate(joke_en, dest='pt').text  #translate the joke to portuguese
    print(joke_pt)
    speak(joke_pt)

def Introduction():
    speak('Eu sou a Olga, sua assistente com inteligência artificial...')
    speak('Fui projetada para otimizar as suas tarefas....')
    speak('Deseja saber o que eu sou capaz de fazer?..')
    
if __name__ == '__main__':

    clear = lambda: os.system('cls') # Clean the commands before the execution 
    clear()
    wishme()
    
    while True:
        query = TakeCommand().lower()
        # comandos convertidos em minúsculas

        if 'horas' in query:
            time_()
        elif 'que dia é hoje' in query:
            date()
        elif 'como você está' in query:
            speak('Eu estou bem senhor, obrigado por perguntar.')
            speak('E o senhor?')
            ans = (TakeCommand().lower())
            if 'bom' in query or "ótimo" in ans: 
                speak('Que bom, senhor. Espero que continue assim')
            else:
                speak('O que aconteceu?')
                ans = (TakeCommand().lower())
                if 'nada' in ans:
                    speak('Gostaria de ouvir uma piada?')
                    ans = (TakeCommand().lower())
                    if 'sim' or 'claro' in ans:
                        jokes()
                    else:
                        speak('Tudo bem, senhor. Precisando, só chamar.!')
                else:
                    speak('Nossa, lamento ouvir isso, senhor')
                    speak('Em que posso ser útil agora?')
        elif 'wikipedia' in query:
            speak("É pra já, senhor...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak("De acordo com a wikipedia")
            print(result)
            speak(result)
        
        elif 'Abra o youtube' in query:
            speak('O que eu devo procurar?')
            Search_term = TakeCommand().lower()
            speak('Procurando...\n')
            wb.open('https://www.youtube.com/results?search_query='+Search_term)
            time.sleep(5)

        elif 'procurar no google' in query:
            speak("o que eu devo procurar?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)
        elif 'procurar por' in query: 
            query = query.replace('procurar por','')
            wb.open(query)
        elif 'chrome' or 'pesquisar no chrome' in query:
            speak('O que eu devo procurar?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif 'introdução' or 'se apresente' or 'quem é você' in query:
            Introduction()
        elif 'quem desenvolveu você' or 'quem criou você' in query:
            speak('O Allysson me criou para otimizar as suas tarefas')
        elif 'quem é Allysson' in query:
            speak('Allysson é um engenheiro agrônomo, que utiliza tecnologias para otimizar tarefas. Por isso ele me criou.')
        
        elif 'word' in query:
            speak('Abrindo o word')
            word = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
            os.startfile(word)

        elif 'enviar email' in query:
            try:
                speak('O que eu devo escrever?')
                content = TakeCommand()
                speak('Quem é o destinatário?')
                reciept = input('digite o email: ')
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak('O email foi enviado')
            except Exception as e:
                print(e)
                speak('Não foi possível enviar o email')
       
        elif 'log out' in query:
            os.system("shutdown -l")
        elif 'reiniciar o computador' in query:
            os.system("shutdown /r /t 1")
        elif 'desligar o computador' in query:
            os.system("shutdown /s /t 1")

            
        elif 'lembre' or 'lembrar' in query:
            speak('O que eu devo lembrar?')
            memory = TakeCommand()
            speak('Você me pediu para lembrar de'+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'você se lembra de algo' or 'o que eu lhe falei' or 'lembranças' or 'lembrete' in query:
            remember =open('memory.txt', 'r')
            speak('Você me pediu para lembrar de '+remember.read())
        
        
        elif 'escreva' or 'anotação' in query:
            speak('O que eu devo escrever?')
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak('Devo incluir dia e hora?')
            dt = TakeCommand()
            if 'sim' in dt or 'claro' in dt:
                strTime = datetime.datetime.now().strftime('%H:%M:%S')
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('feito')
            else:
                file.write(note)
                
        elif 'anotações' or 'mostrar notas' or 'ler notas' in query:
            speak('Mostrando notas')
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 

        elif "clima" in query: 
			
			# Google Open weather website 
			# to get API of Open weather
            api_key = "open weather api"
            base_url = "http://api.openweathermap.org/data/2.5/weather?q="
            speak(" City name ")
            print("City name : ")
            city_name = TakeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
            else:
                speak(" City Not Found ") 





        elif 'news' in query:
            
            try:

                jsonObj = urlopen('''news api link''')
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the times of india')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 


                
        
        elif 'tirar print' in query:
            screenshot()
            speak('feito')    
        elif 'cpu' in query:
            cpu()
        elif 'piada' in query:
            jokes()
    
        
        #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
            
        elif "i love you" in query:
            speak("It's hard to understand, I am still trying to figure this out.")
        

        #calculation
        elif "calculate" in query:
            
            app_id = "wolfram alpha api"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        



        #General Questions
        elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier
            client = wolframalpha.Client("wolfram alpha api")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 





        elif 'não escute' or 'pare de ouvir' or 'espere' in query:
            speak('Por quantos segundos devo ficar ausente?')
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        elif 'offline' in query:
            speak('ficando offline')
            quit()

#Transformar em executável .exe
#abrir o diretório 
#pyinstaller --onefile 'olga.py'S