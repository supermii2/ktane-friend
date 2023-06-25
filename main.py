import speech_recognition as sr

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
            input_words = r.recognize_google(audio).lower().split()
            
            if input_words[0] == "initialize":
                is_in_init_mode = True

            if is_in_init_mode:
                case.update_data(input_words)
                print(case.data)


            if input_words[0] == "stop":
                print(case.data)
                break

        except:
            print("Can't hear")
        
