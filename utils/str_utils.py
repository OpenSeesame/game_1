import unicodedata
from constants.constants import Constants

class StrUtils:
    def is_str(x):
        result = False
        if isinstance(x, str) :
            result = True
        
        return result

    def is_none(x):
        if not StrUtils.is_str(x):
            return False

        result = False
        if x == None:
            result = True
        
        return result

    def is_blank(x):
        if not StrUtils.is_str(x):
            return False

        result = False
        if x == "":
            result = True
        
        return result

    def sub(x, y):
        if not StrUtils.is_str(x):
            return {'result':False, 'value':''}
        if StrUtils.is_none(x) or StrUtils.is_blank(x) or StrUtils.is_none(y) or StrUtils.is_blank(y):
            return {'result':False, 'value':''}
        if not x.isdecimal() or not y.isdecimal():
            return {'result':False, 'value':''}

        return {'result':True, 'value':str(int(x) - int(y))}

    def  len(text):
        count = 0
        for c in text:
            if unicodedata.east_asian_width(c) in Constants.FWA:
                count += 2
            else:
                count += 1
        return count