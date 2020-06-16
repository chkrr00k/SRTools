LICENSE_MESSAGE="""
    #############################################################
    #                                                           #
    #   This program is relased in the GNU GPL v3.0 license     #
    #   you can modify/use this program as you wish. Please     #
    #   link the original distribution of this software. If     #
    #   you plan to redistribute your modified/copied copy      #
    #   you need to relased the in GNU GPL v3.0 licence too     #
    #   according to the overmentioned licence.                 #
    #                                                           #
    #   "PROUDLY" MADE BY chkrr00k (i'm not THAT proud tbh)     #
    #                                                           #
    #############################################################
    #                                                           #
    #                                                           #
    #                            YEE                            #
    #                                                           #
    #                                                           #
    #############################################################
    """
import math

def tStar(t, c, d):
    u = sum(c[i]/t[i] for i in range(len(t)))
    return sum( (1 - d[i] / t[i]) * c[i] for i in range(len(t))) / (1 - u)

def BI(t, c):
    result = [sum(c)]
    stop = False
    i = 1
    while not stop:
        result.append(sum( math.ceil( result[i-1] / t[j]) * c[j] for j in range(len(t))))
        if result[i] == result[i-1]:
            stop = True
        i+=1
    return result

def getM(tS, bi):
    return min(tS, bi[-1])

def getD(t, d, m):
    result = list()
    for i in range(len(d)):
        current = d[i]
        while current < m:
            result.append(current)
            current += t[i]
    result.sort()
    return result

def processorDemand(t, d, c, times):
    result = list()
    for i in range(len(t)):
        tmp = list()
        for time in times:
            tmp.append((math.floor( (time - d[i]) / t[i]) + 1) * c[i])    
        result.append(tmp)
    result.append(list())
    for i in range(len(result[0])):
        result[-1].append(sum(result[j][i] for j in range(len(result)-1)))
    return result

def density(c, d):
    return sum(c[i]/d[i] for i in range(len(c)))

import getopt
import sys
import json
HELP_MESSAGE = """Help:
Creates the EDF test table
-h, --help    Displays this help
-c            The Ci column
-t            The Ti column
-d            The Di column
-l            Shows the license
Columns must be rappresented in array form. E.g. "[1,2,3,4]"
"""  
try:
    opts, args = getopt.getopt(sys.argv[1:], "hlc:t:d:", ["help"])
except getopt.GetoptError:
    print("Error in arguments\n")
    print(HELP_MESSAGE)
    sys.exit(1)
settings = {
    "c" : [],
    "t": [],
    "d": []
    }
for opt, arg in opts:
    if opt in ("-h", "--help"):
        print(HELP_MESSAGE)
        sys.exit(0)
    elif opt in ("-l"):
        print(LICENSE_MESSAGE)
        sys.exit(0)
    elif opt in ("-c"):
        settings["c"] = json.loads(arg)
    elif opt in ("-t"):
        settings["t"] = json.loads(arg)
    elif opt in ("-d"):
        settings["d"] = json.loads(arg)


if len(settings["c"]) != len(settings["t"]) != len(settings["t"]):
    raise ValueError("All array must be equal length")
if settings["d"] != None and len(settings["d"]) != len(settings["t"]):
    raise ValueError("All array must be equal length")

t = settings["t"]
c = settings["c"]
d = settings["d"]

den = density(c, d)
print("Density := {:.2f} ({})\n".format(den, den <= 1))
tS = tStar(t, c, d)
print("t* := {:.2f}\n".format(tS))
bi = BI(t, c)
print("BI := {}".format(bi[-1]))
for i in range(len(bi)):
    print(" |{:2} | {:4.2f} |".format(i, bi[i]))
m = getM(tS, bi)
print("max{{t*, bi}} := {:.2f}\n".format(m) )
D = getD(t, d, m)
print("D n D* := {}\n".format(D))
print("Processor demand :=")
pd = processorDemand(t, d, c, D)
for i in range(len(pd[0])):
    print("{:3}".format(D[i])+" |" + "|".join(["{:3}".format(pd[j][i]) for j in range(len(pd))]) + "| " + str(D[i] >= pd[-1][i]))
