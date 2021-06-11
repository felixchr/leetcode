#!/usr/bin/env python3

import csv
from math import sqrt
from os import name

GRAVITY=9.8

def get_speed(stride_length, leg_length):
    return ((stride_length/leg_length) - 1) * sqrt(leg_length * GRAVITY)


main_dict = {}

data = csv.reader(open('dataset1.csv'))
main_dict = {line[0]: {'leg_length': float(line[1]), 'diet': line[2]} \
    for line in data if data.line_num != 1}
data = csv.reader(open('dataset2.csv'))
for line in data:
    if data.line_num == 1:
        continue
    if line[0] in main_dict:
        main_dict[line[0]].update({
            'stride_length': float(line[1]),
            'stance': line[2]
        })
    else:
        print('{} is not in list'.format(line[0]))
print(main_dict)

dino_list = [(key, get_speed(value['stride_length'], value['leg_length'])) \
    for key, value in main_dict.items() \
    if 'stride_length' in value and value['stance'] == 'bipedal']
print(dino_list)

dino_list=sorted(dino_list, key=lambda d:d[1], reverse=True)
print('\n'.join([str(dino) for dino in dino_list]))



