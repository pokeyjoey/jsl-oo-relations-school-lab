from code import Student, School, store

def test_can_create_student():
    assert type(Student()) == Student

def test_initializes_with_name():
    student = Student('Sam Smith')
    assert student._name ==  'Sam Smith'

def test_initializes_with_hometown():
    student = Student('Sam Smith', 'NYC')
    assert student._hometown ==  'NYC'

def test_name_returns_name():
    student = Student('William Tennent', '125 Maple Road')
    assert student.name ==  'William Tennent'

def test_address_return_address():
    student = Student('Sam Smith', 'NYC')
    assert student.hometown ==  'NYC'

def test_initializing_a_student_increments_an_underscore_id():
    # reset store
    store['students'] = []
    store['student_counter'] = 0
    # done resetting store

    student = Student('Sam Smith', 'NYC')
    assert student._id == 1

    new_student = Student('Ben Kingsley', 'Philadelphia')
    assert new_student._id == 2

def test_id_returns_id():
    # reset store
    store['students'] = []
    store['student_counter'] = 0
    # done resetting store
    student = Student('Sam Smith', 'NYC')
    assert student.id == 1

def test_initializing_a_student_adds_a_new_student_to_the_store():
    store['students'] = []
    store['student_counter'] = 0
    # done resetting store
    student = Student('Sam Smith', 'NYC')
    assert store['students'][0] == student

def test_school_id_stored_as_attribute():
    store['students'] = []
    store['student_counter'] = 0

    store['schools'] = []
    store['school_counter'] = 0
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    student = Student('Sam Smith', 'NYC', school)
    assert student._school_id == 1

def test_school_returns_related_school_instance():
    store['students'] = []
    store['student_counter'] = 0

    store['schools'] = []
    store['school_counter'] = 0
    # done resetting store
    school = School('Tennent', '125 Maple Ave')
    student = Student('Sam Smith', 'NYC', school)
    assert student.school() == school