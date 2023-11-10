class Student:
    def __init__(self, first_name, last_name, course, avg_mark):
        if not(len(first_name) >= 3 and isinstance(first_name, str)):
            raise Exception('First name should be a string and have more than two letters')
        self.first_name = first_name
        if not(len(last_name) >= 3 and isinstance(last_name, str)):
            raise Exception('Last name should be a string and have more than two letters')
        self.last_name = last_name
        if not(1 <=course <=6 and isinstance(course, int)):
            raise Exception('Course should be in range from 1 to 6 and be int')
        self.course = course
        self.avg_mark = avg_mark

    def __str__(self):
        return f'First name:{self.first_name}, Last name:{self.last_name}, Course:{self.course}, Avg mark:{self.avg_mark}'
