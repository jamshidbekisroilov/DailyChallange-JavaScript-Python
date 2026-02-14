def ski_jump_medal(distance_points, style_points, wind_comp, k_point_bonus):
    arr = [165.5, 172.0, 158.0, 180.0, 169.5, 175.0, 162.0, 170.0]
    sum_all = distance_points + style_points + wind_comp + k_point_bonus;

    arr.append(sum_all)
    new_arr = sorted(arr, reverse=True)
    index_num = new_arr.index(sum_all)
    
    if index_num == 0: return "Gold" 
    elif index_num == 1: return "Silver"
    elif index_num == 2: return "Bronze"
    else: return "No Medal"


