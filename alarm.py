import datetime
import time
import winsound
import pyttsx3


alarm_time = input("Enter alarm time (HH:MM): ")
print(f"Alarm set for {alarm_time}")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now >= alarm_time:   
        engine = pyttsx3.init()
        engine.say("Wake up Sir! It's morning, please wake up!!!")
        engine.runAndWait()

       
        melody = [
            (1000, 500), (1200, 500), (1400, 500)
        ]

        # Repeat alarm sound 5 times
        for _ in range(5):
            for freq, dur in melody:
                winsound.Beep(freq, dur)

        break  
    time.sleep(1)

