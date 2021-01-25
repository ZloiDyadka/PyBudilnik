import datetime, time, winsound
from tkinter import *





def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)
        print(now)
        if now == set_alarm_timer:
            print('time to Wake up')
            winsound.PlaySound('90.wav', winsound.SND_ASYNC)
            break

def actual_time():

    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()

clock.title("Будильник")
clock.geometry("500x300")
addTime = Label(clock,text = "Часы  Минуты   Секунды",font=60).place(x = 150)
setYourAlarm = Label(clock,text = "Время срабатывания",fg="blue",relief = "solid",font=("Helevetica",8,"bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime=Entry(clock, textvariable = hour, bg = "pink", width=15).place(x=150, y=30)
minTime=Entry(clock, textvariable = min, bg = "pink", width=15).place(x=200, y=30)
secTime=Entry(clock, textvariable = sec, bg = "pink", width=15).place(x=250, y=30)

submit=Button(clock, text="Поставить будильник", fg='red', width=10, command=actual_time).place(x=150, y=70, anchor="w", height=30, width=130)

clock.mainloop()