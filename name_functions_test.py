from name_functions import upper_name


def test_upper_name():
    assert upper_name("John Doe") == "JOHN DOE"    


def test_upper_name_with_empty():
    assert upper_name("") == "N/A"
    


