#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return(0)

    tot_score = 0
    tot_weight = 0

    for score, weight in my_list:
        tot_score += score * weight
        tot_weight += weight

    if tot_weight == 0:
        return (0)

    return (tot_score / tot_weight)
