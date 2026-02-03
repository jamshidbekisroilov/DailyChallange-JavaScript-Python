def groundhog_day_prediction(appearance):
    if type(appearance) is not bool:
        return "No prediction this year."
    elif appearance == True:
        return "Looks like we'll have six more weeks of winter."
    return "It's going to be an early spring."
#Demo test
print(groundhog_day_prediction("False"))#Output: No prediction this year.
print(groundhog_day_prediction(True))#Output: Looks like we'll have six more weeks of winter.
print(groundhog_day_prediction(False))#Output: It's going to be an early spring.
