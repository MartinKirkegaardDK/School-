import numpy as np


def search_pascal_multiples_fast(row_limit):
    #generates the triangle 
    trow = [1]
    y = [0]
    li = []
    for x in range(row_limit):
        li.append(trow)
        trow=[(left+right) for left,right in zip(trow+y, y+trow)]
    
    #li is now a list of lists of all the value
    #now i'm creating a single list of the list of lists
    flat_list = []
    for sublist in li:
        for item in sublist:
            flat_list.append(item)
    
    number_list = []
    #Here i use the algorithm provided in the code to exclude the outermost 2 numbers in each row
    for r in range(row_limit):
        row = li[r]
        for i, number in enumerate(row):
            if i > 1 and i < len(row)-1: 
                number_list.append(number)
                
    #Here i convert the list to a numpy array
    a = np.array(number_list)
    #Here i create a dictionary of all the values and occurances
    unique, counts = np.unique(a, return_counts=True)
    dictionary = (dict(zip(unique, counts)))
    #Here I have chosen the name lemonade since its a fire song
    #If the occurances are more than 3, append the value to a list
    lemonade = []
    for value, occurance in dictionary.items():  # 
        if occurance > 3:
            li.append(value)
    #Returns lemonade
    return lemonade
    
#----------- DO NOT CHANGE ANYTHING BELOW THIS LINE


def search_pascal_multiples_slow(row_limit):

    # Building up Pascal's triangle with a dict of lists
    ptriangle = {}
    ptriangle[0] = [1]
    ptriangle[1] = [1,1]
    ptriangle[2] = [1,2,1]
    for r in range(3, row_limit):
        ptriangle[r] = []
        for i in range(len(ptriangle[r-1])+1):
            if i == 0: # on left border, so we just add 1
                ptriangle[r].append(1)
            elif i == len(ptriangle[r-1]): # on right border, so we just add 1
                ptriangle[r].append(1)
            else: # not on border, so we sum up the two numbers above
                ptriangle[r].append(ptriangle[r-1][i-1] + ptriangle[r-1][i])

    # Putting all numbers into one list, except the outermost 2 numbers in each row
    number_list = []
    for r in range(row_limit):
        row = ptriangle[r]
        for i, number in enumerate(row):
            if i > 1 and i < len(row)-1: # exclude the outermost 2 numbers in each row
                number_list.append(number)

    # Counting the numbers
    number_set = set(number_list) 
    pascal_multiples = []
    for unique_number in number_set:
        count = 0
        for number in number_list:
            if number == unique_number:
                count = count + 1
        if count > 3:
            pascal_multiples.append(unique_number)
    
    return sorted(pascal_multiples)


from timeit import default_timer as timer

def main():
	row_limit = 250

	start = timer()
	print(search_pascal_multiples_slow(row_limit))
	end = timer()
	runtime_slow = end-start

	start = timer()
	print(search_pascal_multiples_fast(row_limit))
	end = timer()   
	runtime_fast = end-start

	print(round(runtime_slow / runtime_fast, 2))

if __name__ == "__main__":
	main()