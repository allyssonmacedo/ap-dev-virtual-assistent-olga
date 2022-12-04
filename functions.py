# Libraries used in this project

# Taking screenshots:
from tracemalloc import take_snapshot

# Translations of text:
from gettext import translation
from googletrans import Translator #pip install googletrans==4.0.0-rc1

# For convert speech to text:
import pyttsx3 #pip install pyttsx3 (lib to speaking)
import speech_recognition as sr #pip install SpeechRecognition

# Time 
import datetime #lib to get the time of the OS
import time

import wikipedia #pip install wikipedia  
import smtplib

# Scrapping the web
import webbrowser as wb
import pywhatkit as kit

# Control of the OS and computer
import os
import pyautogui #pip install pyautogui (Para Screenshot)
import psutil #pip install pustil

# To get data
import pyjokes #pip install pyjokes (Para piadas)
import operator
import json
# import wolframalpha
from urllib.request import urlopen
import requests

import settings

# from contacts import contact #(para importar contatos)

import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Functions of Olga:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escutando...")
        r.adjust_for_ambient_noise(source) #noise reduction
        r.pause_threshold = settings.time_recognition #set the time of waiting for the answer until the recognition of the command
        audio = r.listen(source)  #start the speech recognition 
    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language= settings.portuguese).lower() #set the language of the recognition and use the google speech recognize
        if "olga" in query.lower():
            query = query.replace("olga", "")
               #drop the word "olga" from the query
        print(query)
        
    except Exception as e:
        print(e)
        return "None"
    return query

def get_time():
    Time = datetime.datetime.now().strftime('%Horas e %Minutos') #24hr
    #Time=datetime.datetime.now().strftime("%I:%M:%S") #12h
    speak('São {}'.format(Time))

def get_date():
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

### {def sendEmail(to = settings.to, content = settings.content):
    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.ehlo()
    #server.starttls()
    # the email has to be with low security level
    #server.login(settings.your_email, settings.your_password) #configuration of the login and password
    #server.sendmail(settings.your_email, to, content) #configuration of the message of the receiver and the content of the message
   # server.close()

### def screenshot(path_screenshot = settings.path_screenshot):
   #img = pyautogui.screenshot()
    #img.save(path_screenshot) #set the path of the image

def cpu():
    usage = str(psutil.cpu_percent())
    return ('O uso da CPU está em'+ usage)

def jokes_pt():
    joke_en = pyjokes.get_joke() #get a random joke
    print(joke_en) #print the joke on terminal
    trans = Translator() 
    joke_pt = trans.translate(joke_en, dest='pt').text  #translate the joke to portuguese
    print(joke_pt)
    speak(joke_pt)

def Answer():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando resposta")
        r.adjust_for_ambient_noise(source) #noise reduction
        r.pause_threshold = 0.5 #set the time of waiting for the answer until the recognition of the command
        audio = r.listen(source)  #start the speech recognition 
    try:
        print("Identificando")
        query = r.recognize_google(audio, language= settings.portuguese).lower() #set the language of the recognition and use the google speech recognize 
        if "olga" in query.lower():
            query = query.replace("olga", "")   #drop the word "olga" from the query
        print(query)
        
    except Exception as e:
        print(e)
        return "None"
    return query

def wikipedia():
    query = audio.replace("wikipédia","")
    result = wikipedia.summary(query, sentences=2)
    speak("De acordo com a wikipedia", result)
    print(result)

