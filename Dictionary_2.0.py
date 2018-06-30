#Задача из учебника
#Преобразование англо-французского словаря в французско-английский

new_data = ('dog/chien', 'cat/chat', 'walrus/morse')

def dict_e2f(x):
	array = list()
	for y in range(0, len(x)):
		array.append(x[y].split('/'))
	global e2f
	e2f = dict(array)
	print('Англо-французский словарь (call by variable e2f):\n%s ' % e2f)

def dict_f2e():
	f2e_key = list(e2f.values())
	f2e_val = list(e2f.keys())
	f2e_dict = list()
	for x in range(0,len(f2e_key)):
		f2e_dict.append(list())
		f2e_dict[x].append(f2e_key[x])
		f2e_dict[x].append(f2e_val[x])
	global f2e
	f2e = dict(f2e_dict)
	print ('Французско-английский словарь(call by variable f2e):\n%s ' % f2e)

def result():
    dict_e2f(new_data)
    print()
    dict_f2e()

result()
