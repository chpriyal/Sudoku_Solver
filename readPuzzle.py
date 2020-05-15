import numpy as np
def readPuzz():
	f = open("sudoku","r")
	arr = list()
	question = list()
	for x in f:
		for n in x:

			if(n.isnumeric()):
				if( int(n)>=0 & int(n)<=9):
					arr.append(int(n))	
		question.append(arr)
		arr = list()
	question = np.array(question)
	print(question)
	print("Press Y if the problem is correct. Press N to exit")
	x = input()
	if(x.lower!='y'):
		return (question,False)
	return (question,True)