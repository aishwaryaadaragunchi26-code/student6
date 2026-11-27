import sys

def student_details(name, usn, college, city):
    return {
        "name": name,
        "usn": usn,
        "college": college,
        "city": city
    }

if __name__ == "__main__":

    name = sys.argv[1]
    usn = sys.argv[2]
    college = sys.argv[3]
    city = sys.argv[4]

    print("Student Details")
    print("Name:", name)
    print("USN:", usn)
    print("College:", college)
    print("City:", city)

    print(student_details(name, usn, college, city))