def read_file(filename):
	#Some of the times i have to use encoding = 'utf8' I dont know why.
	#Some times that fails, hence the try except
	try:
		f = open(filename, "r",encoding="utf8")
		x = f.read()
	except:
		f = open(filename, "r")
		x = f.read()
	x = x.split("\n")
	#print(x)
	f.close()
	return x

def parse_csv_lines(lines):
	li = []
	for elm in lines:
		x = elm.split(';')
		li.append(x)
	#print(li)
	return li

def parse_delimited_lines(lines, delimiter):
	li = []
	for elm in lines:
		x = elm.split(delimiter)
		li.append(x)
	return li

def age_difference(lines):
	li = parse_csv_lines(lines)
	l = len(li)
	
	returnlist = []

	for i in range(0,l-1):
		returnlist.append(abs(float(li[i][1])-float(li[i][-1])))
	return returnlist



def find_unisex_names(male_names, female_names):
	#print(male_names)
	def list_to_set (listlist):
		li = []
		for elm in listlist:
			for i in elm:
				li.append(i)
		return set(li)
	male_set = list_to_set(male_names)
	female_set = list_to_set(female_names)
	unisex = male_set.intersection(female_set)
	return unisex

def build_name_dataset(female_names, male_names, unisex_names):


	#Generates a list of the female and male names
	def remove_unisex (listlist,unisex):
		li = []
		for elm in listlist:
			for i in elm:
				li.append(str(i))
		for elm in unisex:
			li.remove(str(elm))
		return li
	female_list_new = remove_unisex(female_names,unisex_names)
	male_list_new = remove_unisex(male_names,unisex_names)




	#Ads gender to names
	def gender(list_arg, gender):
		li = []
		for elm in list_arg:
			li.append(str(elm) + gender)
		return li
	female_list = gender(female_list_new, ',F')
	male_list = gender(male_list_new, ',M')


	#Ads u to unisex names
	unisex_list = []
	for elm in list(unisex_names):
		unisex_list.append(str(elm) + ',U')

	#Ads everything to a total list
	for elm in female_list:
		unisex_list.append(elm)	
	for elm in male_list:
		unisex_list.append(elm)


	#Tries to generate a new file called "all_names.csv"
	try:
		unisex_list.remove(',U')
	except:
		None

	#Tries to generate the csv file called all_names
	try:
		f = open("all_names.csv", "x")
		f.close()
	except:
		None

	#Opens the file and writes all the names to the file
	x = open('all_names.csv', "w")
	for elm in unisex_list:
		x.write(elm)
		x.write('\n')
	x.close()


def write_sorted_names(names):
	#Converts it from listlist to list
	def list_list_to_list (listlist):
		li = []
		for elm in listlist:
			for i in elm:
				li.append(i)
		return li
	name_list = list_list_to_list(names)


	#This generates the csv files
	for elm in name_list:
		try:
			file_name = str(elm[0])
			x = open(file_name + '.csv', 'x')
			x.close()

		except:
			None
	l = len(name_list)

	#This sorts the names into the csv files
	for i in range(0, l-1):
		file_name = name_list[i][0] + '.csv'
		p = open(file_name, 'w')
		for k in range(0,l-1):
			if name_list[i][0] == name_list[k][0]:
				p.write(name_list[k])
				p.write('\n')
		p.close()
	print('Done')
	return None


def main():
	#Here you will need to call some or all of the above functions to test that your code is working. Some functions will generate an output that is used as input in another function.
	read_file('municipalities-2005-2019.csv')
	parse_csv_lines(read_file('municipalities-2005-2019.csv'))
	parse_delimited_lines(read_file('municipalities-2005-2019.csv'),';')
	age_difference(read_file('municipalities-2005-2019.csv'))
	find_unisex_names(parse_csv_lines(read_file('male_names.csv')), parse_csv_lines(read_file('female_names.csv')))
	build_name_dataset(parse_csv_lines(read_file('female_names.csv')), parse_csv_lines(read_file('male_names.csv')), find_unisex_names(parse_csv_lines(read_file('male_names.csv')), parse_csv_lines(read_file('female_names.csv'))))
	write_sorted_names(parse_csv_lines(read_file('all_names.csv')))


if __name__ == "__main__":
	# Executes only if run as a script
	main()
