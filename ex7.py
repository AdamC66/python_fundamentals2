totalpeople = 3
distances= []
mins=[]
speeds=[]
def getinput():
    personnum = 0
    while personnum < totalpeople:
        print("how far did person{} (run in meters)?".format(personnum+1))
        distances.append(float(input()))
        print("How long (in minutes) did person {} run take to run {} metres?".format(personnum+1,distances[personnum]))
        mins.append(float(input()))   
        personnum += 1

def calcspeeds(mins,distances):
    for x in range(len(distances)):
        speeds.append(distances[x]/(mins[x]*60))
        print(speeds[x])
    return(speeds)


def fastest(speeds):
    if 
    maxspeed = max(speeds)
    fastestperson = speeds.index(maxspeed)+1
    print("person {} was the fastest at {} m/s".format(fastestperson,maxspeed))


getinput()
speeds = calcspeeds(mins,distances)
fastest(speeds)
