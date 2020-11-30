

def read_csv(filename):
    #Opens and reads everything
    f = open(filename, "r", encoding='UTF-8')
    x = f.read()
    x = x.split("\n")
    # converts each element to a tuple and appends to a list
    #I tried to do append((elm)) but that didn't work. I found this method, but it creates a comma at the end of the tuples
    li = []
    for elm in x:
        li.append((elm, ))
    return li


def generate_name_map(nodes):
    #Removes the last element in the tuples and generates a list.
    li = []
    lib = {}
    for elm in nodes:
        k = elm[0].split(",")
        k = k[0:2]
        li.append(k)
    #There is an empty list at the end of the listlist, which i remove using pop
    li.pop()
    #Converts the listlist to a library
    #print(len(li))
    for elm in li:
        lib[elm[0]] = elm[1]
    return lib


def name_edges(edges_arg, name_map, x= 0):
    li = []
    l = len(edges_arg)
    for elm in edges_arg:
        #Generates a list
        k = elm[0].split(",")
        #Maps edges id to what they represent
        person = k[0]
        movie = k[1]
        role = k[2]
        #Appends it all to a list
        k = name_map[person],name_map[movie],role
        li.append(k)
        x = x +1
        #For some reason the list index is out of range even though i use a for loop and not a range.
        #I have created this breakpoint which is equal to the lengh of the list.
        if x == l-1:
            break
    return li


def generate_movie_dictionary(named_edges_arg):
    #Ensures it only creates movies which has actors in
    #I create a set instead of a list to ensure there are no dublications
    dic = {x[1]:set() for x in named_edges_arg if x[2] != 'DIRECTED' }
    #Creates the dictionary with only actors
    for elm in named_edges_arg:
        if elm[2] != 'DIRECTED':
            dic[elm[1]].add((elm[0]))
    return dic




def get_actor_friends(movie_dictionary):
    #Creates an empty dictionary
    dic = {}
    for elm in movie_dictionary:
        name = list(movie_dictionary[elm])
        for i in range(0, len(name)):
            #i'm using sets to avoid dublicats
            dic[name[i]] = set()
    
    #Here I put everything into the dictionary
    for elm in movie_dictionary:
        name = list(movie_dictionary[elm])
        for i in name:
            for k in range(0, len(name)):
                #I'm using this if command to avoid the person being friends with the same person
                if i != name[k]:
                    dic[i].add(name[k])
    return dic



def main():
    #nodes = read_csv('nodes.csv')
    #edges = read_csv('edges.csv') 
    #print('nodes', nodes[0], 'edges', edges[0])
    #namemap = generate_name_map(nodes)
    #print('namemap:', namemap['345'])
    #named_edges = name_edges(edges, namemap)
    #print('named_edges:', named_edges[0])
    #movie_dict = generate_movie_dictionary(named_edges)
    #print('movie_dict:',movie_dict["The Matrix"])
    #actor_friends = get_actor_friends(movie_dict)
    #print('actor_friends:',actor_friends['Keanu Reeves'])
    None

if __name__ == "__main__":
	# Executes only if run as a script
	main()
    
