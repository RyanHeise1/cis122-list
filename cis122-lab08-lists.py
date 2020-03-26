'''
CIS 122 Winter 2020 Lab 8
Author: Ryan Heise
Partner: None
Description: Generate a Random Integer List
'''

import random


def gen_random_integer_list(num, start_range = 1, end_range = 100, sort_list = 'N'):
    """
    Args:
    num(int): num of grades in list
    start_range(): min grade from RNG
    end_range(): max grade from RNG
    sort_list(): if the list need to be sorted  
    """
    # declaring empty list for return
    t = []
    # safty measure
    if num <= 0:
        # List cant have neg num of elements
        print('num must be > 0')
    elif not isinstance(num, int):
       print('num must be an integer')
    elif not isinstance(start_range, int) or not isinstance(end_range, int):
       print('start_range and end_range must be integers')
    # input random numbers
    else:
        for i in range(num):
            r = random.randint(start_range, end_range)
            t.append(r)
    if sort_list.upper() == 'Y':
        t.sort()
    return t


def get_high_score(t):
    if not isinstance(t, list):
        print("List argument expected")
    elif len(t) > 0:
        new_t = t[-1]
        new_t.sort()
        score = new_t[-1]
    return score


def get_low_score(t):
    if not isinstance(t, list):
        print("List argument expected")
    elif len (t) > 0:
        new_t = t[:]
        new_t.sort()
        score = new_t[0]
    return score


def get_mean_score(t):
    if not isinstance(t, list):
        print("List argument expected")
        return 
    find_sum = sum(t)
    mean = len(t) / find_sum
    return("Mean is " + str(round(mean, 2)))


def get_median_score(t):
    t_len = len(t)
    t.sort()
    if not isinstance(t, list):
        print("List argument expected")
        return (-1)
    if t_len % 2 == 0:
        median_right = int(t_len / 2)
        median_left = median_right - 1
        median = median_right + median_left / 2
    else:
        median = t[t_len / 2]
    return("Median is " + str(round(median,2)))


def count_range(t, high, low):
    if not isinstance(t,list):
        print("List argument expected")
        return -1
    if len(t) == 0:
        return 0
    if not isinstance(high ,int) or not isinstance(low ,int):
        print("start and end must be integers")
        return -1
    if high >= low:
        print("start must be < end")
        return -1
    count = 0
    for i in t:
        if i >= high and i <= low:
            count += 1
    return count

def grade_range_counts(t):
    print("A -",count_range(t,90,100))
    print("B -",count_range(t,80,89))
    print("C -",count_range(t,70,79))
    print("D -",count_range(t,60,69))
    print("F -",count_range(t,0,59))

t = gen_random_integer_list(100)
grade_range_counts(t)
