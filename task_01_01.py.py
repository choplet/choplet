a = int(input())
if a % 100 == 0 and a % 400 !=0:
    print ("yes")
elif a % 4 !=0:
    print("yes")
else:
    print("no")