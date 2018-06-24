import sys
def moon_weight():
   print('Введите ваш нынешний земной вес:')
   earth_weight = int (sys.stdin.readline())
   print('Сколько вы прибавляете каждый год?')
   delta_weight = int (sys.stdin.readline())
   print('В течение скольки лет будем производить расчёт?')
   year = int (sys.stdin.readline())+1
   for i in range (1,year):
      moon_weight = earth_weight * 0.165
      print('%s год - лунный вес: %s кг' % (i, moon_weight))
      earth_weight = earth_weight+delta_weight
moon_weight()
