#Решение задачи из учебника.

new_data = ('dog/chien', 'cat/chat', 'walrus/morse')

def dictionary(x):
	array = list()
	for y in range(0, len(x)):
		array.append(x[y].split('/'))
	eng_2_fran = dict(array)
	print(eng_2_fran)

dictionary(new_data)
