x = 0
i = x
loop = True
loop2 = True


while loop == True:
    i = i + 1
    x = i
    print(x)
    loop2 = True
    
    while loop2 == True:
          
        if x % 2 == 0:
            x = x / 2            
                        
        else:
            x = (x * 3) + 1
            
        if x == 1:
            loop2 = False

    
        
            
# if x % 2 == 0: pari
