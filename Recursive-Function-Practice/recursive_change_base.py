def recursive_change_base(number, base):
    """Takes a number and a base as inputs, returning
    that number in the base's system"""
    num_to_str = "0123456789ABCDEF"
    if number <= base:
        return num_to_str[number]
    else:
        return recursive_change_base(number//base, base) + num_to_str[number%base] 

