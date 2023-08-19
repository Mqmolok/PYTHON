print(" Это калькулятор  ")
a = input("Введите первое число: ")
c = input("Введите операцию: ")
b = input("Введите второе число: ")
try :
    a = int(a)
    b = int(b)    
    
except ValueError:
    print('Введите число, а не слово.')
    
else:
    try:
    
        if  c=="+":    
            print(f"{a}+{b}={a+b}")
        elif c=="-":
            print(f"{a}-{b}={a-b}")
        elif c=="*":
            print(f"{a}*{b}={a*b}")
        elif c=="/":
            print(f"{a}/{b}={a/b}")
        elif c=="**":
            print(f"{a}**{b}={a**b}")
        elif c=="//":
            print(f"{a}//{b}={a//b}")
        elif c=="%":
            print(f"{a}%{b}={a%b}")
        else:
            print("Я тебя не понимаю")
    except ZeroDivisionError:
        print('Деление на 0 НЕЛЬЗЯ.')
finally:
    print('Конец программы.')
