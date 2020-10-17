#This is the program to identify the class name of given ip address in network
#This program works for both decimal and binary notation
#It is a menu driven program
import math
print("enter 1 for decimal notation or 2 for binary")
d=int(input())
if d==1:
    print("enter decimal ipaddress")
    s=input()
    x=s.find('.')
    ip=s[0:x]
    ip1=int(ip)
    if ip1<=127 and ip1>=0:
        print("class A")
    else:
        if ip1>=128 and ip1<= 191:
            print("class B")
        else:
            if ip1>=192 and ip1<=223:
                print("class C")
            else:
                if ip1>=224 and ip1<=239:
                    print("class D")
                else:
                    if ip1>=240 and ip1<=255:
                        print("class E")
                    else:
                        print("your input is out of range")

if d==2:
    print("enter binary notation")
    s1=input()
    x1=s1.find('.')
    ip2=s1[0:x1]
    #print(ip2)
    su=0.0
    for i in range(len(ip2)):
        if ip2[i]=='1':
            #print(i,8-i)
            e=math.pow(2,(7-i))
            su=su+e
    #print(su)
    su1=int(su)
    if su1<=127 and su1>=0:
        print("class A")
    else:
        if su1>=128 and su1<= 191:
            print("class B")
        else:
            if su1>=192 and su1<=223:
                print("class C")
            else:
                if su1>=224 and su1<=239:
                    print("class D")
                else:
                    if su1>=240 and su1<=255:
                        print("class E")
                    else:
                        print("your input is out of range")

