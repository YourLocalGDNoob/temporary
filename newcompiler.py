from math import *
from sys import exit
from re import split

code = []
with open("editor.txt", "r") as file:
    code = file.read().split("\n")
for i in range(len(code)):
    line = code[i]
    si = 0
    for c in line:
        if c in [" ", "\t"]:
            si += 1
        else:
            break
    code[i] = line[si:len(line)]

var = {}
keys = []
functions = {}

def removeempty(line):
    new = []
    for i in line:
        if i != "":
            new.append(i)
    return new

def VAR(v, n, op, index):
    if v not in var:
        var[v] = 0
    if n in var:
        n  = var[n]
    if op == "=":
        var[v] = n
    elif op == "+":
        var[v] += n
    elif op == "-":
        var[v] -= n
    elif op in ["*", "×"]:
        var[v] *= n
    elif op in ["/", "÷"]:
        if n != 0:
            var[v] /= n
        else:
            exit(f"{index+1}: Division by 0\n{code[index]}")
    elif op == "%":
        var[v] %= n
    else:
        exit(f"{index+1}: Unknown variable operation\n{code[index]}")

def PRINT(v, nl, index):
    if v in var:
        print(var[v], end = "\n"*nl)
    else:
        exit(f"{index+1}: Print command error, variable given doesn't exist\n{code[index]}")    

def SIN(v, index):
    if v in var:
        var[v] = sin(var[v])
    else:
        exit(f"{index+1}: Sine command error, variable given doesn't exist\n{code[index]}")    

def COS(v, index):
    if v in var:
        var[v] = cos(var[v])
    else:
        exit(f"{index+1}: Cosine command error, variable given doesn't exist\n{code[index]}")    

def TAN(v, index):
    if v in var:
        var[v] = tan(var[v])
    else:
        exit(f"{index+1}: Tangent command error, variable given doesn't exist\n{code[index]}")

def DEG(v, index):
    if v in var:
        var[v] = var[v]*180/pi
    else:
        exit(f"{index+1}: Radian command error, variable given doesn't exist\n{code[index]}")

def RAD(v, index):
    if v in var:
        var[v] = var[v]*pi/180
    else:
        exit(f"{index+1}: Radian command error, variable given doesn't exist\n{code[index]}")

def ROUND(v, index):
    if v in var:
        var[v] = round(var[v])
    else:
        exit(f"{index+1}: Round command error, variable given doesn't exist\n{code[index]}")

def FLOOR(v, index):
    if v in var:
        var[v] = floor(var[v])
    else:
        exit(f"{index+1}: Floor command error, variable given doesn't exist\n{code[index]}")

def CEILING(v, index):
    if v in var:
        var[v] = ceil(var[v])
    else:
        exit(f"{index+1}: Ceiling command error, variable given doesn't exist \n{code[index]}")

def FOR(i, a, k, index):
    if len(a) == 1:
        try:
            a[0] = round(a[0])
        except:
            if a[0] in var:
                a[0] = round(var[a[0]])
            else:
                exit(f"{index+1}: For loop error, end value excpected to be integer or variable\n{code[index]}")
    elif len(a) == 2:
        try:
            a[0] = round(a[0])
        except:
            if a[0] in var:
                a[0] = round(var[a[0]])
            else:
                exit(f"{index+1}: For loop error, start value excpected to be integer or variable\n{code[index]}")
        try:
            a[1] = round(a[1])
        except:
            if a[1] in var:
                a[1] = round(var[a[1]])
            else:
                exit(f"{index+1}: For loop error, end number excpected to be integer or variable\n{code[index]}")
    else:
        exit(f"{index+1}: For loop error, too many or too little argument, must be (end) or (start end)\n{code[index]}")
    if k not in keys:
        try:
            k = int(k)
        except:
            exit(f"{index+1}: For loop error, function key expected to be an integer (rounded if float)\n{code[index]}")
        keys.append(round(k))
    else:
        exit(f"{index+1}: For loop error, function key already in use, please use a different one\n{code[index]}")
    if len(a) == 1:
        for _ in range(a[0]+1):
            var[i] = _
            read(index+1, code.index(f"end {k}", index))
    else:
        for _ in range(a[0], a[1]+1):
            var[i] = _
            read(index+1, code.index(f"end {k}", index))
    keys.remove(k)
    return code.index(f"end {k}", index)
def FUNCTION(n, a, index):
    print(a)
def read(start = 0, end = len(code)):
    INDEX = start
    while INDEX < end:
        line = removeempty(split(" |\t", code[INDEX]))
        if line in [[], ["end"]]:
            INDEX += 1
            continue
        key = line[0].lower()
        if key == "var":
            if line[3] not in ["pi", "e"]:
                try:
                    line[3] = float(line[3])
                except:
                    if line[3] in var:
                        line[3] = var[line[3]]
                    else:
                        exit(f"{INDEX+1}: Number expected for variable\n{code[INDEX]}")
            else:
                if line[3] == "pi":
                    line[3] = pi
                elif line[3] == "e":
                    line[3] = e
            VAR(line[1], line[3], line[2], INDEX)
        elif key == "print":
            newline = True
            if len(line) == 3:
                if line[2].lower() == "true":
                    pass
                elif line[2].lower() == "false":
                    newline=False
                elif line[2] in var:
                    if var[line[2]] == 1:
                        pass
                    elif var[line[2]] == 0:
                        newline = False
                    else:
                        exit(f"{INDEX+1}: Print command error, new line determinor variable expected to be 0 or 1\n{code[INDEX]}")
                else:
                    exit(f"{INDEX+1}: Print command error, newline determinor expected to be 'true' or 'false'\n{code[INDEX]}")
            PRINT(line[1], newline, INDEX)
        elif key in ["sin", "sine"]:
            SIN(line[1], INDEX)
        elif key in ["cos", "cosine"]:
            COS(line[1], INDEX)
        elif key in ["tan", "tangent"]:
            TAN(line[1], INDEX)
        elif key in ["rad", "torad", "radians", "toradians"]:
            RAD(line[1], INDEX)
        elif key in ["deg", "todeg", "degrees", "todegrees"]:
            DEG(line[1], INDEX)
        elif key == "round":
            ROUND(line[1], INDEX)
        elif key in ["ceil", "ceiling"]:
            CEILING(line[1], INDEX)
        elif key in ["flr", "floor"]:
            FLOOR(line[1], INDEX)
        elif key == "for":
            INDEX = FOR(line[1], line[2:len(line)-1], line[len(line)-1], INDEX)
        elif key in ["func", "function"]:
            if len(line) == 2:
                FUNCTION(line[1], [], INDEX)
            else:
                FUNCTION(line[1], line[2:len(line)], INDEX)
        else:
            exit(f"{INDEX+1}: Unknown keyword {line[0]}\n{code[INDEX]}")
        INDEX += 1
read()
