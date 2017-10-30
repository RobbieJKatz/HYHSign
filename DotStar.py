count = 0;
while True:
	counter = 0;
	if(count < 400):
		with open("./textfiles/"+str(count)+'.txt') as f:
			for i in range(592):
				s=f.readline();
				ss = s.split(',');
				y=l[counter][0]
				x=l[counter][1]

				counter=counter+1

		count+=1
	else:
		count=0
		break

