import mod, os, settings

engine = mod.pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Functions of Olga:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def TakeCommand():
    r = mod.sr.Recognizer()
    with mod.sr.Microphone() as source:
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
    Time = mod.datetime.datetime.now().strftime('%Horas e %Minutos') #24hr
    #Time=datetime.datetime.now().strftime("%I:%M:%S") #12h
    speak('São {}'.format(Time))

def get_date():
    year = (mod.datetime.datetime.now().year)
    month = (mod.datetime.datetime.now().month)
    date = (mod.datetime.datetime.now().day)
    speak('São {} do {} de {}'.format(date, month, year))

def wishme():
    #speak('Bem-vindo de volta Senhor!')
    hour = mod.datetime.datetime.now().hour
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

