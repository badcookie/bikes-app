class StudentCourseError(Exception):
    """Handles errors referred to Student class.

    Parameters
    ----------
        message
            Output info.

    """

    def __init__(self, message):
        self.message = message


class Student:
    """Contains data on a student.

    Parameters
    ----------
    full_name
        Student's full name.
    course_name
        Name of a current student's course (optional).

    Attributes
    ----------
    course_num
        Student's current course number (initially set to 1).

    """

    def __init__(self, full_name, course_name=None):
        self.full_name = full_name
        self.course_name = course_name
        self.course_num = 1

    def next_course(self):
        """Increases student's course number by one.

        Raises
        ------
        StudentCourseError
            Raised when a course name is not defined
            or course number is equal to 3.

        """

        if not self.course_name:
            raise StudentCourseError('Not have course')
        if self.course_num == 3:
            raise StudentCourseError('Student have degree')

        self.course_num += 1

    def change_course(self, course_name):
        """Changes student's course.

        Parameters
        ----------
        course_name
            Name of a course to change to.

        Notes
        -----
        With each new course student's course
        number is set to 1.

        """

        self.course_name = course_name
        self.course_num = 1

    def get_diploma(self):
        """Builds info on student's completed course.

        Returns
        -------
        str
            Student's name with completed
            course name.

        Raises
        ------
        StudentCourseError
            Raised if student's course number
            is less than 3.

        """

        if self.course_num < 3:
            raise StudentCourseError('Student not have degree')

        return f'{self.full_name},{self.course_name}'
