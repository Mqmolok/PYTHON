from tkinter import*
import datetime

okno = Tk()
okno.geometry('500x500')
okno['bg'] = 'red'
okno .title('Окно')



def qq():
    print(datetime.datetime.now())

aaa = Button(okno, text='Click', command=qq)
aaa.pack()


okno.mainloop()
