import sys
class Root:
    _sv_=1

if __name__== '__main__':

    fname= sys.argv[1]
    f = open(fname, 'r')
    root= Root()
    while True:
        line = f.readline();
        line =line.replace("\n", "")
        cmds= line.rsplit(" ")
        if cmds[0] == "group":
            exec(f"root.{cmds[1]}={{}}")
            global gname
            gname= cmds[1]
        elif cmds[0] == "end":
            break
        elif cmds[0] == "var":
            try: 
                exec(f"root.{gname}[cmds[1]]= {cmds[2]}")
            except NameError:
                print("create a group before variable")
        elif cmds[0] == "print":
            exec(f"print(root.{cmds[1]})")
        
def run(fname):
    f = open(fname, 'r')
    root= Root()
    while True:
        line = f.readline();
        line =line.replace("\n", "")
        cmds= line.rsplit(" ")
        if cmds[0] == "group":
            exec(f"root.{cmds[1]}={{}}")
            global gname
            gname= cmds[1]
        elif cmds[0] == "end":
            break
        elif cmds[0] == "var":
            try: 
                exec(f"root.{gname}[cmds[1]]= {cmds[2]}")
            except NameError:
                print("create a group before variable")
        elif cmds[0] == "print":
            exec(f"print(root.{cmds[1]})")
    return root
    
        

        
    

