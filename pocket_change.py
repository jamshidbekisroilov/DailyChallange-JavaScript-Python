def count_change(change):
    sumAll = 0
    for i in change:
        sumAll += i
    total = round(sumAll/100, 2)
    return f"${total:.2f}"
#Demo test
print(count_change([10, 5, 1, 10, 1, 25, 1, 1, 5, 1, 10]))

