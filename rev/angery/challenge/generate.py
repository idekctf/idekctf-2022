import time
import random
import os
import subprocess
from string import printable

template = '''#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void lose() @
	printf("No!");
	exit(-1);
~

void win() @
	printf("Yes!");
	exit(1);
~

int main() @
	char inp[100], is_correct = 1;
	memset(inp, 0, sizeof(inp));
	int dummy = read(0, inp, 80);
	inp[strlen(inp) - 1] = 0;

	if (strlen(inp) != 60) lose();

{}

	if (is_correct) win();
	else lose();

	return 0;
~
'''

printable = printable[:-6]
ans = ''

# random.seed(time.time()*100000)

for i in range(60):
	ans += printable[random.randint(0, len(printable)-1)]

inp = ans.encode()
freq = [2] * len(ans)

def is_stop():
	for i in freq:
		if i != 0: return 0
	return 1

fill = ''
sus_2 = [4, 8]

while is_stop() == 0:
	x = []
	for i in range(3):
		char_id = random.randint(0, len(ans)-1)
		while char_id in x or freq[char_id] == 0:
			char_id = (char_id + 1) % len(ans)
		x.append(char_id)
		freq[char_id] -= 1
		if is_stop(): break

	cou = 0
	summ = 0 
	crit_id = -1

	for i in range(len(freq)):
		if freq[i] != 0:
			cou += 1
			summ += freq[i]
			if freq[i] == 2:
				crit_id = i
	if cou < 3 and summ == 3:
		if freq[crit_id] == 2:
			x.append(crit_id)
		freq = [0]

	statement = ''

	# add sus_2 to spice things up
	option = random.randint(0, 3)
	if option == 0:
		statement = 'is_correct &= ((inp[{0}] _0 inp[{1}] _1 inp[{2}]) == _2);'.format(x[0], x[1], x[2])
	elif option == 1:
		statement = 'is_correct &= ((inp[{0}] % {3} _0 inp[{1}] _1 inp[{2}]) == _2);'.format(x[0], x[1], x[2], sus_2[random.randint(0, len(sus_2) - 1)])
	elif option == 2:
		statement = 'is_correct &= ((inp[{0}] _0 inp[{1}] % {3} _1 inp[{2}]) == _2);'.format(x[0], x[1], x[2], sus_2[random.randint(0, len(sus_2) - 1)])
	elif option == 3:
		statement = 'is_correct &= ((inp[{0}] _0 inp[{1}] _1 inp[{2}] % {3}) == _2);'.format(x[0], x[1], x[2], sus_2[random.randint(0, len(sus_2) - 1)])
	elif option == 3:
		statement = 'is_correct &= ((inp[{0}] % {4} _0 inp[{1}] _1 inp[{2}] % {3}) == _2);'.format(x[0], x[1], x[2], sus_2[random.randint(0, len(sus_2) - 1)], sus_2[random.randint(0, len(sus_2) - 1)])

	for i in range(2):	# choose arithmetic
		# 0 for +, 1 for -, 2 for *, 3 for %
		x = random.randint(0, 3)
		if x == 0:
			statement = statement.replace('_' + str(i), '+')
		elif x == 1:
			statement = statement.replace('_' + str(i), '-')
		elif x == 2:
			statement = statement.replace('_' + str(i), '*')
		elif x == 3:
			statement = statement.replace('_' + str(i), '%')
		# print(x)

	t = statement[statement.find('(('):statement.find(') ==')][2:]
	hehe = eval(t)

	statement = statement.replace('_2', str(hehe))
	# print(statement)
	fill += '\t' + statement + '\n'

template = template.format(fill)
template = template.replace('@', '{')
template = template.replace('~', '}')
# print(template)

f = open('/tmp/challenge.c', 'w')
f.write(template)
f.close()

subprocess.run(['gcc', '-no-pie', '-O3', '-Wunused-result', '/tmp/challenge.c', '-o', '/tmp/challenge'])
