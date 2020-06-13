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
import copy
import math
RU_LBL = "Ru"
R_LBL = "R"

def table(x, y, cols, rows, indexed=True):
    turtle.goto(x-2, y)
    for i in range(0, cols+1):
        turtle.goto(x+ i*15-2, y+ rows*15+5)
        turtle.pendown()
        turtle.goto(x+ i*15-2, y)
        turtle.penup()
        if indexed:
            turtle.write(i)
    turtle.goto(x-2, y)
    for i in range(0, rows+1):
        turtle.goto(x-2, y+ i*15+5)
        turtle.pendown()
        turtle.goto(x+ cols*15-2, y+ i*15 + 5)
        turtle.penup()
    turtle.home()

def show(x, y, e, t, c, r, f, *ar, tags=None):
    if tags:
        for i in range(0, len(tags)):
            turtle.goto(x, y+ i*15 +20)
            turtle.write(tags[i])
        x+=15
    capacity = list()
    for ru, re, ti, cap in f(e+1, copy.deepcopy(t), copy.deepcopy(c), copy.deepcopy(r), *ar):
        if len(capacity) != len(cap):
            for i in range(0, len(cap)-len(capacity)):
                capacity.append([])
        for i in range(0, len(cap)):
            capacity[i].append(cap[i])
        if ti < e:
            if ru >= 0:
                turtle.setx(x+ ti*15)
                turtle.sety(y+ 20+ru*15)
                turtle.write(RU_LBL)
            for pr in re:
                turtle.setx(x+ ti*15)
                turtle.sety(y+ 20+pr*15)
                turtle.write(R_LBL)
                
    printcap = all([True if len(c) > 0 else False for c in capacity])
    size = turtle.pensize()
    
    if printcap:
        yy = y+(len(t)+1)*15
        for ca in capacity:
            yy += max(ca)*15 + 20
            turtle.pensize(size+1)
            turtle.goto(x, yy+20-max(ca)*15)
            turtle.pendown()
            
            for pos in range(0, len(ca)):
                cc = ca[pos] if ca[pos] != -math.inf else 0
                sx = x+ pos*15
                sy = yy+ 20-(cc)*15

                turtle.goto(sx, sy)

            turtle.penup()

    turtle.pensize(size)
    table(x, y, e, len(t)+1)
    if printcap:
        yy = (len(t)+1)*15+y
        for ca in capacity:
            yy += max(ca)*15 + 20
            table(x, yy+15-max(ca)*15, e, max(ca))
    turtle.penup()
    return yy

def bkgd(end, t, c, r, _cs, _ts):
    time = 0
    p = [0 for i in range(0, len(t))]
    while time < end:
        ready = list()
        running = -1
        for i in range(0, len(p)):
            if time % t[i] == 0:
                p[i] = 0
            if running < 0 and p[i] < c[i]:
                p[i] += 1
                running = i
            elif running >= 0 and p[i] < c[i]:
                ready.append(i)

        for i in range(0, len(r)):
            if running < 0 and r[i][0] <= time and r[i][1] > 0:
                r[i][1] -= 1
                running = len(t)
            elif running >= 0 and r[i][0] <= time and r[i][1] > 0 and len(t) not in ready:
                ready.append(len(t))
                
        yield running, ready, time, []
        time += 1

def serverPos(t, ts, ins=True):
    for i in range(0, len(t)):
        if t[i] > ts:
            if ins:
                t.insert(i, ts)
            return i
    t.append(ts)
    return len(t)

def plig(end, t, c, r, cap, ts):
    time = 0
    p = [0 for i in range(0, len(t)+1)]
    ser = serverPos(t, ts)
    c.insert(ser, cap)
    while time < end:
        ready = list()
        running = -1
        rr = -1
        for i in range(0, len(p)):
            if time % t[i] == 0:
                p[i] = 0
            if i == ser:
                ex = False
                for j in range(0, len(r)):
                    if running < 0 and r[j][0] <= time and r[j][1] > 0 and p[i] < c[i]:
                        r[j][1] -= 1
                        running = i
                        
                        ex = True
                        rr = i
                    elif running >= 0 and r[j][0] <= time and r[j][1] > 0 and i not in ready and p[i] < c[i]:
                        ready.append(i)
                        ex = True
            else:    
                if running < 0 and p[i] < c[i]:
                    p[i] += 1
                    running = i
                elif running >= 0 and p[i] < c[i]:
                    ready.append(i)
        cret = c[ser]-p[ser]
        if not ex and running > ser:
            p[ser] = c[ser]
            cret = 0
        if cret > 0 and ser not in ready:
            ready.append(ser)
        yield running, ready, time, [cret]

        if rr != -1:
            p[rr] += 1
            
        time += 1

