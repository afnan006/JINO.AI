# import uuid

# def generate_uuid():
#     return str(uuid.uuid4())


import uuid

def generate_uuid():
    """
    Generates a new UUID and returns it as a string.
    """
    return str(uuid.uuid4())

def validate_uuid(uuid_str):
    """
    Validates if the given string is a valid UUID.
    Returns True if valid, False otherwise.
    """
    try:
        # Try converting the string to a UUID object
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str  # Ensure the string matches the UUID format
    except ValueError:
        return False
