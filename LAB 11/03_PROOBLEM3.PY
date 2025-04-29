name=input("Enter your name:")
phone=input("Enter your phone number:")
Email=input("Enter your Email:")

v_card=f'''
Name={name}
Mo.No={phone}
Email={Email}
'''
filename=name.replace(" ","_") + ".vcf"

with open(filename,"w") as file:
    file.write(v_card)