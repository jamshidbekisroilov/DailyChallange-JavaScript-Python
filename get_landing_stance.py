import math as m
def get_landing_stance(start_stance, rotation):
    times = m.floor(abs(rotation) / 180 )
    if times % 2 == 0:
        return start_stance
    else:
        return "Goofy" if start_stance == "Regular" else "Regular"
    


