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
    99:{
        "params":0,
        "code":"Halt",
        "paramRef":[]
    }
}
def refer(param,code):
    if param[1] == 1:
        return(param[0])
    elif param[1] == 0:
        return(code[param[0]])

def parse(code,opcode,*params):
    opcode = intcodes[opcode]["code"]
    if opcode == "add":
        code[params[2][0]] = refer(params[0],code) + refer(params[1],code)
    elif opcode == "multi":
         code[params[2][0]] = refer(params[0],code) * refer(params[1],code)
    elif opcode == "Input":
        code[params[0][0]] = input(">")
    elif opcode == "Output":
        print(refer(code,params[0]))
    elif opcode == "Halt":
        return(1)
    return(code)


code =["11001","1","1","1","99"]
pos = 0
targetPos = 0
params = []
op = ""
while pos < len(code)-1:
    
    if pos - targetPos == 0:
        if pos != 0:
            if intcodes[int(op)]["params"] == 3:
                code = parse(code,int(op),params[0],params[1],params[2])
            elif intcodes[int(op)]["params"] == 3:
                code = parse(code,int(op),params[0])
            else:
                break;
        targetPos = pos + intcodes[int(code[pos][len(code[pos])-2:len(code[pos])])]["params"]+1
        print(targetPos)
        op = code[pos][0:len(code[pos])-2]
        while len(op) < 3:
            op = "0"+op
        print(op)
        params = []
        for i in op:
            params.append([0,i])
        op = code[pos][len(code[pos])-2:len(code[pos])]

    else:
       params[intcodes[int(op)]["params"]-(targetPos-pos)][0] = int(i)

    pos+=1