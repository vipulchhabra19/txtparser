#Author:  Vipul Chhabra

#. number of . will decide indentation and collapse property 
#over all logic is to maintain star numbers in a list and "." values in dictionary 
#to buffer next and previous line for "+" and "-"
import sys

line_index = 0

star_list = []
index = 1


line_buffer = {'len_linestart': 0, 'line': ''}
for line in sys.stdin:
	# print line
	line_start = line.split(' ', 1)[0]
	if not line.strip():	
		continue
	if '*' in line_start:
		if line_buffer['line']!= '':
			tabs = "\t"*line_buffer['len_linestart']
			new_line = line_buffer['line'].replace(line_buffer['line'].split(' ', 1)[0], tabs+'-')
			sys.stdout.write(new_line)
		line_buffer = {'len_linestart': 0, 'line': ''} 
		if len(line_start) == 1:
			star_list = []
			star_list.append(index)
			index +=1
			subindex = 1

		if  len(line_start) > 1:
			ind = len(line_start) - 1
			if len(star_list) > ind:
				star_list[ind] += 1
			else:
				star_list.append(1)

		new_line = line.replace(line_start, ".".join(str(e) for e in star_list[:len(line_start)]))		
		sys.stdout.write(new_line)
	
	elif '.' in line_start:
		# print "in .", len(line_start)
		if  line_buffer['len_linestart'] == 0:
			line_buffer['len_linestart'] = len(line_start)
			line_buffer['line'] = line
		elif line_buffer['len_linestart'] == len(line_start):
			tabs = "\t"*line_buffer['len_linestart']
			new_line = line_buffer['line'].replace(line_buffer['line'].split(' ', 1)[0], tabs+'-')
			line_buffer = {'len_linestart': len(line_start), 'line': line}
			sys.stdout.write(new_line)
		elif len(line_start) > line_buffer['len_linestart']:
			tabs = "\t"*line_buffer['len_linestart']
			new_line = line_buffer['line'].replace(line_buffer['line'].split(' ', 1)[0], tabs+'+')
			line_buffer = {'len_linestart': len(line_start), 'line': line}	

			sys.stdout.write(new_line)

	elif line!='':
		tabs = "\t"*(line_buffer['len_linestart']+1)
		line_buffer['line'] += tabs + line
