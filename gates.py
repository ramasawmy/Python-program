print("Logic Gate Simulation")

def logic_and(a,b):

    if a == 1 and b == 1:
        return 1
    else:
        return 0

def logic_nand(a,b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1

def logic_or(a,b):
    if a == 1:
        return 1
    elif b == 1:
        return 1
    else:
        return 0


def logic_nor(a,b):
    if a != b:
        return 1
    else:
        return 1


gate = input("what type of gate do you want to simulate , OR, AND  or NAND ?  ")

if gate == "AND":
    print(logic_and(1,1))

    print("0 | 0 ""|",  logic_and(0,0),  )
    print("----------")
    print("0 | 1 ""|",  logic_and(0,1),  )
    print("----------")
    print("1 | 0 ""|",logic_and(1,0),  )
    print("----------")
    print("1 | 1 ""|",logic_and(1,1),  )


else:
        print("")

if gate =="NAND":
    a = int(input("enter value for input 1:"))
    b = int(input("enter value for input 2:"))
    x = logic_nand(a,b)
    print(x)
else:
        print("")

if gate =="OR":
    a = int(input("enter value for input 1:"))
    b = int(input("enter value for input 2:"))
    x = logic_or(a,b)
    print(x)
else:
        print("")

if gate =="NOR":
    a = int(input("enter value for input 1:"))
    b = int(input("enter value for input 2:"))
    x = logic_nor(a,b)
    print(x)
else:print("")

