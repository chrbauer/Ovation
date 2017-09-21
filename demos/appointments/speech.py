import audio

        
class Speech():

    def __init__(self):
        print ("Using Speech")
        audio.init_threshold()

    def check(self):
        print("Listening for keyword '", audio.keyword, "'", sep="")
        line = audio.passive_listen()
        if line:
            print("YOU:", line)
        return True

    def waitForSentence(self):
        while True:
            alts=audio.active_listen()
            print("Alternatives:", ", ".join(alts))
            if alts and len(alts) > 0:
                response=alts[0]
                print("YOU:", response)
                return response

    
    def say(self,response):
        print("BOT:", response)
        audio.say(response)
