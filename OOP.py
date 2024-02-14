
def allLectorsAvg(arr, courseName):
    result = 0
    for el in arr:
        if courseName in el.grades:
            l = len(el.grades[courseName])
            s = sum(el.grades[courseName])
            result += s/l

    return f'Средняя оценка всех лекторов по курсу {courseName}: {result / (len(arr))}\n'

def allStudentAvg(arr, courseName):
    result = 0
    for el in arr:
        if courseName in el.grades:
            l = len(el.grades[courseName])
            s = sum(el.grades[courseName])
            result += s/l

    return f'Средняя оценка всех Студентов по курсу {courseName}: {result/(len(arr))}\n'


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def setGradeLector(self, lecture, grade, course):
        if isinstance(lecture, Lecturer) and 0 < grade <= 10 and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course].append(grade)
            else:
                lecture.grades[course] = [grade]
        else:
            return ('Ошибка')

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.findAvgGrade()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {", ".join(self.finished_courses)}\n')


    def __eq__(self,other):  # ==
        if isinstance(other, Student):
            avgSelf = self.findAvgGrade()
            avgOther = other.findAvgGrade()
            if isinstance(avgOther, (int, float)) and isinstance(avgSelf, (int, float)):
                return avgSelf == avgOther
            else:
                return 'ошибка'
        else:
            return ('Ошибка')


    def __le__(self, other):  # <=
        if isinstance(other, Student):
            avgSelf = self.findAvgGrade()
            avgOther = other.findAvgGrade()
            if isinstance(avgOther, (int, float)) and isinstance(avgSelf, (int, float)):
                return avgSelf == avgOther
            else:
                return 'ошибка'
        else:
            return (f'ошибка')


    def __lt__(self, other): # <
        if isinstance(other, Student):
            avgSelf = self.findAvgGrade()
            avgOther = other.findAvgGrade()
            if isinstance(avgOther, (int, float)) and isinstance(avgSelf, (int, float)):
                return avgSelf == avgOther
            else:
                return 'ошибка'
        else:
            return (f'ошибка')


    def findAvgGrade(self):
        if len(self.grades) == 0:
            return 'Нету оценок'

        temp = []
        for el in self.grades:
            l = len(self.grades[el])
            s = sum(self.grades[el])
            temp.append(s/l)

        l = len(temp)
        s = sum(temp)
        return s/l


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):


    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.findAvgGrade()}\n'


    def __eq__(self,other):  # ==
        if isinstance(other, Lecturer):
            avgSelf = self.findAvgGrade()
            avgOther = other.findAvgGrade()
            if isinstance(avgOther, (int, float)) and isinstance(avgSelf, (int, float)):
                return avgSelf == avgOther
            else:
                return 'ошибка'
        else:
            return ('Ошибка')


    def __le__(self, other):  # <=
        if isinstance(other, Lecturer):
            avgSelf = self.findAvgGrade()
            avgOther = other.findAvgGrade()
            if isinstance(avgOther, (int, float)) and isinstance(avgSelf, (int, float)):
                return avgSelf == avgOther
            else:
                return 'ошибка'
        else:
            return (f'ошибка')


    def __lt__(self, other): # <
        if isinstance(other, Lecturer):
            avgSelf = self.findAvgGrade()
            avgOther = other.findAvgGrade()
            if isinstance(avgOther, (int, float)) and isinstance(avgSelf, (int, float)):
                return avgSelf == avgOther
            else:
                return 'ошибка'
        else:
            return (f'ошибка')


    def findAvgGrade(self):
        if len(self.grades) == 0:
            return 'Нету оценок'
        temp = []
        for el in self.grades:
            l = len(self.grades[el])
            s = sum(self.grades[el])
            temp.append(s/l)

        l = len(temp)
        s = sum(temp)
        return s/l


class Reviewer(Mentor):

    def setGrade(self, student, grade, course, lecture):
        if isinstance(student, Student) and 0 < grade <= 10 and course in student.courses_in_progress and course in lecture.courses_attached:
            if course in student.grades and 0 < grade <= 10:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return ('Это не студент')

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n'



kiril = Student('Кирилл', 'Кутраплели', 'man')
misha = Student('Миша','Демишев', 'man')

zhenya = Reviewer('Женя', 'Селиванова')
nastya = Reviewer('Настя', 'Петрушковна')

egor = Lecturer('Егор', 'Острый')
artem = Lecturer('Артем', 'Сырный')

misha.courses_in_progress.append('python')
kiril.courses_in_progress.append('python')
kiril.courses_in_progress.append('java')

egor.courses_attached.append('python')
artem.courses_attached.append('python')
artem.courses_attached.append('java')


misha.setGradeLector(egor, 10, 'python')
misha.setGradeLector(artem, 7, 'python')
kiril.setGradeLector(artem, 10, 'python')
kiril.setGradeLector(artem, 5, 'java')

zhenya.setGrade(misha, 5, 'python', egor)
zhenya.setGrade(misha, 8,'python', artem)
nastya.setGrade(kiril, 4,'python', egor)
nastya.setGrade(kiril, 6,'java', artem)

print(misha > kiril)
print(misha < kiril)
print(misha != kiril)

print(egor > artem)
print(egor != artem)
print(egor >= artem)

print(allLectorsAvg([egor, artem], 'python'))

print(allStudentAvg([kiril, misha], 'python'))

print(allStudentAvg([kiril, misha], 'java'))

print(kiril)

print(zhenya)

print(egor)

