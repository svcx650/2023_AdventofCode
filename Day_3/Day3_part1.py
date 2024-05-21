# note on syntax in this script:
# number == digit ('4')
# full number = sequential digits ('467')
# part number = full number that is adjacent to a symbol

def find_numberAndSymbol_indices(input_string):
	index = 0
	digit = None
	# number_indices = []
	number_start_indices = []
	number_stop_indices = []
	symbol_indices = []
	last_number_index = None
	for char in input_string:
		digit = '' # this fucking guy
		if char == '.':
			if last_number_index not in number_stop_indices and last_number_index != None:
				number_stop_indices.append(last_number_index)
				last_number_index = None
			index += 1
			continue
		try:
			digit = int(char)
		except ValueError:
			if last_number_index not in number_stop_indices and last_number_index != None:
				number_stop_indices.append(last_number_index)
				last_number_index = None
			symbol_indices.append(index) #we know it's a symbol, now record index in symbol_indices
		if type(digit) == int:
			if last_number_index == None:
				number_start_indices.append(index)
				# print(char)
				# print(index)
				# print(number_start_indices)
				# print('last_number_index was: ', last_number_index)
				last_number_index = index
				# print('last_number_index now: ', last_number_index)
			else:
				last_number_index = index
		index += 1
	if last_number_index not in number_stop_indices and last_number_index != None: number_stop_indices.append(last_number_index)
	return number_start_indices , number_stop_indices, symbol_indices

def isitaPN(start_index, stop_index, current_string_symbol_indices, previous_string_symbol_indices, next_string_symbol_indices):
	#check if numbers are adjacent to a symbol in current line
	if start_index-1 in current_string_symbol_indices or stop_index+1 in current_string_symbol_indices: return start_index, stop_index
	
	#check if numbers indexes meet criteria that are 'adjacent to symbol in previous line'
	if previous_string_symbol_indices != None:
		for index in range(start_index-1, stop_index+2):
			if index in previous_string_symbol_indices: return  start_index, stop_index
	
	#check if numbers indexes meet criteria that are 'adjacent to symbol in next line'
	if next_string_symbol_indices != None:
		for index in range(start_index-1, stop_index+2):
			if index in next_string_symbol_indices: return  start_index, stop_index
	return None, None

def fullnumber_from_indices(start_index, stop_index, line):
	fullnumber = ''
	for i in range(start_index, stop_index+1):
		 fullnumber = fullnumber + line[i]
	return int(fullnumber)


inputtextfile = open('input.txt', 'r')
read_inputs = inputtextfile.read()
read_inputs.replace('\n', ', ')
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

####### test the example here ########
# lines = [
# 	'467..114..',
# 	'...*......',
# 	'..35..633.',
# 	'......#...',
# 	'617*......',
# 	'.....+.58.',
# 	'..592.....',
# 	'.....*755.',
# 	'..........',
# 	'*664.598*.'
# 	]

# lines = [
# 	'...733.......289..262.....520..................161.462..........450.........................183.............................................',
# 	'....*....................*.............707.352....*............/.....................801...@...............333..196........484.635......287.',
# 	'....42.........131....913..............*......&..........634..................440..&...............83.....@...........404$..=....*..423.*...',
# 	'618.......272....*.........&......547.344...............#............689.589.*....150......382=................................168......433.',
# 	'..........=...............253.102*.........#......78.......804..........*........................858.........................-..............',
# 	'...69.......*37...510.797...........596.946........#..................................602.175...............203..100..........681.......546.'
# 	] #13542 expected

partnumbers = []
for line in lines:
	#Check if we're on the first/last line:
	current_line_index = lines.index(line)
	if current_line_index != 0: previous_line = lines[current_line_index-1]
	else:
		previous_line = None
		pl_start_indices = None
		pl_stop_indices = None
		pl_symbols = None
	if current_line_index != len(lines)-1: next_line = lines[current_line_index+1]
	else:
		next_line = None
		nl_start_indices = None
		nl_stop_indices = None
		nl_symbols = None
	
	#get indices of numbers and symbols
	cl_start_indices, cl_stop_indices, cl_symbols = find_numberAndSymbol_indices(line)
	# For the following 2 lines: we don't need previous/next line start/stop indices (4 lists total), but splitting the function into symbols and start/stop indices is more work.
	if previous_line != None: pl_start_indices, pl_stop_indices, pl_symbols = find_numberAndSymbol_indices(previous_line)
	if next_line != None: nl_start_indices, nl_stop_indices, nl_symbols = find_numberAndSymbol_indices(next_line)

	# if current_line_index % 1 == 0:
	# 	print(line)
	# print('line: ', line)
	# print('number start indices: ', cl_start_indices)
	# print('number stop indices: ', cl_stop_indices)
	# print('symbol indices: ', cl_symbols)
	
	for i in cl_start_indices:
		#figure out if each option is a pn or not
		pn_start_index, pn_stop_index = None, None
		start_index = i
		stop_index = cl_stop_indices[cl_start_indices.index(i)]
		pn_start_index, pn_stop_index = isitaPN(start_index, stop_index, cl_symbols, pl_symbols, nl_symbols)
		# print(partnumbers)
		if pn_start_index == None: continue #skip if the full number is not a part number
		partnumbers.append(fullnumber_from_indices(pn_start_index, pn_stop_index, line)) #add part number to list of part numbers

	# if current_line_index % 5 == 0: print(partnumbers)

output = sum(partnumbers)
print(partnumbers)
print('output: ', output)
inputtextfile.close()

#incorrect answers: 485441