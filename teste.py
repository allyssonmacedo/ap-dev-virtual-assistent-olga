elif 'abra o youtube' in audio:
            speak('O que eu devo procurar?')
            search_term = TakeCommand().lower()
            speak('Procurando...\n')
            wb.open('https://www.youtube.com/results?search_query='+Search_term)
            time.sleep(5)

        elif 'procurar no google' in audio:
            speak("o que eu devo procurar?")
            Search_term = TakeCommand().lower()
            wb.open('https://www.google.com/search?q='+Search_term)

        elif 'procurar por' in query: 
            query = query.replace('procurar por','')
            wb.open(query)
        elif 'chrome' or 'pesquisar no chrome' in query:
            speak('O que eu devo procurar?')
            chromepath = conf.path_chrome
            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

        elif ['introdução', 'se apresente', 'quem é você'] in query:
            speak(phrases.introduction)
        elif 'quem desenvolveu você' or 'quem criou você' in query:
            speak('O Allysson me criou para otimizar as suas tarefas')
        elif 'quem é Allysson' in query:
            speak('Allysson é um engenheiro agrônomo, que utiliza tecnologias para otimizar tarefas. Por isso ele me criou.')
        
        elif 'word' in query:
            speak('Abrindo o word')
            word = settings.path_word
            os.startfile(word)

        #elif 'enviar email' in query:
           # try:
            #    speak('O que eu devo escrever?')
             #   content = TakeCommand()
              #  speak('Quem é o destinatário?')
               # reciept = input('digite o email: ')
                #to = (reciept)
                #sendEmail(to,content)
                #speak(content)
                #speak('O email foi enviado')
            #except Exception as e:
             #   print(e)
              #  speak('Não foi possível enviar o email')
       
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


                
        
        ### elif 'tirar print' in query:
           # screenshot()
            # speak('feito')    
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