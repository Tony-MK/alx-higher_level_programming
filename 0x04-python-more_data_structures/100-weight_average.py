#!/usr/bin/python3
def weight_average(my_list):
    weights_sum: int = sum(map(lambda x: x[1], my_list))
    return sum(map(lambda x: x[0] * x[1], my_list)) / weights_sum
