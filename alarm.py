import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"You set the alarm for: {alarm_time}")
    sound="mixkit-rooster-crowing-in-the-morning-2462.wav"
    
    while True:
        currunt_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(currunt_time)
        time.sleep(1)
        if currunt_time==alarm_time:
            print("Wake up!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break


alarm_time=input("Enter the alarm time(HH:MM:SS): ")
set_alarm(alarm_time)





