n=int(input("Enter the number of terms"))
a=0
b=1
print("The fibonacci series is:")
print(a)
print(b)
for i in range(2,n+1):
    c=a+b
    print(c)
    a=b
    b=c


'''
Output:
Enter the number of terms10
The fibonacci series is:
0
1
1
2
3
5
8
13
21
34
55
'''
