import re

def HaveForbidenSymbols(password):
    digitsList = re.findall(r"[^a-z0-9]", password, re.IGNORECASE)
    if len(digitsList) > 0:
        print ("Password have forbidden symbols")
        return True
    return False

def HassUpperAndLowerCaseChars(password):
    if ((password.isupper) and (password.islower)):
        print ("Password has upper- and lower-case chars")
        return True
    return False

def OnlyDigits(password):
    digitsList = re.findall(r"[0-9]", password)
    if len(digitsList) == len(password):
        print ("password has only digits")
        return True
    return False

def HassOneOrMoreDigits(password):
    digitsList = re.findall(r"[0-9]", password)
    if len(digitsList) > 0:
        print ("Password has one or more digits")
        return True
    return False

def get_password_strength(password):
    if (HaveForbidenSymbols(password)):
        return 0
    strength = 1
    if OnlyDigits(password):
        return strength
    strength += 1
    if HassUpperAndLowerCaseChars(password):
        strength += 1
    if HassOneOrMoreDigits(password):
        strength += 1
    return strength
    pass


if __name__ == '__main__':
    print ("Please input your password")
    strengthLevel = get_password_strength(input())
    print (str(strengthLevel))
