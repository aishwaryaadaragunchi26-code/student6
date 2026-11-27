from app import student_details

def test_student_details():
    s = student_details("Asha", "01FE25BCA101", "ABC College", "Hubballi")
    assert s["name"] == "Asha"
    assert s["usn"] == "01FE25BCA101"
    assert s["college"] == "ABC College"
    assert s["city"] == "Hubballi"

