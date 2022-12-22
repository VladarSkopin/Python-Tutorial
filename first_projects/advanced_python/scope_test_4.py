def outer():
    z = "local"

    def inner():
        # nonlocal z
        z = "nonlocal"  # shadowing
        print("inner:", z)
    inner()
    print("outer:", z)


outer()  # inner: nonlocal
