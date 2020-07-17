import time
from tkinter import *
from pygame import mixer
mixer.init()
mixer.music.load('alarm_clock_tonight.mp3')
z = 0
c = 20
a = 0
error = ''


def dt():
    ct = time.strftime('%I:%M:%S:%p')
    l1['text'] = ct
    w.after(1000, dt)


def alarm(self):
    global z
    global a
    global error

    try:
        a = m.get()
        z = h.get()
        if u.get() != 'am' and u.get() != 'pm':
            a = ''
        a = int(a)
        z = int(z)
        if u.get() == 'pm' and h.get() == '12':
            pass
        elif u.get() == 'am' and h.get() == '12':
            z = 00
        elif u.get() == 'pm':
            z = z + 12
        if error != '':
            error.grid_remove()
        error = ''
        sound()
    except Exception as e:
        error = Label(f1, text='Wrong Input')
        error.grid(row=5, column=0)
        print(e)


def stop(self):
    global c
    c = 0


def sound():
    global z
    global c
    global a
    global error

    if time.localtime().tm_hour == z and time.localtime().tm_min == a:
        while c > 0:
            mixer.music.play()
            c = c - 1
    if m.get() != '' and h.get() != '':
        w.after(1000, sound)


w = Tk()
w.title('Alarm Clock')
f1 = Frame(w, bg='white')
f1.pack(side='left')
l1 = Label(w, bg="black", fg="red", font=("arial", 80))
l1.pack(expand=True, fill="both")
dt()
lh = Label(f1, text="Enter the hour : ")
lh.grid(row=0, column=0)
lm = Label(f1, text="Enter the minute : ")
lm.grid(row=1, column=0)
lu = Label(f1, text="Enter am or pm")
lu.grid(row=2, column=0)
h = Entry(f1, bg='white', fg='red')
h.grid(row=0, column=1)
m = Entry(f1, bg='white', fg='red')
m.grid(row=1, column=1)
u = Entry(f1, bg='white', fg='red')
u.grid(row=2, column=1)
b1 = Button(f1, text="Set The Alarm", fg="red")
b1.bind("<Button-1>", alarm)
b1.grid(row=3, column=0)
b2 = Button(f1, text="Turn off", fg="red")
b2.bind("<Button-1>", stop)
b2.grid(row=3, column=1)


w.mainloop()