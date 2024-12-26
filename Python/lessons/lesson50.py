# class Student:
#     average_mark: float = 0
#     scholarship: int = 0
#
#     def __init__(self, first_name: str, last_name: str, group: str, marks: dict):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.group = group
#         self.marks = marks
#
#     @property
#     def get_average_mark(self):
#         self.average_mark = sum(self.marks.values()) / len(self.marks)
#         return f'Средняя оценка: {self.average_mark}'
#
#     def get_scholarship(self):
#         self.scholarship = 2000 if self.average_mark == 5.0 else 1900
#         return f'Стипендия студента: {self.scholarship}'
#
#
# class Aspirant(Student):
#     def __init__(self, first_name: str, last_name: str, group: str, marks: dict, research_work: str):
#         super().__init__(first_name, last_name, group, marks)
#         self.research_work = research_work
#
#     def get_scholarship(self):
#         self.scholarship = 2500 if self.average_mark == 5.0 else 2200
#         return f'Стипендия аспиранта: {self.scholarship}'
#
#
# student1 = Student('Alex', 'Kovach', '11-A', {
#     'Math': 5,
#     'Chemistry': 5,
#     'History': 5,
#     'English': 5,
#     'Russian': 5,
# })
#
# aspirant1 = Aspirant('Alex', 'Kovach', '11-A', {
#     'Math': 2,
#     'Chemistry': 2,
#     'History': 2,
#     'English': 2,
#     'Russian': 2,
# }, 'Fairytale')
#
# lists: list = [student1, aspirant1]
# for i in lists:
#     print(i.get_average_mark)
#     print(i.get_scholarship())
#     print()


