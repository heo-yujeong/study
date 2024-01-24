class StringUtils:
	@staticmethod
	def reverse_string(string):
		return string[::-1]
	
	@staticmethod
	def capitalize_string(string):
		return string.capitalize()

text = 'hello, world'

reversed_text = StringUtils.reverse_string(text)
# 클래스가 호출해야 함
print(reversed_text) # dlrow , olleh

capitalized_text = StringUtils.capitalize_string(text)
print(capitalized_text) # Hello, world