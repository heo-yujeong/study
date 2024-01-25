# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

class Cat(Animal):
    def __init__(self, meow_sound):
        self.meow_sound = meow_sound

    def meow(self):
        print(f'{self.meow_sound}!')


cat1 = Cat("야옹")
cat1.meow()
