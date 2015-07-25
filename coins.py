a={}
def coins(n):
    if n==0:
        return 0
    elif n in a:
        return a[n]
    else:
        a[n]=max(n,(coins(n/2))+(coins(n/3))+(coins(n/4)))
        return a[n]
while True:
    try:
        n=int(raw_input())
        print coins(n)
    except:
        break
