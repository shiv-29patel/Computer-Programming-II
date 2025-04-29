def ispangram(string):
    alpha={chr(i) for i in range(97,123)}
    s={ch.lower() for ch in string if ch.isalpha()}
    if alpha<=s:
        print("The given string is pangram")
    else:
        print("The given string is not pangram")

st=input("Enter the string:")
ispangram(st)

