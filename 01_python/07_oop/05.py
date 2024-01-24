class MyClass:

	def instance_method(self):
		return 'instance method', self

	@classmethod
	def class_method(cls):
		return 'class method', cls

	@staticmethod
	def static_method():
		return 'static method'

instance = MyClass()

print(MyClass.instance_method(instance))
print(MyClass.class_method())
print(MyClass.static_method())

print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())