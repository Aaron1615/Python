def recursive_reverse_string(string):
    """Returns a reversed string"""
    if len(string) <= 1:
        return string
    else:
        return recursive_reverse_string(string[1:]) + string[0]
