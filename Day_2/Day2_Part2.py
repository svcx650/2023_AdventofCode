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

output = 0 #sum of powers
# format data
for line in lines:
	game = line.split(': ')
	gameid = int(game[0][5:])
	pulls = game[1].split('; ')
	red = []
	green = []
	blue = []
	for result in pulls:
		results = result.split(', ')
		for cube in results:
			if cube.endswith('red'):
				red.append(int(cube[:-4]))
			elif cube.endswith('green'):
				green.append(int(cube[:-6]))
			elif cube.endswith('blue'):
				blue.append(int(cube[:-5]))
	print(red)
	print(green)
	print(blue)
	minimumcubes = [max(red), max(green), max(blue)]
	powers = minimumcubes[0]*minimumcubes[1]*minimumcubes[2]
	print(minimumcubes)
	output += powers

print('output: ', output)
inputtextfile.close()