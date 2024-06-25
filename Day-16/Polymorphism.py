class Dog:
    def make_sound(self):
        return "Woof!"

class Cat:
    def make_sound(self):
        return "Meow!"

class Cow:
    def make_sound(self):
        return "Moo!"

def animal_sound(animal):
    return animal.make_sound()

# Objek dari kelas berbeda
dog = Dog()
cat = Cat()
cow = Cow()

# Memanggil metode yang sama pada objek yang berbeda
print(animal_sound(dog))  
print(animal_sound(cat))  
print(animal_sound(cow))  
