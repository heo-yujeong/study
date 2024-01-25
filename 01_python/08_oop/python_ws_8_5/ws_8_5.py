class Dog:
    sound = '멍멍'

class Cat:
    sound = '야옹'

class Pet(Dog, Cat):
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'

print('---Dog 클래스를 우선 상속---')    
pet1 = Pet()
print(pet1)

class Pet(Cat, Dog):
    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'
    
print()
print('---Cat 클래스를 우선 상속---')    
pet2 = Pet()
print(pet2)