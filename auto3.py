import pyautogui as pd
import time
import random

# pd.alert(text = 'all', button = 'ok', title = 'lo')
# knjpka = pd.confirm(text = 'lll', buttons =['yes', 'no'])
# print(knjpka)

# aa = pd.prompt(text = 'hello')
# print(aa)
# pd.password(text = 'Введите ваш пароль.')

while True:
    a = random.randint(1,15)
    time.sleep(0.5)
    if a == 8:
        pd.alert(text = 'Вы выиграли миллион!!!!!!!', title = 'Поздрявляем!', button = 'Спасибо!')
        break
    else:
        print('Не повезло:(')