# class Game():
# 	def __init__(self, name):
# 		self.name = name

# 	def subset(self, red, green, blue):
# 		self.red = red
# 		self.green = green
# 		self.blue = blue

inputtextfile = open('input.txt', 'r')
read_inputs = inputtextfile.read()
read_inputs.replace('\n', ', ')
with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

####### test the example here ########
# lines = [
# 	'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
# 	'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
# 	'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
# 	'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
# 	'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
# 	]

output = 0 #summed game IDs that meet the conditions
# format data
for line in lines:
	game = line.split(': ')
	gameid = int(game[0][5:])
	pulls = game[1].split('; ')
	passorfail = []
	for result in pulls:
		results = result.split(', ')
		# print('results: ',results)
		for cube in results:
			# print(cube)
			if cube.endswith('red'):
				if int(cube[:-4])<=12:
					passorfail.append('pass')
				else:
					passorfail.append('fail')
			if cube.endswith('green'):
				if int(cube[:-6])<=13:
					passorfail.append('pass')
				else:
					passorfail.append('fail')
			if cube.endswith('blue'):
				if int(cube[:-5])<=14:
					passorfail.append('pass')
				else:
					passorfail.append('fail')
	print(passorfail)
	for i in passorfail:
		if i == 'fail': gameid = 0
	output += gameid

print('output: ', output)
inputtextfile.close()