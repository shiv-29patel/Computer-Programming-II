def count_alpha_digit(string):
    alpha_count=0
    digit_count=0
    for ch in string:
        if ch.isalpha():
            alpha_count+=1
        elif ch.isdigit():
            digit_count+=1
    dict={"No if alphabets":alpha_count,"No of digits":digit_count}
    return dict

s=input("Enter a string:")
x=count_alpha_digit(s)
print(x)            
