def find_numberAndstar_indices(input_string):
	index = 0
	digit = None
	# number_indices = []
	number_start_indices = []
	number_stop_indices = []
	star_indices = []
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
			if char == '*': star_indices.append(index)
		if type(digit) == int:
			if last_number_index == None:
				number_start_indices.append(index)
				last_number_index = index
			else:
				last_number_index = index
		index += 1
	if last_number_index not in number_stop_indices and last_number_index != None: number_stop_indices.append(last_number_index)
	return number_start_indices , number_stop_indices, star_indices

def find_number_start_index(foundintegerindex, start_indices, stop_indices):
	for i in stop_indices:
		lastvalue = stop_indices.index(i)
		if i >= foundintegerindex: break
	return start_indices[lastvalue]

def isitagear(symbol_index, current_start_indices, current_stop_indices, previous_start_indices, previous_stop_indices, previous_line, next_start_indices, next_stop_indices, next_line):
	#check if stars are adjacent to a number in current line
	# print('symbol_index: ', symbol_index)
	output_start_indices = []
	output_line_offset = []
	
	if symbol_index-1 in current_stop_indices: 
		output_start_indices.append(find_number_start_index(symbol_index-1, current_start_indices, current_stop_indices))
		output_line_offset.append(0)
	
	if symbol_index+1 in current_start_indices:
		output_start_indices.append(find_number_start_index(symbol_index+1, current_start_indices, current_stop_indices))
		output_line_offset.append(0)
	
	#check if numbers indexes meet criteria that are 'adjacent to star in previous line'
	if previous_start_indices != None:
		found_integers = []
		for char in previous_line[symbol_index-1:symbol_index+2]:
			digit = ''
			try:
				digit = int(char)
			except ValueError:
				found_integers.append(None)
			if type(digit) == int:
				found_integers.append(digit)
		found_integer_start_indices = []
		for foundinteger_indexoffset, foundinteger in enumerate(found_integers):
			if foundinteger == None: continue
			foundinteger_index = foundinteger_indexoffset+symbol_index-1 #this is the index of the found integer in the original line
			found_integer_start_indices.append(find_number_start_index(foundinteger_index, previous_start_indices, previous_stop_indices))
		unique_found_integer_start_indices = []
		for item in found_integer_start_indices: # remove duplicate start indices from multiple digits of same number found
			if item not in unique_found_integer_start_indices:
				unique_found_integer_start_indices.append(item)
		for item in unique_found_integer_start_indices:
			output_start_indices.append(item)
			output_line_offset.append(-1)

	#check if numbers indexes meet criteria that are 'adjacent to star in next line'
	if next_start_indices != None:
		found_integers = []
		for char in next_line[symbol_index-1:symbol_index+2]:
			digit = '' #this fucking guy, AGAIN
			try:
				digit = int(char)
			except ValueError:
				found_integers.append(None)
			if type(digit) == int:
				found_integers.append(digit)
		found_integer_start_indices = []
		for foundinteger_indexoffset, foundinteger in enumerate(found_integers):
			if foundinteger == None: continue
			foundinteger_index = foundinteger_indexoffset+symbol_index-1 #this is the index of the found integer in the original line
			found_integer_start_indices.append(find_number_start_index(foundinteger_index, next_start_indices, next_stop_indices))
		unique_found_integer_start_indices = []
		for item in found_integer_start_indices: # remove duplicate start indices from multiple digits of same number found
			if item not in unique_found_integer_start_indices:
				unique_found_integer_start_indices.append(item)
		for item in unique_found_integer_start_indices:
			output_start_indices.append(item)
			output_line_offset.append(1)

	if len(output_start_indices) > 2:
		print('too many values in output_start_indices.')
		return None, None #return nothing if only 1 (or more than 2) adjacent number(s) are found
	elif len(output_start_indices) < 2:
		return None, None
	else: return output_start_indices, output_line_offset

