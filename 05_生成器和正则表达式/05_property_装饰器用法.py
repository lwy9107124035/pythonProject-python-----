class Student:
    def __init__(self):
        self.__age = 18

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age


if __name__ == '__main__':
    s = Student()
    s.age = 19

    print(s.age)

