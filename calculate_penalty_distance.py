def calculate_penalty_distance(rounds):

    return sum(max(0, 5 - n) for n in rounds) * 150
#Demo test:
print(calculate_penalty_distance([4, 4]))


