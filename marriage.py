import sys
import timeit

# get relevant information from the data file
def getData():
    count = 0
    men = []
    women = []
    menPrefs = {}
    womenPrefs = {}
    # get the file
    infile = open(str(sys.argv[1]), 'r')
    # get the number of how many of each gender there are
    num = int(infile.readline())
    # for every line in the file..
    # initialization: infile is not empty
    # maintenance: there exists a line in infile
    # termination: terminate if there are no more lines in infile
    for line in infile:
        line = line.strip()
        line = line.split(' ')
        # add the men to a list, then link them and their preferences in a dictionary
        # the variable, count, separates the men from the women
        if (count < num):
            men += [line[0]]
            menPrefs[line[0]] = line
        # add the women to a list, then link them and their preferences in a dictionary
        else:
            women += [line[0]]
            womenPrefs[line[0]] = line
        count = count + 1
    return men, menPrefs, women, womenPrefs

# implement gale-shapley
def match():
    # call getData() to get the relevant information
    men, menPrefs, women, womenPrefs = getData()
    # initiate a dictionary for the pairs
    pairs = {}
    # initialization: the starting length of men is n so it's greater than 0
    # maintenance: as we go through the loop, men get removed and added back
    # the loop will continue as long as there's still somebody in the list
    # termination: terminate if the list of single men is empty
    while(len(men) > 0):
        # get a man in the list of single men
        man = men[0]
        # get a woman from his preference list
        woman = menPrefs[man][1]
        # if the woman is single..
        if(woman in women):
            # the man and the woman get engaged
            pairs[woman] = man
            # remove the man from the list of single men
            men.remove(man)
            # remove the woman from the list of single women
            women.remove(woman)
        # if the woman is not single..
        else:
            # find out who she's engaged to
            fiance = pairs[woman]
            # if she prefers the man over her fiance..
            if(womenPrefs[woman].index(man) < womenPrefs[woman].index(fiance)):
                # put her fiance back in the list of single men
                men.append(fiance)
                # the woman and the man get engaged
                pairs[woman] = man
                # remove the man from the list of single men
                men.remove(man)
        # take the woman out of the man's preference list now that he's proposed to her
        del menPrefs[man][1]
    # print the pairs
    # initialization: pairs is not empty
    # maintenance: there exists a p in pairs
    # termination: terminate if there is no more p in pairs
    for p in pairs:
        sys.stdout.write(str(pairs[p]) + ' ' + str(p) + '\n')

# the main function calls match and exits with result code 1 in the case of any errors
def main():
    try:
        match()
    except:
        exit(1)

main()
