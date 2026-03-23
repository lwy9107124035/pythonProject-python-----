



class Student:
    def __init__(self):
        self.__age = 20

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age

    age = property(get_age, set_age)    


if __name__ == '__main__':
    s = Student()
    s.age = 99

    print(s.age)