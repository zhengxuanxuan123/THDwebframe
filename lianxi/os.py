import os
def detect_walk(path,failename):
	for root ,dirs,files in os.walk(path):
		for a in files:
			if failename in a :
				print(root,a)
detect_walk('c:/','test' )
