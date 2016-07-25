import fileinput

#we initialize the first row
wholeText = fileinput.input();
currentindex = wholeText[0];			#our lines
total = int(currentindex.split('\t')[1]);		#our starting value
currentindex = currentindex.split('\t')[0];		#our starting index

for line in wholeText:			#each line's read and split
	values = line.split('\t');
	locationID = values[0];
	if(locationID != currentindex):		#if locationID is not equal to current 
		print(('{0}\t{1}'.format(currentindex, total)).replace("\n",""))	#print summed cash
		currentindex = locationID;											#and initialize to the new index
		total = 0;
	total += int(values[1].replace("\n",""))						#add the current cash to the right index
print(('{0}\t{1}'.format(currentindex, total)).replace("\n",""))			#final print