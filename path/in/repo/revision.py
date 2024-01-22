n = 5
k = round(n/2)*2
for i in range(0,n,2):
    for j in range(0,k+1):
        print(end = " ")
    for j in range(0,i+1):
        print("*", end = " ")
    k = k-2
    
    print()
    
k = 1
for i in range(n-1,0,-2):
    for j in range(0, k+2):
        print(end = " ")
    k = k+2
    print()


n = int(input("Enter the no of lines: "))
for i in range(1,n+1):
    for k in range(1,n-i+1):
        print(" ", end = " ")
    for j in range(1,i+1):
        print(j, end = " ")
    for k in range(j-1,0,-1):
        print(k, end = " ")
    print()

