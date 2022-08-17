from code import Teacher, School, store

def test_school_returns_related_school_instance():
    store['teachers'] = []
    store['teacher_counter'] = 0

    store['schools'] = []
    store['school_counter'] = 0
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    teacher = Teacher('Sam Smith', 'NYC', school)
    assert teacher.school() == school