a=input()
b=0
for i in range(int(len(a)/2)):
    if a[i]==a[len(a)-1-i]:
        b=b+1
    else:
        b=b-1
if b==int(len(a)/2):
    print("yes")
else:
    print("no")
