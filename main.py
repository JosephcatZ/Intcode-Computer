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
    99:{
        "params":0,
        "code":"Halt",
        "paramRef":[]
    }
}
def refer(param,code):
    if param[1] == 1:
        return(int(param[0]))
    elif param[1] == 0:
        return(int(code[param[0]]))

def parse(code,opcode,*params):
    global pos
    p = pos
    opcode = intcodes[opcode]["code"]
    if opcode == "add":
        code[params[2][0]] = str(refer(params[0],code) + refer(params[1],code))
    elif opcode == "multi":
         code[params[2][0]] = str(refer(params[0],code) * refer(params[1],code))
    elif opcode == "less":
        if refer(params[0],code) < refer(params[1],code):
            code[params[2][0]] = "1"
        else:
            code[params[2][0]] = "0"
    elif opcode == "equal":
        if refer(params[0],code) == refer(params[1],code):
            code[params[2][0]] = "1"
        else:
            code[params[2][0]] = "0"
    elif opcode == "Jump-If-True":
        if refer(params[0],code) == 1:
            p = refer(params[1],code)
    elif opcode == "Jump-If-False":
        if refer(params[0],code) == 0:
            p = refer(params[1],code)
    elif opcode == "Input":
        j = None
        while j == None:
            j = int(input("> "))
            code[params[0][0]] = str(j)
    elif opcode == "Output":
        print(refer(params[0],code))
    elif opcode == "Halt":
        return(1)
    if p!= pos:
        print(code[p])
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
while pos < len(code):
    print(code[pos])
    if not(code[245]=="1" and code[246]=="99999"):
        print(pos,code[pos],code[245],code[246])
    if pos - targetPos == 0:
        if pos != 0:
            if intcodes[int(op)]["params"] == 3:
                code = parse(code,int(op),params[2],params[1],params[0])
            elif intcodes[int(op)]["params"] == 2:
                code = parse(code,int(op),params[1],params[0])
            elif intcodes[int(op)]["params"] == 1:
                code = parse(code,int(op),params[0])
            else:
                break;
        targetPos = pos + intcodes[int(code[pos][len(code[pos])-2:len(code[pos])])]["params"]+1
        op = code[pos][0:len(code[pos])-2]

        while len(op) < targetPos-pos-1:
            op = "0"+op
        params = []
        for i in op:
            params.append([0,int(i)])

        op = code[pos][len(code[pos])-2:len(code[pos])]


    else:
       params[(targetPos-pos)-1][0] = int(code[pos])
    pos+=1