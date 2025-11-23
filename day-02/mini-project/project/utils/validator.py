def validate_id(student_id):
    return isinstance(student_id, int) and student_id > 0


def validate_name(name):
    return isinstance(name, str) and len(name.strip()) > 0


def validate_age(age):
    return isinstance(age, int) and 3 <= age <= 120
