import random
import gc
from microbit import *
import speech


def speak(msg):
    speech.say(msg, speed=120, pitch=100, throat=100, mouth=200)
    return
    
sleeping = [Image.ASLEEP]    
faces = [Image.HEART, Image.SMILE, Image.HAPPY]
encourage = ["good", "more more", "keep it up", "yes", "very good", "dont stop", "I am watching"]

def wash():
    display.show(Image.SURPRISED)
    speak("start washing your hands!")
    speak("EXTERMINATE,  KIRONA Virus")
    sleep(500)
    
    for i in range(10):
        display.show(9 - i)
        # display.show(random.choice(faces))
        speak(random.choice(encourage))
        sleep(750)

    display.show(Image.SURPRISED)
    speak("Well done, human")
    display.show(Image.HAPPY)
    sleep(100)
    speak("I am going to take a nap now")
    display.show(Image.ASLEEP)


display.show(Image.HEART)
speak("EXTERMINATE, EXTERMINATE,  KIRONA Virus")

i = 1
while True:
    gc.collect()
    i += 1
    x = abs(accelerometer.get_x())
    y = abs(accelerometer.get_y())
    z = abs(accelerometer.get_z())
    if (x > 1200) or (y > 1200) or (z > 1200):
        wash()
    sleep(50)
    if (i < 100 == 0) :
        display.show(Image.HEART_SMALL)
    elif (i % 20 == 0) :
        display.set_pixel(2,2,5)
    elif (i % 20 == 10)  :
        display.clear()
    
    if i > 1000:
        i = 0

        
    