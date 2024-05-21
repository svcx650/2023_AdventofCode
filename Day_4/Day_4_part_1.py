def string_to_int(string):
    function_output = []
    for number in string.split(' '):
        if number != '': function_output.append(int(number))
    return function_output

lines = list(open('input.txt')) 
### test examples ###
# lines = [
#     'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
#     'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
#     'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
#     'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
#     'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
#     'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
#   ]

output = 0
for line in lines:
    card_number_string, numbers_string = line.split(':')
    winning_numbers_string, my_numbers_string = numbers_string.split('|')
    
    winning_numbers = string_to_int(winning_numbers_string)
    my_numbers = string_to_int(my_numbers_string)
    
    my_winning_numbers = []
    for number in my_numbers:
        if number in winning_numbers: my_winning_numbers.append(number)
    # print(my_winning_numbers)
    points = 1
    for i in range(len(my_winning_numbers)-1):
        points = points*2
    #     print(points)
    # print('final points', points)
    if len(my_winning_numbers) != 0: output += points

print('output: ', output)