from store import store
class Teacher:
    def __init__(self, name = '', hometown = '', school = ''):
        store['teacher_counter'] += 1
        store['teachers'].append(self)
        self._name = name
        self._hometown = hometown
        if school:
            self._school_id = school.id
        self._id = store['teacher_counter']

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def hometown(self):
        return self._hometown

    @property
    def school(self):
        return self._school_id

