import math

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

def han(t, c):
    n = len(t)
    result = list()
    for f in range(0, n):
        z = [0]*n
        z[f] = t[f]
        for i in range(f+1, n):
            z[i] = z[i-1] * math.floor(t[i] / z[i-1])
        for i in range(f-1, -1, -1):
            z[i] = z[i+1] / math.ceil(z[i+1]/t[i])

        print("+{}+{}+{}+".format("-"*5, "-"*5, "-"*7))
        print("|{:^5}|{:^5}|{:^7}|".format("Ti'", "Ci", "Ui"))
        print("+{}+{}+{}+".format("-"*5, "-"*5, "-"*7))
        for i in range(n):
            print("|{:5}|{:5}|{:7.2f}|".format(z[i], c[i], c[i]/z[i]), end="")
            print(" <" if i == f else " /\\" if i < f else " \\/")
            print("+{}+{}+{}+".format("-"*5, "-"*5, "-"*7))
        ut = sum(c[i]/z[i] for i in range(n))
        print(" "*12 + "|{:7.2f}|".format(ut))
        print(" "*12 + "+{}+".format("-"*7))
        print()
        if ut <= 1:
            return True
        
    return False

import getopt
import sys
import json
HELP_MESSAGE = """Help:
Creates the han test table
-h, --help    Displays this help
-c "<array>"  The Ci column
-t "<array>"  The Ti column
-l            Shows the license
Columns must be rappresented in array form. E.g. "[1,2,3,4]"
"""  
try:
    opts, args = getopt.getopt(sys.argv[1:], "hlc:t:", ["help"])
except getopt.GetoptError:
    print("Error in arguments\n")
    print(HELP_MESSAGE)
    sys.exit(1)
settings = {
    "c" : [],
    "t": []
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


if len(settings["c"]) != len(settings["t"]):
    raise ValueError("All array must be equal length")

if han(settings["t"], settings["c"]):
    print("Test passed")
else:
    print("Test NOT passed")
