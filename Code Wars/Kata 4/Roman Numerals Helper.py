class RomanNumerals:

    def __init__(self):
        self.numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    def to_roman(self, arabic_number):
        roman_number_list = []
        index = 0
        for _ in self.numerals:
            if (arabic_number >= 900) and (arabic_number < 1000):
                roman_number_list.append('CM')
                arabic_number -= 900
            elif (arabic_number >= 90) and (arabic_number < 100):
                roman_number_list.append('XC')
                arabic_number -= 90
            elif (arabic_number >= 40) and (arabic_number < 50):
                roman_number_list.append('XL')
                arabic_number -= 40
            elif arabic_number == 9:
                roman_number_list.append('IX')
                arabic_number -= 9
            elif arabic_number == 4:
                roman_number_list.append('IV')
                arabic_number -= 4
            else:
                while arabic_number >= self.numerals[_]:
                    roman_number_list.append(_)
                    arabic_number = arabic_number - self.numerals[_]
            index += 1
        return ''.join(roman_number_list)

    def from_roman(self, roman_number):
        year = 0
        new_list = []
        for x in roman_number:
            new_list.append(self.numerals[x])
        new_list.append(0)
        for x in range(len(new_list)-1):
            if new_list[x] < new_list[x+1]:
                year -= new_list[x]
            else:
                year += new_list[x]
        return year

r = RomanNumerals()
print(r.from_roman('CCL'))
print(r.to_roman(1000))