while True:
    x = int(input("Number? "))

    loop = True
    while loop == True:
        
        if x % 2 == 0:
            x = x / 2
            print(x)

        else:
            x = (x * 3) + 1
            print(x)

        if x == 1:
            loop = False

        print("")
