#Кредит vs депозит
#Допустим, вы взяли в кредит некоторую сумму, и положили её на депозит
#Сколько надо времени, чтобы депозит стал доходным, учитывая капитализацию?

import time
def credit():
    K = float(input('Введите сумму кредита: '))
    D = K
    N = int(input('На сколько месяцев берём кредит?: '))
    Pс = (((float(input('Введите процентную ставку по кредиту: ')))/100)/12)
    Pd = (((float(input('Введите процентную ставку по депозиту: ')))/100)/12)
    A = (Pс*((1+Pс)**N))/(((1+Pс)**N)-1)
    Sa = A * K
    S = N*A*K
    print()
    print('Размер ежемесячного платежа: %s руб.' % int (Sa))
    print('Общая сумма выплат за весь период: %s руб.' % int(S))
    print()
    global month
    month = 0
    while True:
        if D < (K+S):
            D = D + (D*Pd)
            month += 1
        else:
            print ('Чтобы кредит окупился, требуется %s мес.' % month)
            Pensia = D*Pd
            print('Твоя ежемесячная "пенсия" после окупаемости кредита составит %s руб.' % int(Pensia))
            print()
            def good_dep():
                global dep
                global dep2
                dep2 = 0
                dep = 0
                for x in range(1,N):
                    dep = (dep+Sa) +((dep+Sa)*Pd)
                    dep2 = (dep2+Sa) +((dep2+Sa)*Pd)
                for x in range(1, month-N):
                    dep2 = (dep2+Sa) +((dep2+Sa)*Pd)
                    
            good_dep()
            Good = int(dep*Pd)
            Good2 = int (dep2 *Pd)
            print()
            print ('''Если вместо платежей по кредиту, ты будешь откладывать эти деньги на депозит,
то к моменту окончания кредита (%s мес.), у тебя на счету будет %s руб.,
твоя "пенсия" будет составлять %s руб.''' % (N, int(dep), Good))
            print()
            print('''А если у тебя хватит терпения, то к концу срока окупаемости кредита (%s мес.),
у тебя на счету будет %s руб., твоя "пенсия" составит %s руб.''' % (month, int(dep2), Good2))
            time.sleep(60)
            break
credit()
        
    



