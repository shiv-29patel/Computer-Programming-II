"""If a positive integer is entered through the keyword,
 write a recursive function to obtain the prime factors of the number.
"""
def prime_fact(n,i=2):
    if n==1:
        return
    if n%i==0:
        print(i)
        prime_fact(n//i,i)
    else:
        prime_fact(n,i+1)
n=int(input("Enter the number:"))

print(f"The prime factores if {n} is :")

prime_fact(n)
