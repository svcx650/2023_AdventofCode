import math

def contains_spelled_digits(input_string,firstorlast):
	found_digit = None
	spelled_digits_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
	if firstorlast == 'first':
		for key in spelled_digits_mapping.keys():
			if input_string.endswith(key):
				found_digit = int(spelled_digits_mapping[key]) 
				break
		# print('contains-first, returning: ', found_digit)
		return found_digit
	elif firstorlast == 'last':
		for key in spelled_digits_mapping.keys():
			if input_string.startswith(key): #swapped endswith for startswith
				found_digit = int(spelled_digits_mapping[key]) 
				break
		# print('contains-last, returning: ', found_digit)
		return found_digit

def find_digit(input_string, firstorlast):
	letters = ''
	digit = None
	if firstorlast == 'first':
		for char in input_string:
			try:
				digit = int(char)
			except ValueError:
				letters = letters + char
				found_digit = contains_spelled_digits(letters, 'first')
				if found_digit != None:
					digit = found_digit
			if type(digit) == int:
				# print('find-first, returning: ', digit)
				return digit
	elif firstorlast == 'last':
		input_string = flip_string(input_string)
		for char in input_string:
			try:
				digit = int(char)
			except ValueError:
				letters = letters + char
				found_digit = contains_spelled_digits(flip_string(letters),'last')
				if found_digit != None:
					digit = found_digit
			if type(digit) == int:
				# print('find-last, returning: ', digit)
				return digit

def flip_string(forward_string):
	backwards_string = forward_string[::-1]
	return backwards_string

inputtextfile = open('input.txt', 'r')
read_inputs = inputtextfile.read()
read_inputs.replace('\n', ', ')
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

####### test the example here ########
# lines = [
# 	'two1nine',
# 	'eightwothree',
# 	'abcone2threexyz',
# 	'xtwone3four',
# 	'4nineeightseven2',
# 	'zoneight234',
# 	'7pqrstsixteen'
# 	]

output = 0
for line in lines:
	# print('startingfirstint')
	first_int = find_digit(line, 'first')
	# print('finished firstint: ', first_int)
	last_int = find_digit(line, 'last')
	# print('finished last_int: ', last_int)
	calibration = str(first_int) + str(last_int)
	print(calibration)
	output += int(calibration)

print('output: ', output)
inputtextfile.close()