def cinema(b, g):
    seattable = []
    if b > 2*g:
        return None
    elif g > 2*b:
        return None
    else :
        while (b>0) or (g>0):
            if (b >= g) and (b >= 2):
                seattable.append('BGB')
                b = b-2
                g = g-1
            elif (g >= b) and (g >= 2):
                seattable.append('GBG')
                b = b-1
                g = g-2
            elif g==b:
                seattable.append('GB')
                g = g - 1
                b = b - 1
            elif (g == 1) and (g > b):
                seattable.append('G')
                g = g-1
            else :
                seattable.append('B')
                b = g-1
    return ''.join(seattable)

print(cinema(7,8))