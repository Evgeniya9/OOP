class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['java']
        self.courses_in_progress = ['python']
        self.grades = {'python': [5, 3], 'java': [9, 7]}

    def setGradeLector(self, lecture, grade, course):
        if isinstance(lecture, Lecturer) and 0 < grade < 10 and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course].append(grade)
            else:
                lecture.grades[course] = [grade]
        else:
            print('Ошибка')

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.findAvgGrade()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')

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
        self.courses_attached = ['python']
        self.grades = {}


class Lecturer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\nСредняя оценка за лекции: {self.findAvgGrade()}'

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

    def setGrade(self, student, grade):
        if isinstance(student, Student) and 0 < grade < 10:
            student.grades['Homework'] = grade
        else:
            print('Это не студент')

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


misha = Student('Миша', 'Демишев', 'man')
kiril = Student('Ки', 'Рил', 'man')

artem = Lecturer('Артем', "прокуша")

zhenya = Reviewer('Женя', 'Селиванова')

# print(artem.grades)
misha.setGradeLector(artem, 6, 'python')
# print(artem.grades)
kiril.setGradeLector(artem, 4, 'python')
# print(artem.grades)

print(misha)