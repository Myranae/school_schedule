from school_schedule.student import Student

def test_check_attributes_correctly_set():
    # arrange
    # ???

    # act
    student = Student(
                "Quinn", 
                "junior", 
                [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ])

    # assert
    # assert student
    assert student.name == "Quinn"
    assert student.grade == "junior"
    assert student.classes == [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ]

def test_get_num_classes_returns_correct_length():
    # arrange
    sabrina = Student("Sabrina", "Junior", [
                    "Pre-Calc", 
                    "English III", 
                    "World History", 
                    "Gym", 
                    "Chemistry", 
                    "Music Composition"
                ])
    # act 
    results = sabrina.get_num_classes()

    # assert
    assert  results == 6

def test_empty_class_list_returns_none():
    # arrange
    sabrina = Student("Sabrina", "Junior", [
                ])
    # act 
    results = sabrina.get_num_classes()

    # assert
    assert  results == None