def is_int(x):
    result = False
    if isinstance(x, int) :
        result = True
    
    return result

def is_none(x):
    if not is_int(x):
        return False

    result = False
    if (x == None):
        result = True
    
    return result

def is_zero(x):
    if not is_int(x):
        return False

    result = False
    if (x == 0):
        result = True
    
    return result

def is_multiple_of_7(x):
    if not is_int(x):
        return False

    result = False
    if (x % 7 == 0):
        result = True
    
    return result
