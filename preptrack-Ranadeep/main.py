"""
Student Name Validation Module for PrepTrack.
"""

def validate_student_name(name: str) -> str:
    """
    Validates that a student name is non-empty and valid.

    Args:
        name (str): The student name to validate.

    Returns:
        str: The stripped, validated student name.

    Raises:
        ValueError: If the student name is None, empty, or consists only of whitespace.
        TypeError: If the provided name is not a string.
    """
    if name is None:
        raise ValueError("Student name cannot be None.")
    
    if not isinstance(name, str):
        raise TypeError(f"Student name must be a string, got {type(name).__name__}.")
    
    trimmed_name = name.strip()
    if not trimmed_name:
        raise ValueError("Student name cannot be empty or contain only whitespace.")
    
    return trimmed_name


def is_valid_student_name(name: str) -> bool:
    """
    Helper function to check if a student name is non-empty without raising exceptions.

    Args:
        name (str): The student name to check.

    Returns:
        bool: True if the name is valid and non-empty, False otherwise.
    """
    try:
        validate_student_name(name)
        return True
    except (ValueError, TypeError):
        return False


if __name__ == "__main__":
    student_name = input("Enter student name: ")
    while not student_name.strip():
        print("Student name cannot be empty.\n")
        student_name = input("Enter student name: ")

    print(f"Validated Student Name: {student_name}")

