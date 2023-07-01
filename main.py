import speech_recognition as sr
from handleDevice import InputHandler

r = sr.Recognizer()
mic = sr.Microphone()


with mic as source:
    device = InputHandler()
    r.adjust_for_ambient_noise(source)
    is_in_init_mode = False
    while(True):
        try:
            audio = r.recognize_google(r.listen(source))
            device.handle_input_word(audio)

        except sr.UnknownValueError:
            print("Can't Hear")
        
