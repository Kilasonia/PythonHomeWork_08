class SchoolMember:
    '''Represents any person at school.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Generated SchoolMember: {0}'.format(self.name))

    def tell(self):
        '''Output information.'''
        print('Name:"{0}" Age:"{1}"'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Represents the teacher.'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Generated Teacher: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{0:d}"'.format(self.salary))


class Student(SchoolMember):
    '''Represents the student'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Generated Student: {0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Evaluations: "{0:d}"'.format(self.marks))


t = Teacher('Сергей Романов', 32, 300000)
s = Student('Дмитрий Киласония', 35, 100)

print() # создаёт пустую строку


members = [t, s]
for member in members:
    member.tell()  # Работает как для преподователя, так и для студента
