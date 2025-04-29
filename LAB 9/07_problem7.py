def ispelindrome(string):

    st=''.join(ch.lower() for ch in string if ch.isalpha())
    
    if st==st[::-1]:
        print("The string is pelindrome")
    else:
        print("The string is not pelindrome")

str=input("Enter the string:")

ispelindrome(str)