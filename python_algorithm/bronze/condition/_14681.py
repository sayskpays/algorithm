
section1,section2,section3,section4 = 1,2,3,4

a = int(input())
b = int(input())

if a>0 and b>0:
    print(section1)
elif a<0 and b>0:
    print(section2)
elif a<0 and b<0:
    print(section3)
else:
    print(section4)
