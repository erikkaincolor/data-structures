"""Functions to parse a file containing villager data."""



#once i figure out how to pass villagers.csv as an arg on the CL, then i can test whether these functions work or not

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    file_strings=open(filename, "r") #create file object, open it
    empty_set = set() #init an empty set
    for lines in file_strings:
        split_string_into_list= lines.rstrip().split("|")    #strip whitespace in string + split each line in file of strings into sep. list items by the "|" + 
        second_item=split_string_into_list[1]               #i want to do something to the second item in the list.
        empty_set.add(second_item)                  #using .add set method to add to empty set
    return (empty_set)

#when interactively calling function, use "" around filename!!!!!
#>>> all_species("villagers.csv")



















def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names

    species=[1]
    vil_name=[0]
    """

    villagers = []

    file_name=open(filename, "r") #create file object, open it

    for lines in file_name: #for each line in 
        profile=lines.rstrip().split("|") #get rid of whitespace, and put into list of strings by "|"
        #same as name, species = line.rstrip().split("|")[:2]
        #2nd indice not included
        if search_string in lines:
            villagers.append(profile[0]) #add first item in former list to new list

    return sorted(villagers)
#>>> get_villagers_by_species("villagers.csv", search_string="Bear")























def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    file = open(filename, "r") #create file object, open it
    #open file
    #make object a list by stripping whitesoace and splitting byy delimiter into list
    #if new_list[3] = "Education", append name to Education list....names are first thing in list
    result = []
    education = []
    fashion = []
    fitness = []
    nature = []
    play = []
    music = []
    
    for lines in file:
        new_line = lines.rstrip().split("|")
        
        if "Education" in new_line[3]:
            education.append(new_line[0])
        if "Fashion" in new_line[3]:
            fashion.append(new_line[0])
        if "Fitness" in new_line[3]:
            fitness.append(new_line[0])
        if "Nature" in new_line[3]:
            nature.append(new_line[0])
        if "Play" in new_line[3]:
            play.append(new_line[0])
        if "Music" in new_line[3]:
            music.append(new_line[0])
        
    result = [sorted(education), sorted(fashion), sorted(fitness), sorted(nature), sorted(play), sorted(music)]
    return [result]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    all_data=[]
    file=open(filename)
    for lines in file:
        all_data.append(tuple(lines.rstrip().split("|"))) #add onto the empty list the tupled lines

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    file = open(filename)
    for line in file:
        line.rstrip().split("|") #list of items
        if villager_name == line[0]:
            print(line[4])
        else:
            return None
    
    


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
