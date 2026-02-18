#r= range(4)
#print (r)

def days():
    d=["mon","tue","wed","thu","fri","sat","sun"]
    i=0;
    while True:
        yield d[i]
        i=(i+1)%7

day=days()
print(next(day))
print(next(day))
print(next(day))
print(next(day))