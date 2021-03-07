def valid_parentheses(string):
    bra = 0
    ket = 0
    for _ in list(string):
        if bra >= ket:
            if _ == '(':
                bra = bra + 1
            elif _ == ')':
                ket = ket + 1
        elif ket > bra:
            return False
    if bra == ket:
        return True
    else:
        return False
