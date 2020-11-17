class School:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


class Student(School):
    def __init__(self, firstname, lastname, age, average_score):
        School.__init__(self, firstname, lastname, age)
        self.average_score = average_score

    def info(self):
        print(self.firstname)
        print(self.lastname)
        print(self.age)
        print(self.average_score)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Teacher(School):
    def __init__(self, firstname, lastname, age, exp):
        School.__init__(self, firstname, lastname, age)
        self.exp = exp

    def info(self):
        print(self.firstname)
        print(self.lastname)
        print(self.age)
        print(self.exp)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def __repr__(self):
        return f"{self.firstname} {self.lastname}"


class Group:
    def __init__(self, num, stud_lst=None, teach_lst=None):
        self.num = num
        self.stud = stud_lst or []
        self.teach = teach_lst or []

    def add_student(self, student):
        self.stud.append(student)

    def delete_student(self, student):
        self.stud.remove(student)

    def average(self):
        print("Средний балл: ", sum([x.average_score for x in self.stud]) // len(self.stud))

    def add_teacher(self, teacher):
        self.teach.append(teacher)

    def delete_teacher(self, teacher):
        self.teach.remove(teacher)

    def exp(self):
        print("Средний стаж: ", sum([x.exp for x in self.teach]) // len(self.teach))

    def inf(self):
        print('Студенты\n', 'Группа №', self.num, ':', ', '.join(map(str, self.stud)))
        print('Преподаватели\n', 'Группа №', self.num, ':', ', '.join(map(str, self.teach)))


a1 = Student('Vitaly', 'Sazonov', 27, 6)
a2 = Student('Olya', 'Denis', 24, 10)
a3 = Student('Ivan', 'Petrov', 20, 8)

t1 = Teacher('Artem', 'Ivanov', 65, 30)
t2 = Teacher('Oleg', 'Shitov', 63, 24)
t3 = Teacher('Anna', 'Shitova', 58, 20)

g1 = Group(2)
g1.add_student(a1)
g1.add_student(a2)
g1.add_student(a3)
g1.add_teacher(t1)
g1.add_teacher(t2)
g1.add_teacher(t3)
g1.inf()
g1.delete_teacher(t3)
g1.inf()
g1.delete_student(a2)
g1.inf()
g1.average()
g1.exp()
