from store import store
class Student:
    def __init__(self, name = '', hometown = '', school = ''):  
        store['students'].append(self)
        self._id = len(store['students'])
        self._name = name
        self._hometown = hometown
        self._school = school

    def name(self):
        return self._name

    def hometown(self):
        return self._hometown

    def school(self):
        return self._school

    def id(self):
        return self._id
