import math

def dist_euclidiana(p1,p2):    
    dist = math.sqrt(math.pow(2,p1[0] - p2[0]) + math.pow(2,p1[1] - p2[1]))
    return dist