def SGPA(n):
    sub=8
    c=0
    if n==1 or n==3:
        c=21
    elif n==2 or n==4:
        c=23
        sub=9
    elif n==5:
        c=22
    a=[]
    b=[]
    for i in range(1,sub+1):
        m=0 
        y=int(input("Enter the marks of subject 18MCA"+str(n)+str(i)+" : "))
        x=y
        if x in range(0,50):
            x=0
        elif x in range(50,55):
            x=4
        elif x in range(55,60):
            x=6
        elif x in range(60,70):
            x=7
        elif x in range(70,80):
            x=8
        elif x in range(80,90):
            x=9
        elif x in range(90,101):
            x=10
        if i<=5 or (n==5 and i==8):
            m=3
        else:
            m=2
        a.append(x*m)
        b.append(y)
        res="{:.2f}".format(sum(a)/c)
    print("Your Total Score is : "+str(sum(b)))
    print("Your Total Grade Point is : "+str(sum(a)))
    print("Your CGPA for Semester "+str(n)+" is "+str(res))
def CGPA():
    l=[0,21,23,21,23,22]
    arr=[]
    for i in range(1,6):
        x=float(input("Enter the Semester "+str(i)+" SGPA if doesn't apply enter 0 : "))
        if x==0:
            l[i]=0
        arr.append(x*l[i])
    cgpa="{:.2f}".format(sum(arr)/sum(l))
    print("Your Total CGPA is : "+str(cgpa))
    

print("\t\t\t\t MCA CGPA")
ch=1
while(ch==1 or ch==2):
    print("*** Please select your choice ***")
    print("1 => Know you your SGPA")
    print("2 => Know you your CGPA")
    print("Any other number to exit")
    ch=int(input())
    if ch==1:
        n=int(input("Enter Your sem : "))
        SGPA(n)
    elif ch==2:
        CGPA()