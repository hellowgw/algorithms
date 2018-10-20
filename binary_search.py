#!/bin/env python

def search_number(sum_list, guess):
    count = 0 
    low_index = 0
    high_index = len(sum_list)-1
    while low_index <= high_index:
        count = count + 1
        print('查找第{}次'.format(count))
        mid = int((low_index + high_index)/2)
        print('最小索引值为{}，数值为{}'.format(low_index,sum_list[low_index]))
        print('中间索引值为{}, 数值为{}'.format(mid,sum_list[mid]))
        print('最大索引值为{}，数值为{}'.format(high_index,sum_list[high_index]))
        if guess < sum_list[mid]:
            high_index = mid -1
        elif guess > sum_list[mid]:
            low_index = mid +1
        else:
            return mid

s_list = []
for i in range(100):
    s_list.append(i)

print(search_number(s_list, 41))


        

