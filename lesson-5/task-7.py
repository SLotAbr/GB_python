import json


with open('task-7-text-i.txt', 'r') as f_i:
	lines = f_i.readlines()
	# 3th variable is a number of firms with positive income
	f_lenght, avg_profit, pos = len(lines), 0, 0
	lines = [lines[i].split() for i in range(f_lenght)]
	lines = [(lines[i][0], int(lines[i][-2])-int(lines[i][-1])) 
			 for i in range(f_lenght)]
	[(pos:=pos+1, avg_profit:=avg_profit+lines[i][1]) 
	 for i in range(f_lenght) if lines[i][1]>0]

with open('task-7-text-o.json', 'w') as f_o:
	data = [dict(lines), 
			dict([('average_profit', round(avg_profit/pos,4))])
			]
	json.dump(data, f_o)
	