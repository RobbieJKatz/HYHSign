import cv2,PIL

l=[[591,838],
[590,838],
[588,838],
[587,838],
[586,838],
[584,838],
[583,838],
[582,838],
[580,838],
[579,838],
[578,838],
[576,838],
[575,838],
[574,838],
[573,838],
[571,838],
[570,838],
[569,838],
[567,838],
[566,838],
[565,838],
[563,838],
[562,838],
[561,838],
[559,838],
[558,838],
[557,838],
[556,838],
[554,838],
[553,838],
[552,838],
[550,838],
[549,838],
[548,838],
[546,838],
[545,838],
[544,838],
[542,838],
[541,838],
[540,838],
[538,838],
[537,838],
[536,838],
[535,838],
[533,838],
[532,838],
[531,838],
[529,838],
[528,838],
[527,838],
[525,838],
[524,838],
[523,838],
[521,838],
[520,838],
[519,838],
[518,838],
[516,838],
[515,838],
[514,838],
[512,838],
[511,838],
[510,838],
[508,838],
[507,838],
[506,838],
[504,838],
[503,838],
[502,838],
[500,838],
[499,838],
[498,838],
[497,838],
[495,838],
[494,838],
[493,838],
[491,838],
[490,838],
[489,838],
[487,838],
[486,838],
[485,838],
[483,838],
[482,838],
[481,838],
[480,838],
[478,838],
[477,838],
[476,838],
[474,838],
[473,838],
[472,838],
[470,838],
[469,838],
[468,838],
[466,838],
[465,838],
[464,838],
[462,838],
[461,838],
[460,838],
[459,838],
[457,838],
[456,838],
[455,838],
[453,838],
[452,838],
[451,838],
[449,838],
[448,838],
[447,838],
[445,838],
[444,838],
[443,838],
[442,838],
[440,838],
[439,838],
[438,838],
[436,838],
[435,838],
[434,838],
[432,838],
[431,838],
[430,838],
[428,838],
[427,838],
[426,838],
[425,838],
[508,849],
[507,850],
[506,850],
[505,851],
[504,852],
[502,853],
[501,853],
[500,854],
[499,855],
[498,856],
[497,857],
[497,858],
[496,859],
[495,860],
[494,861],
[493,862],
[493,864],
[492,865],
[492,866],
[491,867],
[491,869],
[490,870],
[490,871],
[489,872],
[489,874],
[489,875],
[489,876],
[489,878],
[489,879],
[489,880],
[489,881],
[489,882],
[489,883],
[489,885],
[489,886],
[489,887],
[490,889],
[490,890],
[491,891],
[491,893],
[492,894],
[492,895],
[493,896],
[493,897],
[494,898],
[495,900],
[496,901],
[496,902],
[497,903],
[498,904],
[499,905],
[500,906],
[501,906],
[502,907],
[503,908],
[504,909],
[506,910],
[507,910],
[508,911],
[509,911],
[510,912],
[512,912],
[513,913],
[514,913],
[516,914],
[517,914],
[518,914],
[519,914],
[521,914],
[522,914],
[524,914],
[525,914],
[526,914],
[527,914],
[528,914],
[529,914],
[530,914],
[531,914],
[532,914],
[533,914],
[534,914],
[535,914],
[536,914],
[537,914],
[538,914],
[539,914],
[540,914],
[541,914],
[542,914],
[543,914],
[544,914],
[545,914],
[546,914],
[547,914],
[548,914],
[549,914],
[550,914],
[551,914],
[552,914],
[553,914],
[555,923],
[556,923],
[557,923],
[559,923],
[561,923],
[563,923],
[564,924],
[566,924],
[568,925],
[569,925],
[571,926],
[572,927],
[574,927],
[576,928],
[577,929],
[578,930],
[580,932],
[581,933],
[582,934],
[583,935],
[585,937],
[586,938],
[587,940],
[588,941],
[588,943],
[589,944],
[590,946],
[590,947],
[591,949],
[591,951],
[592,953],
[592,954],
[592,956],
[592,958],
[592,959],
[592,960],
[592,962],
[592,964],
[592,966],
[591,967],
[591,969],
[590,971],
[590,972],
[589,974],
[588,975],
[588,977],
[587,979],
[586,980],
[585,981],
[583,983],
[582,984],
[581,985],
[580,986],
[578,988],
[577,989],
[576,990],
[574,991],
[572,991],
[571,992],
[569,993],
[568,993],
[566,994],
[564,994],
[563,995],
[561,995],
[559,995],
[558,995],
[557,995],
[556,995],
[554,995],
[553,995],
[551,995],
[550,995],
[549,995],
[547,995],
[546,995],
[544,995],
[543,995],
[542,995],
[540,995],
[539,995],
[537,995],
[536,995],
[535,995],
[533,995],
[532,995],
[530,995],
[529,995],
[528,995],
[526,995],
[525,995],
[523,995],
[522,995],
[521,995],
[519,995],
[518,995],
[516,995],
[515,995],
[514,995],
[512,995],
[511,995],
[509,995],
[508,995],
[507,995],
[505,995],
[504,995],
[502,995],
[501,995],
[500,995],
[498,995],
[497,995],
[496,995],
[494,995],
[493,995],
[491,995],
[490,995],
[488,995],
[487,995],
[486,995],
[484,995],
[483,995],
[481,995],
[480,995],
[479,995],
[477,995],
[476,995],
[474,995],
[473,995],
[472,995],
[470,995],
[469,995],
[467,995],
[466,995],
[465,995],
[463,995],
[462,995],
[460,995],
[459,995],
[458,995],
[456,995],
[455,995],
[453,995],
[452,995],
[451,995],
[449,995],
[448,995],
[446,995],
[445,995],
[444,995],
[442,995],
[441,995],
[440,995],
[438,995],
[437,995],
[435,995],
[434,995],
[433,995],
[431,995],
[430,995],
[428,995],
[427,995],
[425,995],
[508,1008],
[507,1009],
[505,1009],
[504,1010],
[503,1011],
[502,1011],
[501,1012],
[500,1013],
[499,1014],
[498,1015],
[497,1016],
[497,1017],
[496,1018],
[495,1019],
[494,1020],
[494,1021],
[493,1022],
[492,1023],
[492,1024],
[491,1025],
[490,1026],
[490,1027],
[490,1029],
[489,1030],
[489,1031],
[488,1032],
[488,1033],
[488,1035],
[488,1036],
[488,1037],
[488,1038],
[488,1040],
[488,1040],
[488,1041],
[488,1043],
[488,1044],
[488,1045],
[488,1046],
[488,1048],
[489,1049],
[489,1050],
[489,1051],
[490,1052],
[490,1054],
[491,1055],
[491,1056],
[492,1057],
[493,1058],
[493,1059],
[494,1060],
[495,1061],
[496,1062],
[496,1063],
[497,1064],
[498,1065],
[499,1066],
[500,1067],
[501,1068],
[502,1068],
[503,1069],
[504,1070],
[505,1071],
[506,1071],
[508,1072],
[509,1072],
[510,1073],
[511,1073],
[512,1074],
[513,1074],
[515,1074],
[516,1075],
[517,1075],
[518,1075],
[520,1075],
[521,1075],
[522,1075],
[522,1075],
[523,1075],
[524,1075],
[526,1075],
[527,1075],
[529,1075],
[530,1075],
[531,1075],
[533,1075],
[534,1075],
[536,1075],
[537,1075],
[538,1075],
[540,1075],
[541,1075],
[543,1075],
[544,1075],
[545,1075],
[547,1075],
[548,1075],
[550,1075],
[551,1075],
[552,1075],
[554,1075],
[555,1075],
[557,1075],
[558,1075],
[559,1075],
[561,1075],
[562,1075],
[564,1075],
[565,1075],
[566,1075],
[568,1075],
[569,1075],
[571,1075],
[572,1075],
[573,1075],
[575,1075],
[576,1075],
[578,1075],
[579,1075],
[580,1075],
[582,1075],
[583,1075],
[584,1075],
[586,1075],
[587,1075],
[589,1075],
[590,1075],
[592,1075],
[575,995],
[576,995],
[577,995],
[578,995],
[579,995],
[580,995],
[581,995],
[582,995],
[583,995],
[584,995],
[586,995],
[587,995],
[588,995],
[589,995],
[590,995],
[591,995],
[592,995],
[593,995],
[594,995],
[595,995],
[597,995],
[598,995],
[599,995],
[600,995],
[601,995],
[602,995],
[603,995],
[604,995],
[605,995],
[606,995],
[608,995],
[609,995],
[610,995],
[611,995],
[612,995],
[613,995],
[614,995],
[615,995],
[616,995],
[617,995],
[619,995],
[620,995],
[621,995],
[622,995],
[623,995],
[624,995],
[625,995],
[626,995],
[627,995],
[628,995],
[630,995],
[631,995],
[632,995],
[633,995],
[634,995],
[635,995],
[636,995],
[637,995],
[638,995],
[639,995],
[641,995],
[642,995],
[643,995],
[644,995],
[645,995],
[646,995],
[647,995],
[648,995],
[649,995],
[650,995],
[652,995],
[653,995],
[654,995],
[655,995],
[656,995],
[657,995],
[658,995]]
previous = "d"
d=0
vidcap = cv2.VideoCapture('movie.mp4')
success,image = vidcap.read()
count = 0
success = True

print(l[0][1])

while success:
	previous = "d"
	f = open("./newTestFiles/"+str(count)+'.txt','w')
	for i in range(592):
		t=(image[l[i][0]][l[i][1]])
		r = t[0]
		g = t[1]
		b = t[2]

		if(r>220 and g>220 and b >220):
			s = "255;255;255"
		elif(r<10 and g<10 and b <10):
			s = "0;0;0"
		elif(140<r and r< 190 and 140<g and g< 190 and 140<b and b< 190 ):
			s="0;0;255"
		elif(r<60 and g >180):
			s= "255;255;200"
		elif(r<60 and g<180):
			s = "255;140;0"
		elif(b<60):
			s = "0;255;255"
	
		else:
			s=previous
			#d+=1
			

		f.write(s+'\n')
		if(s=="d"):
			d+=1
			print count
		previous =s
	f.close();
	success,image = vidcap.read()
	count += 1
print d


