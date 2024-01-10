#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    k1sum = 0
    if my_list:
        for k in list(my_list):
            sum += (k[0] * k[1])
            k1sum += k[1]
        return (sum / k1sum)
    else:
        return (0)
