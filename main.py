import functions as func #importing Olga's functions
import phrases #importing Phrases of Olga
import pyttsx3 #pip install pyttsx3 (lib to speaking)
import chatgpt


#Configuration and initializing 
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

if __name__ == '__main__':
    clear = lambda: func.os.system('cls') # Clean the commands before the execution 
    clear()
    func.wishme(), func.get_date(), func.get_time(), func.speak(phrases.olga_help) #Initial message

    while True:
        audio = func.TakeCommand()

        if 'iniciar chat gpt' in audio:
            while True:
                chatgpt.CallChatGPT()

        if 'que horas são' in audio:
           func.get_time()

        elif 'que dia é hoje' in audio:
            func.get_date()

        elif 'tá aí' in audio:
            func.speak('A seu dispor senhor')

        elif 'como você está' in audio:
            func.speak('Eu estou bem senhor, obrigado por perguntar... E o senhor?')
      
        elif 'estou bem' in audio:
            func.speak('Que maravilha... Espero que continue assim...')
            
        elif 'estou mal' in audio:
           func.speak('O que aconteceu?... Posso ajudar em algo?')
             
        ## elif 'wikipédia' in audio:
        ##   func.wikipedia()
        
        