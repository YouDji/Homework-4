# 1
class Person:
    def __init__(self, age: int, name, surname):
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.age}{self.name}{self.surname}"

    # 2


class Student(Person):

    def __init__(self, kurs: int, s_b: float, age: int, name: str, surname: str):
        super().__init__(age, name, surname)
        self.kurs = kurs
        self.s_b = s_b

    def __eq__(self, other):
        return self.surname == other.surname and self.name == other.name and self.age == other.date_of_birth \
               and self.kurs == other.kurs

    def __str__(self):
        return f"{super().__str__()}{self.kurs}{self.s_b}"


class FirstError(Exception):

    def __init__(self, eric):
        super().__init__()
        self.eric = eric

    def __str__(self):
        return f"{self.eric}\n{super().__str__()}"


class Group:
    def __init__(self, title):
        self.title = title
        self.students = []

    def a(self, student: Student):
        if len(self.students) >= 10:
            raise FirstError('Too many student in group!')

    def group_students(self, student: Student):
        for a_group in self.students:
            if a_group == student:
                return -1
        self.students.append(student)

    def finder(self, surname):
        for a_group in self.students:
            if a_group.surname.lower() == surname.lower():
                return a_group

        return -1

    def __str__(self):
        return f'{self.title}\n' + '\n'.join(map(str, self.students))


st_1 = Student(2, 3.4, 18, "Dan", "Manych")
st_2 = Student(2, 3.4, 18, "Daniil", "Manych2")
st_3 = Student(2, 3.4, 18, "Daniel", "Manych3")
st_4 = Student(2, 3.4, 18, "Danon", "Manych4")
try:
    x = Group(':)')
    x.a(st_1)
    x.a(st_2)
    x.a(st_3)
    x.a(st_4)
except (ValueError) as err:
    print('Набір завершено', err)
print(x.finder('ivanov'))