def stopindex_from_startindex(start_index, line):
	index = start_index
	for char in line[start_index:]:
			digit = ''
			try:
				digit = int(char)
			except ValueError:
				break
			index += 1
	stop_index = index-1
	return stop_index

def fullnumber_from_indices(start_index, stop_index, line):
	fullnumber = ''
	for i in range(start_index, stop_index+1):
		 fullnumber = fullnumber + line[i]
	return int(fullnumber)

###### inputs #####
lines = list(open('input.txt')) # actual input file
# example/tests
# lines = [
# 	'805.559...',
# 	'...*......',
# 	'......633.',
# 	'......#...',
# 	'617.......',
# 	'.....+.58.',
# 	'..592.....',
# 	'......755.',
# 	'...$.*....',
# 	'.664.598..'
# 	]

# lines = [
# 	'467*1*114.',
# 	'..........',
# 	'...5..633.',
# 	'......#...',
# 	'617*......',
# 	'.....+.58.',
# 	'..592.....',
# 	'......755.',
# 	'...$.*....',
# 	'.664.598..'
# 	]
# expect: 452071

# lines = [
# 	'.35..114..',
# 	'...*......',
# 	'..35..633.',
# 	'......#...',
# 	'617*.....',
# 	'.....+.58.',
# 	'..592.....',
# 	'......755.',
# 	'...$.*....',
# 	'.664.598..'
# 	]
#expect: 452715

gearratios = []
for line in lines:
	current_line_index = lines.index(line)
	
	#Check if we're on the first/last line:
	if current_line_index != 0: previous_line = lines[current_line_index-1]
	else:
		previous_line = None
		pl_start_indices = None
		pl_stop_indices = None
		pl_stars = None
	if current_line_index != len(lines)-1: next_line = lines[current_line_index+1]
	else:
		next_line = None
		nl_start_indices = None
		nl_stop_indices = None
		nl_stars = None
	
	#get indices of numbers and stars
	cl_start_indices, cl_stop_indices, cl_stars = find_numberAndstar_indices(line)
	# For the following 2 lines: we don't need previous/next line start/stop indices (4 lists total), but splitting the function into stars and start/stop indices is more work.
	if previous_line != None: pl_start_indices, pl_stop_indices, pl_stars = find_numberAndstar_indices(previous_line)
	if next_line != None: nl_start_indices, nl_stop_indices, nl_stars = find_numberAndstar_indices(next_line)
				# variable prefixes:
				# cl = current line
				# pl = previous line
				# nl = next line

	for star in cl_stars:
		output_start_indices, output_line_offset = None, None
		output_start_indices, output_line_offset = isitagear(star, cl_start_indices, cl_stop_indices, pl_start_indices, pl_stop_indices, previous_line, nl_start_indices, nl_stop_indices, next_line)
		# print('isitagear() outputs: ', output_start_indices, output_line_offset)
		if output_start_indices != None:
			if output_start_indices[1] == None: continue #skip if the star is not a gear
			
			# convert output_line_offset from offset values to the indicated lines
			output_lines = []
			for i in output_line_offset:
				if i == 0: output_lines.append(line)
				elif i == -1: output_lines.append(previous_line)
				elif i == 1: output_lines.append(next_line)
			
			#get stop indices
			output_stop_indices = []
			for i in range(0, len(output_start_indices)):
				a = stopindex_from_startindex(output_start_indices[i], output_lines[i])
				output_stop_indices.append(a)

			#find gear values and multiply
			gear_value_1 = fullnumber_from_indices(output_start_indices[0], output_stop_indices[0], output_lines[0])
			# print('gear_value_1', gear_value_1)
			gear_value_2 = fullnumber_from_indices(output_start_indices[1], output_stop_indices[1], output_lines[1])
			# print('gear_value_2',gear_value_2)
			gear_ratio = gear_value_1*gear_value_2
			gearratios.append(gear_ratio)

output = sum(gearratios)
print('len(gearratios)', len(gearratios))
print('output: ', output)