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

def audsley(c, b, t):
    r = [[ci + bi] for ci, bi in zip(c, b)]
    done = [False for ci in c]
    n = 1

    while(not all(done)):
        for i in range(0, len(c)):
            r[i].append(r[i][0] + sum([math.ceil(r[i][n-1] / t[k]) * c[k] for k in range(0, i)]))
            if(r[i][n] == r[i][n-1]):
                done[i] = True
        n += 1

    return r

def show(mx):
    for r in mx:
        found = False
        last = r[0]
        for i in range(1, len(r)):
            if last == r[i]:
                if found:
                    r[i] = " "*4+"\\"
                else:
                    found = True
            else:
                last = r[i]
                
    print("\n".join(["".join(["{:5}".format(i) for i in r]) for r in zip(*mx)]))
        




import getopt
import sys
import json
HELP_MESSAGE = """Help:
Creates the ausdley test table
-h, --help    Displays this help
-c "<array>"  The Ci column
-b "<array>"  The Bi column (avoid if not present)
-t "<array>"  The Ti column
-d "<array>"  The Di column (if present performs the test)
-l            Shows the license
Columns must be rappresented in array form. E.g. "[1,2,3,4]"
"""  
try:
    opts, args = getopt.getopt(sys.argv[1:], "hlc:b:t:d:", ["help"])
except getopt.GetoptError:
    print("Error in arguments\n")
    print(HELP_MESSAGE)
    sys.exit(1)
settings = {
    "c" : [],
    "b": None,
    "t": [],
    "d": None
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
    elif opt in ("-b"):
        settings["b"] = json.loads(arg)
    elif opt in ("-t"):
        settings["t"] = json.loads(arg)
    elif opt in ("-d"):
        settings["d"] = json.loads(arg)

if settings["b"] == None:
    settings["b"] = [0 for i in range(0, len(settings["c"]))]
if len(settings["c"]) != len(settings["t"]) != len(settings["b"]):
    raise ValueError("All array must be equal length")
if settings["d"] != None and len(settings["d"]) != len(settings["t"]):
    raise ValueError("All array must be equal length")
if settings["d"] != None:
    a = audsley(settings["c"], settings["b"], settings["t"])
    p = [t[0] <= t[1] for t in zip([c[-1] for c in a], settings["d"])]
    print("Passed" if all(p) else "Not passed")
    show(a)
    print("".join(["{:5}".format("  ~~~") if not i else "{:5}".format("") for i in p ]))
else:
    show(audsley(settings["c"], settings["b"], settings["t"]))
