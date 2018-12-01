# To use, first install speech_recognition and pyaudio via pip
# Then pass your Authorization header token as first argument to this script
# For ex, under Settings of your app in Wit.ai, you will see a token in the following format :
# Authorization : Bearer XYZ (32 strings long), copy the XYZ part and
# run this script as follows, python blade.py XYZ
import time
import sys
import os
import speech_recognition as speech_recog

microphone = speech_recog.Microphone()
recognizer = speech_recog.Recognizer()

while True:
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        input = recognizer.listen(source)
        output = recognizer.recognize_wit(input, sys.argv[1])

        print(output)
        if "blade" in output and "sleep" in output:
            os.system('systemctl suspend')
    time.sleep(1)
