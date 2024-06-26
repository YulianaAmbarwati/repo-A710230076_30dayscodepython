# Kelas Induk
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

# Kelas Turunan
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def info(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"

# Contoh penggunaan
student = Student("Yuliana Ambarwati", 18, "A710230076")

print(student.info()) 