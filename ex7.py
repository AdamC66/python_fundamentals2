totalpeople = 3
distances= []
mins=[]
speeds=[]

#Get input from user through console, store distances and times(in minutes) in lists
def getinput():
    personnum = 0
    while personnum < totalpeople:
        print("how far did person{} (run in meters)?".format(personnum+1))
        distances.append(float(input()))
        print("How long (in minutes) did person {} run take to run {} metres?".format(personnum+1,distances[personnum]))
        mins.append(float(input()))   
        personnum += 1

#iterate over distances list (for x in range(len(distances))) calculate speeds and store in same index in new list (speeds)
def calcspeeds(mins,distances):
    for x in range(len(distances)):
        speeds.append(distances[x]/(mins[x]*60))
        #this just prints the speed so I can confirm my fastest function finds the correct answer.
        print(speeds[x])
    return(speeds)

#checks if all items in speeds list is the same
def all_same(speeds):
    return all(x == speeds[0] for x in speeds)

#find max speed max(speeds) , get index of that speed, add 1 and that's the fastest person
#person starts at 1, index starts at 0
def fastest(speeds):
    #first we should check if all runners tied
    if all_same(speeds) == True:
        print("Everyone tied at {} m/s".format(speeds[0]))
        return()
    #by converting the speeds list to a set, we remove duplicates
    #if there was a duplicate, len(twos_same) will be less than len(speeds)
    #this must mean two speeds are the same, and thus 2 runners tied.
    two_same = set(speeds)
    if (len(two_same)) < (len(speeds)):
        print("everyone had a good race")
        return()
#the above could be taken a step further and check if a) the tied runners had the fastest speed and/or b, not output anything
#if the tied speed was not the fastest., or just print "everyone had a good race" which would be the case in the original code.
    maxspeed = max(speeds)
    fastestperson = speeds.index(maxspeed)+1
    print("person {} was the fastest at {} m/s".format(fastestperson,maxspeed))

#call my functions
getinput()
speeds = calcspeeds(mins,distances)
fastest(speeds)
