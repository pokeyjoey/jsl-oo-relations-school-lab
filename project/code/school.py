from store import store
class School:
    def __init__(self, name = '', address = ''):
        store['schools'].append(self)
        self._id = len(store['schools'])
        self._name = name
        self._address = address

    def name(self):
        return self._name

    def address(self):
        return self._address

    def id(self):
        return self._id

    def students(self):
        students = [student for student in store['students'] if student.school().id() == self.id()]
        return students

    def teachers(self):
        teachers = [teacher for teacher in store['teachers'] if self._id == teacher.school()]
        return teachers
