# Person 정의
class Person:
	name = 'unknown'

	def talk(self):
		print(self.name)

p1 = Person()
p1.talk() # unknown

p2 = Person()
p2.talk() # unknown
p2.name = 'Kim'
p2.talk() # Kim

print(Person.name) # unknown
print(p1.name) # unknown
print(p2.name) # Kim

p2.ssafy = 11 # 독립적인 개발공간이기 때문에 어떤 것을 만들어도 No상관
print(p2.ssafy)
# print(p1.ssafy) # AttributeError