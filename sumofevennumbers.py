n=int(input("Enter a number: ")) #gets the value from the user
i=1
sum=0
m=0
while (i<=n): #sets the condition
    if(i%2==0): #logic:even numbers are divisible by 2
        sum=sum+i 
        m+=1
    i+=1
print(f"Sum of even numbers within {n}: ",sum) #prints the sum
print(f"Number of even numbers within {n}: ",m) #prints the number of even numbers present
