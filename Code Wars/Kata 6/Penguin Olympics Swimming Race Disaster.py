def calculate_winners(snapshot, penguins):

    # total distance
    total_distance_left = []
    for i in snapshot.split():
        n = -1
        for step in list(i):
            n = n + 1
            if (step == 'p') or (step == 'P'):
                new_list = list(i)[n+1:]
                distance = 0
                for element in new_list:
                    if element == '-':
                        distance += 1
                    elif element == '~':
                        distance += 2
                    else:
                        total_distance_left.append(distance)

    # defining best three penguins
    count = 0
    winner_list = []
    while count < 3:
        index_min = min(range(len(total_distance_left)), key=total_distance_left.__getitem__)
        winner_list.append(penguins[index_min])
        del total_distance_left[index_min]
        del penguins[index_min]
        count = count+1
    return f'GOLD: {winner_list[0]}, SILVER: {winner_list[1]}, BRONZE: {winner_list[2]}'
