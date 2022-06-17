

def draw1(h):
    if(h==0):
        return
    draw1(h-1)

    for i in range(h):
        print("*")
    print("\n")

def draw2(h):
    for o in range(h):
        for i in range(o):
            print("*")
        print("\n")

print(draw1(5))
print(draw2(5))