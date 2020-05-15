import os
print(os.path.abspath('.'))
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
print(os.listdir('f:/'))
print(os.path.isdir('D:/lesson'))


from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()#每行读取
	if s == '':#当读取到空
		break#终止读取
	print(s.strip())#strip()去掉首尾空格