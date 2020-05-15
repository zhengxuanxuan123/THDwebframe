import os
def fand_file(path,failname):
	for x in os.listdir(path):
		a = os.path.join(path,x)
		if os.path.isfile(a) and failname in x:
			print(a)
		if os.path.isdir(a):
			fand_file(a,failname)
fand_file('f:/','test')