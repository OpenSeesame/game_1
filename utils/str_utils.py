def is_str(x):
    result = False
    if isinstance(x, str) :
        result = True
    
    return result

def is_none(x):
    if not is_str(x):
        return False

    result = False
    if x == None:
        result = True
    
    return result

def is_blank(x):
    if not is_str(x):
        return False

    result = False
    if x == "":
        result = True
    
    return result

def sub(x, y):
    if not is_str(x):
        return {'result':False, 'value':''}
    if is_none(x) or is_blank(x) or is_none(y) or is_blank(y):
        return {'result':False, 'value':''}
    if not x.isdecimal() or not y.isdecimal():
        return {'result':False, 'value':''}

    return {'result':True, 'value':str(int(x) - int(y))}

    