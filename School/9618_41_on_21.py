""" def Unknown(X,Y):                
        if X<Y:
            print(X+Y)
            return Unknown(X+1,Y)*2

        else:
            if X==Y:
                return 1
            else:
                print(X+Y)
                return(Unknown(X-1,Y)/2)
            

    print("unknown when X=10 and Y=15")
    print(Unknown(10,15))

    print("unknown when X=10 and Y=10")
    print(Unknown(10,10)

    print("unknown when X=15 and Y=10")
    print(Unknown(15,10)) """


