# SRTools
Simple collection of several real time system tools for job/task scheduling

## audsley.py

Creates the table for the audsley test

`-c "<array>"`  The Ci column  
`-b "<array>"`  The Bi column (avoid if not present)  
`-t "<array>"`  The Ti column  
`-d "<array>"`  The Di column (if present performs the test)  
`-h, --help`    Displays the help  
`-l`            Shows the license  
  
All columns must be rappresented in array form. E.g. `"[1, 2, 3, 4]"`

## han.py

Creates the table for the han test

`-c "<array>"`  The Ci column  
`-t "<array>"`  The Ti column  
`-h, --help`    Displays the help  
`-l`            Shows the license  
  
All columns must be rappresented in array form. E.g. `"[1, 2, 3, 4]"`

## servers.py

Creates the temporal tables for selected servers, needs turtle installed  

`-h`, `--help`    Displays this help  
`-l`            Shows the license  
-`c "<array>"`  The Ci column  
`-t "<array>"`  The Ti column  
`-r "<array>"`  The request column e.g. `"[[ra, c], [ra, c]]"` with ra and c the request time and the request's c  
`-e <ticks>`    The ticks to simulate (default: 40)  
`-T <number>`   The Ts of the server  
`-C <number>`   The Cs of the server  
All columns must be rappresented in array form. E.g. `"[1,2,3,4]"`

Supported servers:  
`--bg`          Background server  
`--ps`          Polling server  
`--tbs`         Total bandwith server  
`--pes`         Priority exchange server  

### Examples
Executes the background server  
```py servers.py -t "[4,10,32]" -c "[1,2,8]" -r "[[5,2],[14,3],[23,3]]" --bg```  
Executes both the background server and the total bandwifth server  
```py servers.py -t "[4,10,32]" -c "[1,2,8]" -r "[[5,2],[14,3],[23,3]]" --bg --tbs -C 2 -T 8```  
