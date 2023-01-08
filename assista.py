import speech_recognition as aa

listener = aa.Recognizer()


try:
    with aa.Microphone() as origin:
        print("Listening...")
        speech = listener.listen(origin)
        instruction = listener.recognize_google(speech)
        print(instruction)

except:
    pass

