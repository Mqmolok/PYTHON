from tkinter import *
import random
import time
#Импортируем файл
root = Tk()
root.geometry("800x600+90+110")
root.title("Пародия дудл джамба")
canvas = Canvas(root, width=800, height=600, bg='black') #Холст
canvas.pack()
pls = []
x = 40
y = 560
r = 20
vx = -5
vy = 5
player = canvas.create_oval(x - r, y - r, x + r, y + r, fill='orange') #Игрок
still = False
active = False
score = 0
text = canvas.create_text(80, 20, text=f'Очки: {score}', font=("Comic Sans MS", 18)) #Счет 12
def new_platform():
    global pls, score
    x=random.randint(0,800-120)
    y=10
    w=120
    h=20
    color="red"
    platform = canvas.create_rectangle(x, y, x + w, y + h, fill=color, width=0)
    pls.append(platform)
    canvas.after(1750, new_platform)
    if active:
        score += 1
        canvas.itemconfig(text, text=f'Очки: {score}', fill= 'white') # Условия клика и счета
def move_player():
    global player, x, y, vx, vy
    x, y, _, _ = canvas.coords(player)
    if still:
        vy = 2
    else:
        vy += 2
    if still:
        vx *= 0.5
    else:
        vx *= 0.94
    y += vy
    x += vx
    if x <= 0:
        vx = -vx
    if x >= 800 - 2 * r:
        vx = -vx
    if y <= 0:
        vy = -vy
    if y >= 600 - 2 * r and not active:
        vy = 0
    if y >= 600 - 2 * r and active:
        canvas.delete(player)
        canvas.delete(*pls)
        return True

    canvas.move(player, vx, vy)  
def platform_check(platform):
    global pls
    px, py,_,_ = canvas.coords(platform)
    if py > 620:
        pls.remove(platform)
        print("Удалили")
        return True
    return False
def ggg():
    global pls, still, vy, vx
    x, y,_,_  = canvas.coords(player)
    for platform in pls:
        if platform_check(platform):
            break

        canvas.move(platform, 0, 2)
        px, py,_ , _ = canvas.coords(platform)
        if py - 2 * r <= y - r / 3 <= py:
            if px <= x <= px + 120:
                if not still:
                    vy = 0
                    canvas.coords(player, px - r + 60, py - r - 22, px + r + 60, py + r - 22) #Передвижение нашей плотформы 
                    still = True   
def cklick(event):
    global vy, vx, still, active
    x, y,_,_  = canvas.coords(player)
    vx = (event.x - x)/15
    vy = (event.y - y)/9
    still = False
    active = True
root.bind_all('<1>', cklick)
new_platform()
while True:
    ggg()
    loose = move_player()
    if loose:
        canvas.delete(text)
        canvas.create_text(400, 280, text=f"Ты проиграл!\n  Результат: {score}", font=("Comic Sans MS", 52), fill="red") #Результат когда закончил игру
        root.update()
        time.sleep(3)
        break
    root.update()
    root.update_idletasks()
    time.sleep(0.01) #Цикл