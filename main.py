import speech_recognition as sr
import pyaudio

r = sr.Recognizer()
mic = sr.Microphone()



import modules.level_data as case

MODULES_WANTED = ["wires", "buttons"]


## MODULE HANDLING
module_names = map(lambda x: "modules." + x, MODULES_WANTED)
all_modules_required = list(map(__import__, module_names))[0]
modules_available = list(map(lambda x: getattr(all_modules_required, x), MODULES_WANTED))


with mic as source:
    r.adjust_for_ambient_noise(source)
    is_in_init_mode = False
    while(True):
        try:
            audio = r.listen(source)
            #TODO: Create a function that handles the word input

        except:
            print("Can't hear")
        
