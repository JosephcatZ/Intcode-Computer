output = []

intcodes = {
    1:{
        "params":3,
        "code":"add",
        "paramRef":["int1","int2","outputPos"]
    },
    2:{
        "params":3,
        "code":"multi",
        "paramRef":["int1","int2","outputPos"]
    },
    3:{
        "params":1,
        "code":"Input",
        "paramRef":["storage"]
    },
    4:{
        "params":1,
        "code":"Output",
        "paramRef":["data"]
    },
    5:{
        "params":2,
        "code":"Jump-If-True",
        "ParamRef":["Bool","Line"]
    },
    6:{
        "params":2,
        "code":"Jump-If-False",
        "ParamRef":["Bool","Line"]
    },
    7:{
        "params":3,
        "code":"less",
        "ParamRef":["1","2","sto"]
    },
    8:{
        "params":3,
        "code":"equal",
        "ParamRef":["1","2","sto"]
    },
    9:{
        "params":1,
        "code":"mem",
        "ParamRef":["newData"]
    },
    99:{
        "params":0,
        "code":"Halt",
        "paramRef":[]
    }
}
def posfer(param):
    global code
    if param[1] == 0:
        while int(param[0]) > len(code)-1:
            code.append(0)
        return(int(param[0]))
    elif param[1] == 2:
        while int(param[0]) > len(code)-1:
            code.append(0)
        return(int(Memory+int(param[0])))
def refer(param):
    global code
    if param[1] == 1:
        
        return(int(param[0]))
    elif param[1] == 0:
        while int(param[0]) > len(code)-1:
            code.append(0)
        return(int(code[param[0]]))
    elif param[1] == 2:
        while int(param[0]) > len(code)-1:
            code.append(0)
        return(int(code[Memory+int(param[0])]))
Memory = 0
def parse(opcode,*params):
    global code
    global flag
    global pos
    p = pos
    opcode = intcodes[opcode]["code"]
    if opcode == "add":
        code[posfer(params[2])] = str(refer(params[0]) + refer(params[1]))
    elif opcode == "multi":
        code[posfer(params[2])] = str(refer(params[0]) * refer(params[1]))
    elif opcode == "less":
        if refer(params[0]) < refer(params[1]):

            code[posfer(params[2])] = "1"
        else:

            code[posfer(params[2])] = "0"
    elif opcode == "equal":
        if refer(params[0]) == refer(params[1]):
            code[posfer(params[2])] = "1"
        else:
            code[posfer(params[2])] = "0"
    elif opcode == "Jump-If-True":
        if refer(params[0]) >= 1:
            p = refer(params[1])
    elif opcode == "Jump-If-False":
        if refer(params[0]) == 0:
            p = refer(params[1])
    elif opcode == "Input":
        j = None
        while j == None:
            j = int(input("> "))
            code[posfer(params[0])] = str(j)
        #print(code[params[0][0]])
    elif opcode == "Output":
        k = refer(params[0])
        print(k,end = " ")
        output.append(k)
    elif opcode == "Halt":
        return(1)
    elif opcode == "mem":
        global Memory
        Memory = Memory + refer(params[0])
        #print(Memory)
    pos = p
    return(code)


code =[]
with open("input") as IN:
    for j in IN:
        for i in j.split("\n")[0].split(","):
            code.append(i)
pos = 0
targetPos = 0
params = []
op = ""
flag = False
def runCode():
    global code
    global pos
    global targetPos
    global params
    global op
    global flag
    pos = 0
    targetPos = 0
    params = []
    op = ""
    flag = False
    while pos < len(code):
        if pos - targetPos == 0:
            if pos != 0:
                if intcodes[int(op)]["params"] == 3:
                    code = parse(int(op),params[2], params[1],params[0])
                elif intcodes[int(op)]["params"] == 2:
                    code = parse(int(op),params[1],params[0])
                elif intcodes[int(op)]["params"] == 1:
                    code = parse(int(op),params[0])
                else:
                    break;
        
            targetPos = pos + intcodes[int(code[pos][len(code[pos])-2:len(code[pos])])]["params"]+1
            op = code[pos][0:len(code[pos])-2]
            if op == "203":
                flag = True
            while len(op) < targetPos-pos-1:
                op = "0"+op
            params = []
            print(op)
            for i in op:
                params.append([0,int(i)])

            op = code[pos][len(code[pos])-2:len(code[pos])]


        else:
            params[(targetPos-pos)-1][0] = int(code[pos])
        pos+=1

def format():
    global code
    out = ""
    for i in code:
        out+=(str(i)+",")
    print(out)