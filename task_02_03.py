def average(lst):
 	suma = 0
 	for i in lst:
 		suma = suma + i
 	return round(suma/len(lst),3)