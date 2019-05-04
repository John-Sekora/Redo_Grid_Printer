# Part 2
def grid(n):
#    x = "x"
#    - = "-"
#    | = "|"
    num = int((n-3)/2)
    print("x" + "-"*num + "x" + "-"*num + "x")
    for i in range(num):
        print("|" + " "*num + "|" + " "*num + "|")
    print("x" + "-"*num + "x" + "-"*num + "x")
    for i in range(num):
        print("|" + " "*num + "|" + " "*num + "|")
    print("x" + "-"*num + "x" + "-"*num + "x")


# Part 3

def grid2(s,n):
    a = ("x" + "-"*n)*s + "x"
    b = ("|" + " "*n)*s + "|"
    for i in range(s):
        print(a)
        for i in range(s):
            print(b)
    print(a)

grid2(4, 6)
