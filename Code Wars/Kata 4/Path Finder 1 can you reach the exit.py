maze = "\n".join([
  "."
])

# convert string into table
def convert(a):
    row = []
    table = []
    counter = 0
    row_counter = 0
    column_counter = 0
    for x in a:
        column_counter += 1
        counter += 1
        if counter == len(a):
            row.append('END')
            table.append(row)
            row_counter += 1
        elif x != '\n':
            row.append(x)
        elif x == '\n':
            table.append(row)
            row = []
            row_counter += 1
            column_counter = 0
    return (table,row_counter,column_counter)


# create extra layer    ooooo
#                       oxxxo
#                       ooooo
def borderline(table,number_of_rows,number_of_columns):
    zero_row = []
    counter = 0
    table_borderlined = []
    if table == [['END']]:
        return table
    while counter < number_of_columns + 2:
        zero_row.append(0)
        counter += 1
    table_borderlined.append(zero_row)
    for i in table:
        side_borderline = [0] + i +[0]
        table_borderlined.append(side_borderline)
    table_borderlined.append(zero_row)
    table_borderlined[1][1] = 1
    return table_borderlined


#path to the end checking
def path_to_the_end(table,rows,columns):
    change_check = 1               # if change_check == 0 all ways were checked
    if table == [['END']]:
        return True
    while change_check > 0:
        change_check = 0
        for index_1, i in enumerate(table):
            for index_2, j in enumerate(list(i)):
                if j == 'END' and ((table[index_1][index_2 - 1] == 1) or (table[index_1][index_2 + 1] == 1) or (table[index_1 - 1][index_2] == 1) or (table[index_1 + 1][index_2] == 1)):
                    return True
                elif j == 'W':
                    table[index_1][index_2] = 2
                    change_check += 1
                    break
                elif j == '.' and ((table[index_1][index_2 - 1] == 1) or (table[index_1][index_2 + 1] == 1) or (table[index_1 - 1][index_2] == 1) or (table[index_1 + 1][index_2] == 1)):
                    table[index_1][index_2] = 1
                    change_check += 1
    return False


def path_finder(maze):
    first_step = convert(maze)
    second_step = borderline(first_step[0],first_step[1],first_step[2])
    third_step = path_to_the_end(second_step, first_step[1], first_step[2])
    return third_step

print(path_finder(maze))