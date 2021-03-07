import itertools
def sum_arrangements(num):
    new_list = []
    for i in list(itertools.permutations(str(num),len(str(num)))):
        new_list.append(int(''.join(i)))
    return sum(new_list)

#not optimal
print(sum_arrangements(1235556745))