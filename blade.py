# To use, first install speech_recognition and pyaudio via pip
# Then pass your Authorization header token as first argument to this script
# For ex, under Settings of your app in Wit.ai, you will see a token in the following format :
# Authorization : Bearer XYZ (32 strings long), copy the XYZ part and
# run this script as follows, python blade.py XYZ
from gtts import gTTS
import sys
import os
import speech_recognition as speech_recog
import webbrowser
import tldextract

microphone = speech_recog.Microphone()
recognizer = speech_recog.Recognizer()


def spch_to_text(message):
    spch = gTTS(text='Command Received.' + message, lang='en', slow=False)
    spch.save("text.mp3")
    os.system("mpg123 text.mp3")
    os.system("rm -r text.mp3")


def open_browser(url):
    url_stripped = tldextract.extract(url)

    spch_to_text('Opening ' + url_stripped.domain + ' Sam!')
    webbrowser.get('chromium').open_new(url)


with microphone as source:
    recognizer.adjust_for_ambient_noise(source)
while True:
    with microphone as source:
        input = recognizer.listen(source)
        output = recognizer.recognize_wit(input, sys.argv[1]).lower()

        print(output)
        # Suspend System
        if "blade" in output and "sleep" in output:
            spch_to_text('Goodbye Sam! Blade off')
            os.system('systemctl suspend')
        # Open Spotify
        if "blade" in output and "spotify" in output:
            spch_to_text('Opening Spotify Sam!')
            os.system('spotify &')
        # Open Georgia Tech Canvas
        if "blade" in output and "canvas" in output:
            open_browser('https://gatech.instructure.com')
        # Open Piazza
        if "blade" in output and "board" in output:
            open_browser('https://www.piazza.com')
        # Open Netflix
        if "blade" in output and "netflix" in output:
            open_browser('https://www.netflix.com')
        # Open Terminal
        if "blade" in output and "terminal" in output:
            open_browser("gnome-terminal & disown")