def tbs(end, t, c, r, cap, ts):
    time = 0
    p = [0 for i in range(0, len(t))]
    Us = 1-sum([c[i]/t[i] for i in range(0, len(t))])
    rad = [r[i][0]+r[i][1]/Us for i in range(0, len(r))]
    for i in range(0, len(rad)-1):
        if rad[i] > r[i+1][0]:
            rad[i] = r[i+1][0]
    curCap = 0
    j = 0
    while time < end:
        ready = list()
        running = -1
        if time in [ra[0] for ra in r]:
            curCap = r[j][1]
        for i in range(0, len(p)):
            if time % t[i] == 0:
                p[i] = 0
        deadline = [(time//t[i])*t[i]+t[i] if p[i] < c[i] else math.inf for i in range(0, len(t))]
        prec = deadline.index(min(deadline))
        useCap = False
        if j < len(r) and rad[j] < min(deadline) and time >= r[j][0]:
            if curCap > 0 and r[j][1] > 0:
                prec = -1
                running = 0
                r[j][1] -= 1
                useCap = True
                if r[j][1] == 0 and j+1 < len(r):
                    j+=1
                    
        for i in range(0, len(p)):
            if p[i] < c[i]:
                if i == prec: 
                    p[i] += 1
                    running = i+1
                else:
                    ready.append(i+1)
        yield running, ready, time, [curCap]
        if useCap:
            curCap -= 1
        time += 1

def pes(end, t, c, r, cap, ts):
    time = 0
    p = [0 for i in range(0, len(t)+1)]
    pc = [0 for i in range(0, len(t)+1)]
    ser = serverPos(t, ts)
#    t.insert(ser, ts)
    c.insert(ser, cap)
    while time < end:
        ready = list()
        running = -1
        rr = -1
        waste = ser

        if time % ts == 0:
            pc[ser]=cap
        for i in range(0, len(p)):
            if time % t[i] == 0:
                p[i] = 0
        for i in range(0, len(p)):
            if i == ser:
                for j in range(0, len(r)):
                    if running < 0 and r[j][0] <= time and r[j][1] > 0 and any([ca > 0 for ca in pc]):
                        capDonor = math.inf
                        rea = math.inf
                        for ii in range(0, len(p)):
                            if pc[ii] > 0:
                                capDonor = min(capDonor, ii)
                            if p[ii] < c[ii] and ii != ser:
                                rea = min(rea, ii)
                        if capDonor != math.inf and capDonor <= rea:
                            r[j][1] -= 1
                            running = i
                            rr = i
                            waste = capDonor
                    elif running >= 0 and r[j][0] <= time and r[j][1] > 0 and i not in ready and pc[i] <= 0:
                        ready.append(i)
            else:    
                if running < 0 and p[i] < c[i]:
                    p[i] += 1
                    running = i

                elif running >= 0 and p[i] < c[i]:
                    ready.append(i)
        
        yield running, ready, time, pc[ser:]

        if running >= 0 and running != ser:
            for i in range(0, running):
                if pc[i] > 0:
                    pc[i] -= 1
                    pc[running] += 1
                    break
        elif running == ser:
            p[rr] += 1
            pc[waste] -= 1
        elif running < 0:
            for i in range(0, len(pc)):
                if pc[i] > 0:
                    pc[i] -= 1
                    break
        
        time += 1
        
def defr(end, t, c, r, cap, ts):
    time = 0
    p = [0 for i in range(0, len(t)+1)]
    ser = serverPos(t, ts)
    c.insert(ser, cap)
    while time < end:
        ready = list()
        running = -1
        rr = -1
        for i in range(0, len(p)):
            if time % t[i] == 0:
                p[i] = 0
            if i == ser:
                ex = False
                for j in range(0, len(r)):
                    if running < 0 and r[j][0] <= time and r[j][1] > 0 and p[i] < c[i]:
                        r[j][1] -= 1
                        running = i
                        
                        ex = True
                        rr = i
                    elif running >= 0 and r[j][0] <= time and r[j][1] > 0 and i not in ready and p[i] < c[i]:
                        ready.append(i)
                        ex = True
            else:    
                if running < 0 and p[i] < c[i]:
                    p[i] += 1
                    running = i
                elif running >= 0 and p[i] < c[i]:
                    ready.append(i)
        cret = c[ser]-p[ser]
        if cret > 0 and ser not in ready:
            ready.append(ser)
        yield running, ready, time, [cret]

        if rr != -1:
            p[rr] += 1
            
        time += 1
        
e = 40
t = [4,10,32]
c = [1, 2, 8]
r = [[5, 2], [14, 3], [23, 3]]
l = 10
import turtle

cansize = (1000, 1000)


import getopt
import sys
import json
HELP_MESSAGE = """Help:
Creates the temporal tables for selected servers
-h, --help    Displays this help
-l            Shows the license
-c "<array>"  The Ci column
-t "<array>"  The Ti column
-r "<array>"  The request column e.g. "[[ra, c], [ra, c]]"
              with ra and c the request time and the c
-e <ticks>    The ticks to simulate (default: 40)
-T <number>   The Ts of the server
-C <number>   The Cs of the server
Columns must be rappresented in array form. E.g. "[1,2,3,4]"

Supported servers:
--bg          Background server
--ps          Polling server
--tbs         Total bandwith server
--pes         Priority exchange server
--des         Deferrable server
"""

try:
    opts, args = getopt.getopt(sys.argv[1:], "hlc:r:t:e:T:C:", ["des", "bg", "ps", "tbs", "pes", "help"])
except getopt.GetoptError:
    print("Error in arguments\n")
    print(HELP_MESSAGE)
    sys.exit(1)
s = {
    "c" : [],
    "r": [],
    "t": [],
    "e": 40,
    "cs": 0,
    "ts": 0,
    "f": []
    }
for opt, arg in opts:
    if opt in ("-h", "--help"):
        print(HELP_MESSAGE)
        sys.exit(0)
    elif opt in ("-l"):
        print(LICENSE_MESSAGE)
        sys.exit(0)
    elif opt in ("-e"):
        s["e"] = int(arg)
    elif opt in ("-C"):
        s["cs"] = int(arg)
    elif opt in ("-T"):
        s["ts"] = int(arg)
    elif opt in ("-c"):
        s["c"] = json.loads(arg)
    elif opt in ("-t"):
        s["t"] = json.loads(arg)
    elif opt in ("-r"):
        s["r"] = json.loads(arg)
    elif opt in ("--bg"):
        s["f"].append(bkgd)
    elif opt in ("--ps"):
        s["f"].append(plig)
    elif opt in ("--tbs"):
        s["f"].append(tbs)
    elif opt in ("--pes"):
        s["f"].append(pes)
    elif opt in ("--des"):
        s["f"].append(defr)

if len(s["t"]) != len(s["c"]):
    print("-t must be long as -c")
    sys.exit(2)
for rr in s["r"]:
    if len(rr) != 2:
        print("every subarray in -r must be 2 long")
        sys.exit(3)
    elif not(isinstance(rr[0], int) and isinstance(rr[1], int)):
        print("the subarray values must be an integer")
        sys.exit(4)
        
turtle.setup(cansize[0],cansize[1])
turtle.getscreen().setworldcoordinates(0,cansize[0],cansize[1],0)
turtle.penup()
turtle.speed(10)
turtle.color("black")
turtle.bgcolor("white")

#l=show(0, l + 40, e, [6,8,38], [1,2,9], [[6,2],[10,1],[14,4],[27,2]], pes, 3, 10)

for f in s["f"]:
    l = show(0, l, s["e"], s["t"], s["c"], s["r"], f, s["cs"], s["ts"]) + 40

input("Press Enter to exit...")

##l = show(0, l, e, t, c, r, bkgd, None, tags=["p1", "p2", "p3", "Ra"])
##l = show(0, l + 40, e, t, c, r, plig, 2, 8, tags=["p1", "SS", "p2", "p3"])
##l = show(0, l + 40, e, t, c, r, tbs, 3, 8, tags=["TS", "p1", "p2", "p3"])
##l = show(0, l + 40, e, t, c, r, pes, 2, 8, tags=["PE", "p1", "p2", "p3"])
##
##l = show(0, l + 40, e, [10,15,35], [3,3,7], [[4,1],[9,2],[19,3],[29,2],[36,1]], pes, 2, 8, tags=["PE", "p1", "p2", "p3"])

#py servers.py -t "[4,10,32]" -c "[1,2,8]" -r "[[5,2],[14,3],[23,3]]" --bg
#py servers.py -t "[4,10,32]" -c "[1,2,8]" -r "[[5,2],[14,3],[23,3]]" --bg --tbs -C 2 -T 8

