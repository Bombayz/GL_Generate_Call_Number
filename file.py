import json
import csv
from pprint import pprint

#====== input CSV file
o = open("GE_2.csv",'rU')

mydata = csv.DictReader(o)
name_author=[];
name_book=[];
year=[];
body = [];
st=[];
str_head = "General 810"
correct = [];

#======= input json -----
with open('author_json.json') as data_file:    
    data = json.load(data_file)
#pprint(data)


# print (data[0]['name'])

for row in mydata:
    name_author.append(row['name_author'])
    name_book.append(row['name_book'])
    year.append(row['year'])
#print(name_author[0])
#print(name_book[0])
#print(year)

for i in range(len(year)):
    # for i in range(len(data)):
	
    for s in range(len(name_author[i])):
    	st += name_author[i][s]
    	my_lst_str = ''.join(map(str, st))
    	for da in range(len(data)):
    		if(data[da]['name'] == my_lst_str):
    			# print ("Done")
    			correct.append(data[da]['number'])
    			# print correct
    				

    	# print my_lst_str
    if not correct:
    	print str_head+name_author[i][0]+" "+name_book[i][0]+" "+year[i]
    else:
    	st_1 = str_head+name_author[i][0]
    	st_2 = str(correct[-1])
    	st_3 = name_book[i][0]+" "+year[i]
    	print (st_1+st_2+st_3)
    	# print str_head+name_author[i][0]
    	# print correct[-1]
    	# print name_book[i][0]+" "+year[i]

    st=[];
    correct=[];


