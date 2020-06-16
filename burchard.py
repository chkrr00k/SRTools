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

def Urmpo(n, z):
    if z < 1 - 1/n:
        return (n - 1) * (2 ** (z / (n - 1)) - 1) + 2 ** (1 - z) - 1
    else:
        return n * (2 ** (1 / n) - 1)
    
def burchard(t, c):
    x = [math.log2(t[i]) - math.floor(math.log2(t[i])) for i in range(len(t))]
    for i in range(len(x)):
        print("X{} := {:.4f}".format(i, x[i]))
    
    z = max(x) - min(x)
    print("\nZ := {:.4f}".format(z))
    U = sum(c[i]/t[i] for i in range(len(t)))
    Ur = Urmpo(len(t), z)
    print("Urmpo(N={}, Z={:.4f}) := {:.4f}".format(len(t), z, Ur))
    print("\nU := {:.4f} {} Urmpo:= {:.4f}".format(U, "<=" if U<=Ur else ">", Ur))
    return U <= Ur

import getopt
import sys
import json
HELP_MESSAGE = """Help:
Creates the burchard test table
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

if burchard(settings["t"], settings["c"]):
    print("Test passed")
else:
    print("Test NOT passed")
