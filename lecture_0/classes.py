class StudentCourseError(Exception):
    def __init__(self, message):
        self.message = message


class Student:
    def __init__(self, full_name, course_name=None):
        self.full_name = full_name
        self.course_name = course_name
        self.course_num = 1

    def next_course(self):
        if not self.course_name:
            raise StudentCourseError('Not have course')
        if self.course_num == 3:
            raise StudentCourseError('Student have degree')

        self.course_num += 1

    def change_course(self, course_name):
        self.course_name = course_name
        self.course_num = 1

    def get_diploma(self):
        if self.course_num < 3:
            raise StudentCourseError('Student not have degree')

        return f'{self.full_name},{self.course_name}'
