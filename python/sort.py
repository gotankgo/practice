import random

def sort(num_list, list_length):
    if list_length <= 1:
        return num_list

    less    = list()
    greater = list()
    equal   = [num_list[0]]

    for i in range(1, list_length):
        num = num_list[i]
        less.append(num) if num < equal[0] else equal.append(num) if num == equal[0] else greater.append(num)

    return sort(less, len(less)) + equal + sort(greater, len(greater))


if __name__ == '__main__':
    text = "input numbers ex: 1,5,2,3....\n"
    input_num_list = [int(x) for x in input(text).split(',')]
    print(sort(input_num_list, len(input_num_list)))
