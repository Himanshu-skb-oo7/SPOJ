for i in range(int(input())):
    x = int(input())
    i = 1
    mark = x
    while True:
        mark -= i
        i += 1
        if mark <= 0:
            break
    mark *= -1
    if i%2 == 1:
        print ("TERM",x,"IS",str(i-1-mark)+"/"+str(1+mark))
    else:
        print ("TERM",x,"IS",str(1+mark)+"/"+str(i-1-mark))
