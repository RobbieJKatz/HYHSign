count = 0;
while True:
	counter = 0;
	if(count < 1):
		with open("./textfiles/"+str(count)+'.txt') as f:
			for i in range(592):
				s=f.readline();
				ss = s.split(',');

				print(ss[0],ss[1],ss[2])

				counter=counter+1

		count+=1
	else:
		count=0
		break


