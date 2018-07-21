#округление дробного числа

import time
def okruglenie():
    a = input('Введите дробное число: ')
    b = int(input('Введите, сколько знаков оставить после разделительной точки?: '))
    c = a.index('.')
    d = b + c + 1
    e = float(a[0:d])
    print(e)
    print()
    print('Окно программы закроется самостоятельно менее чем через минуту')
    time.sleep(60)
okruglenie()
    
    
