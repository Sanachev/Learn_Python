#Задача: найти сумму натуральныъ чисел меньших 10000,
#в которых встречается не менее двух одинаковых цифр
#пример чисел: 44, 1001, 7712


def func():
    a = 0
    array = []
   
    array2 = [str(x) for x in range(10, 10000)]
    
    for y in array2:
        if len(y)<3:
            if y.count(y[0])==2:
                array.append(y)
        elif 4>len(y)>2:
            if y.count(y[0])>=2 or y.count(y[1])>=2:
                array.append(y)
        elif len(y)>3:
            if y.count(y[0])>=2 or y.count(y[1])>=2 or y.count(y[2])>=2:
                array.append(y)
    for i in array:
        a = a + int(i)
    print(a)
func()
            
