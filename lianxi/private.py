class Student4(object):
	def __init__(self, name, gender):
		self.name = name
		self.__gender = gender
	def get_gender(self):
		return self.__gender
	def set_gender(self,gender):
		self.__gender = gender
bart = Student4('Bart', 'male')
if bart.get_gender() != 'male':
	print('测试失败!')
else:
	bart.set_gender('female')
	if bart.get_gender() != 'female':
		print('测试失败!')
	else:
		print('测试成功!')

a =Student4
print(type(123))
print(type(a))
