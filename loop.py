
# n=int(input("enter"))
# i=2
# sum=0
# while i<=n*2:
#        sum=i+sum
#        i+=2
#        print(sum)

# n=int(input("enter"))
# i=2
# sum=0
# while   sum<1000:
#          sum+=i
#          print(i)
#          i+=2
# else:
#         print(sum)

# n=int(input("enter"))
# i=0
# while  i<100:
#        i+=7
#        print(i)

# n=int(input("enter"))
# i=1
# p=1
# while i<=n:
#       p*i
#       i+=1
#       print(p)

# a=int(input("enter1"))
# b=int(input("enter2"))
# c=str(input("symoble"))
# if  c=="+":
#     print(a+b)
# elif  c=="-":
#     print(a-b)
# elif c=="*":
#    print(a*b)
# elif  c=="/":
#     print(a/b)
# else:
#     print("invalid")
    

# n=int(input("enter"))
# i=0
# ans=0
# while i<=n:
#     a=int(input("number1"))
#     b=input("symble")
#     c=int(input("number2"))
#     if  b=="+":
#        ans+=a
#     elif  b=="-":
#        ans-=a
#     elif b=="*":
#        ans*=a
#     elif b=="/":
#        ans/=a
#     i+=1
# print(ans)    


# n=int(input("enter"))
# sum=0
# while n<0:
#     sum=sum+n%10
#     N=n//10
# else:
#     print(sum)

# n=int(input("enter"))
# i=1
# sum=0
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if  sum==n:
#         print(n,"perfect number")
# else:
#      print(n,"not perfect number")


# n=int(input("enter"))
# i=1
# while i<n:
#     if n%7==0:
#          print("even natural number")
#     i+=1
# else:
#      print("not an even natural number")

# n=int(input("enter"))
# i=1
# sum=0
# while  i<=n:
#     if n%3==0:
#        print("divisible by 3")
#     sum+=i
#     i+=1
# else:
#    print("are not divisible by 3")

# n=int(input("enter"))
# sum=0
# while n>0:
#     sum=sum+n%10
#     n=n//10
#     print(sum)

# n=123456
# reversed=0
# while n != 0:
#     digit=n%10
#     reversed=reversed*10+digit
#     n//=10
# print("reversed_num"+str(reversed))

n=int(input("enter"))
sum=0
if (n>=100) and (n<=999):
    l=n
    while l>0:
        a=l%10
        a1=1
        while a>0:
            a1=(a1*a)
            a=a-1
        sum+=a1
        l=l//10
    if n==sum:
        print("Yes")
    else:
        print("No") 
else:
    print("Enter Valid Input")               
   