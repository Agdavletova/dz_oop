# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

students_all = []
lecturers_all = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_all.append({"name": self.name, "surname": self.surname, "grades": self.grades})

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        sum_grades = 0
        k = 0
        for i in self.grades:
            sum_grades = sum_grades + sum(self.grades[i])
            k = k + len(self.grades[i])
        return round(sum_grades / k, 3)

    def __str__(self):
        s_1 = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}"
        s_2 = f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return s_1 + "\n" + s_2


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers_all.append({"name": self.name, "surname": self.surname, 'grades': self.grades})

    def average(self):
        sum_grades = 0
        k = 0
        for i in self.grades:
            sum_grades = sum_grades + sum(self.grades[i])
            k = k + len(self.grades[i])
        return round(sum_grades / k, 3)

    def __str__(self):
        s = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average()}"
        return s

    def __lt__(self, other):
        res = False
        if float(self.average()) > float(other.average()):
            res = True
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        s = f"Имя: {self.name}\nФамилия: {self.surname}"
        return s


def average_student_all(course):
    summ = 0
    k = 0
    for people in students_all:
        grades = people['grades']
        for g in grades:
            if g == str(course):
                summ = summ + sum(grades[g])
                k = k + len(grades[g])
    return round(summ / k, 2)


def average_lecturer_all(course):
    s = 0
    k = 0
    for people in lecturers_all:
        grades = people['grades']
        for g in grades:
            if g == str(course):
                s = s + sum(grades[g])
                k = k + len(grades[g])
    return round(s / k, 2)


# 1 студент

first_student = Student('Ruoy', 'Eman', 'man')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Java']
first_student.finished_courses += ['Git']

# 2 студент
second_student = Student("Maria", "Oll", "woman")
second_student.courses_in_progress += ['Git']
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Java']

# 1 проверяющий
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['Java']

# 2 проверяющий
cool_mentor_2 = Reviewer('Some_2', 'Buddy_2')
cool_mentor_2.courses_attached += ['Python']
cool_mentor_2.courses_attached += ['Git']

# оценки 1 студента
cool_mentor.rate_hw(first_student, 'Python', 10)
cool_mentor.rate_hw(first_student, 'Python', 10)
cool_mentor.rate_hw(first_student, 'Python', 10)

cool_mentor.rate_hw(first_student, 'Java', 5)
cool_mentor.rate_hw(first_student, 'Java', 7)

# оценки 2 студента
cool_mentor.rate_hw(second_student, 'Python', 6)

cool_mentor.rate_hw(second_student, 'Java', 5)
cool_mentor.rate_hw(second_student, 'Java', 3)

cool_mentor_2.rate_hw(second_student, 'Git', 10)
cool_mentor_2.rate_hw(second_student, 'Git', 9)

# 1 лектор
lector = Lecturer("Joh", "Familia")
lector.courses_attached +=['Python']
lector.courses_attached +=['Git']
# 2 лектор
lector_2 = Lecturer('Stiven', "Hoking")
lector_2.courses_attached +=['Python']
lector_2.courses_attached +=['Java']

# оценки 1 лектора
first_student.rate_hw(lector, "Python", 10)
first_student.rate_hw(lector, "Git", 10)

second_student.rate_hw(lector, "Python", 7)
second_student.rate_hw(lector, "Git", 7)

# оценки 2 лектора
first_student.rate_hw(lector_2, "Python", 6)
first_student.rate_hw(lector_2, "Java", 10)
second_student.rate_hw(lector_2, "Java", 6)
second_student.rate_hw(lector_2, "Python", 6)

print(lector)
print(second_student)
# print(lector_2)
# print(lector.average())
# print(lector_2.average())
#
# print(lector > lector_2)
# print(students_all)
# print(lecturers_all)
# print(best_student.grades['Java'])
# print(second_student.grades["Java"])
#
# print(average_student_all('Java'))
print(lector.grades['Python'])
print(lector_2.grades['Python'])
print(average_lecturer_all('Python'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
