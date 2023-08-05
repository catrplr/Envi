n = int(input("Enter a postive interger"))
list1=[n]
while n <= 0:
    print("Invalid Integer")
    n = int(input("Enter a postive interger"))
print("The number u given is ", n)
while n != 1:
    if n % 2 ==1:
       n =int(3*n+1)
    else:
        n=int(n/2)
    list1.append(n)  
print ("Collatz conjecture:",list1)
print ("Collatz conjecture",len(list1)-1)
