x = "global"


def foo():
    global x
    x = x * 2
    print(x)


foo()  # globalglobal
